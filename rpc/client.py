#!/usr/bin/env python
import sys
import json
import zmq

class RPCClient(object):
    
    def __init__(self, server_addr):
        ctx = zmq.Context()
        self.socket = ctx.socket(zmq.REQ)
        self.socket.connect(server_addr)

    def call(self, method, *args):
        req = {
            'method' : method,
            'args' : args
        }
        self.socket.send(json.dumps(req))
        rep = json.loads(self.socket.recv())
        return rep

def main(addr, start, count):
    import os
    import time
    start_time = time.time()
    pid = os.getpid()

    client = RPCClient(addr)
    for i in xrange(start, start+count):
        x = i 
        y = i+1
        ret = client.call('mul', x, y)
    #    print '[%s]call mul(%s,%s)=%s' %(pid, x, y, ret['ret'])

    print '[%s]all request done, take %d' % (pid, time.time() - start_time)

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
