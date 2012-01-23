#!/usr/bin/env python
'''
This is the app that do the logging
'''

import sys
import logging
import time
import zmq
from zmq.log.handlers import PUBHandler

def app():
    logger = logging.getLogger("")
    logger_worker = logging.getLogger("main.worker")
    logger_web = logging.getLogger("main.web")
    i = 0
    while True:
        j = i * i
        print 'loop', i
        logger.debug("loop %i", i)
        logger_worker.info("Get Result %s*%s=%s" %(i,i,j))
        time.sleep(1)
        logger_web.debug("10.0.0.1 /help 200 OK ")
        i += 1

def setup_logger(bind_to):
    #handler = PUBHandler(bind_to)
    handler = LoggerNameAsTopicHandler(bind_to)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

class LoggerNameAsTopicHandler(PUBHandler):

    def emit(self, record):
        """Emit a log message on my socket."""
        try:
            topic, record.msg = record.msg.split(TOPIC_DELIM,1)
            topic = topic.encode()
        except:
            topic = "".encode()
        try:
            msg = self.format(record).encode()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
        topic_list = []

        if self.root_topic:
            topic_list.append(self.root_topic)

        if record.name != 'root':
            topic_list += record.name.split('.')

        topic_list.append(record.levelname.encode())

        if topic:
            topic_list.append(topic)

        topic = '.'.encode().join(topic_list)

        # map str, since sometimes we get unicode, and zmq can't deal with it
        self.socket.send_multipart([topic,msg])
    
if __name__ == "__main__":
    addr = "tcp://*:%d" % int(sys.argv[1])
    setup_logger(addr)
    app()
        

        
        
