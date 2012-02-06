#!/usr/bin/env python
import sys
import json
import zmq

class RPCClient(object):
    
    def __init__(self, server_addrs):
        ctx = zmq.Context()
        self.socket = ctx.socket(zmq.REQ)
        for addr in server_addrs:
            self.socket.connect(addr)

    def call(self, method, *args):
        req = {
            'method' : method,
            'args' : args
        }
        self.socket.send(json.dumps(req))
        rep = json.loads(self.socket.recv())
        if rep['error'] == 'NO_ERROR':
            return rep['ret']
        else:
            raise Exeption(rep)

def main(start, end, addr):
    import os
    import time
    start_time = time.time()
    pid = os.getpid()

    client = RPCClient(addr)
    total = 0
    for i in xrange(start, end+1):
        x = i 
        ret = client.call('mul', x, x)
        total = client.call('add', total, ret)
    print '[%s]calcuate %d*%d + ... + %d*%d = %d, take time %d' % (pid, start, start, end, end, total, time.time() - start_time)

if __name__ == "__main__":
    start = int(sys.argv[1]) 
    end = int(sys.argv[2])
    addr = sys.argv[3:]
    main(start, end, addr)
