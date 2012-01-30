#!/usr/bin/env python
'''
Produce test data and send to zeromq socket
'''
import time
import json
import random
import zmq

from makedataset import load_data

def replay(input_file,to_addr):
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.bind(to_addr)

    #data = input_file.readlines()
    data = load_data(input_file)

    send_start = time.time()

    for record in data:
        socket.send(json.dumps(record))
    socket.send('')
    send_end = time.time()


    print '%d records sent at %f, took %f' %(len(data), send_end, send_end - send_start)

def main():
    import sys
    replay(sys.stdin, sys.argv[1])

if __name__ == "__main__":
    main()
