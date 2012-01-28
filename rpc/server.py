#!/usr/bin/env python
import sys
import zmq
import json

class RPCServer(object):
    
    SERVICES = {}

    def __init__(self, bind_to):
        ctx = zmq.Context()
        self.socket = ctx.socket(zmq.REP)
        self.socket.bind(bind_to)

    def register(self, name, func):
        self.SERVICES[name] = func

    def run(self):
        while True:
            req = json.loads(self.socket.recv())
            rep = self.handle_req(req)
            self.socket.send(json.dumps(rep))

    def handle_req(self, req):
        method = req['method']
        args = req['args']
        if method not in self.SERVICES:
            return {'error' : 'SERVICE_NOT_FOUND'}
        else:
            try:
                ret = self.SERVICES[method](*args)
                return {
                    'error' : 'NO_ERROR',
                    'ret' : ret
                }
            except:
                return {
                    'error' : 'INTERNAL_ERROR',
                }
       
def main():
    server = RPCServer(sys.argv[1])
    server.register('add', lambda x,y:x+y)
    server.register('mul', lambda x,y:x*y)
    server.run()


if __name__ == "__main__":
    main()
