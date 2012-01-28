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



def main():
    client = RPCClient(sys.argv[1])
    print 'call mul 3 4'
    print 'ret', client.call('mul', 3, 4)

    print 'call add 3 5'
    print 'ret', client.call('add', 3, 5)

    print 'call sub 3 5'
    print 'ret', client.call('sub', 3, 5)


if __name__ == "__main__":
    main()
