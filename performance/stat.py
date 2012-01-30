#!/usr/bin/env python
'''
Do stat calucation on data
'''
import time
import json
import sys
import itertools
import zmq

def stat(data, field):
    total = 0
    count = 0
    for item in data:
        total += item[field]
        count += 1
    return total, count, total * 1.0 /count

def get_data_stream(socket):
    while True:
        msg = socket.recv()
        if msg == '':
            break
        yield json.loads(msg)

def main():
    input_addr = sys.argv[1]
    ctx = zmq.Context()
    input_socket = ctx.socket(zmq.SUB)
    input_socket.connect(input_addr)
    input_socket.setsockopt(zmq.SUBSCRIBE, '')
    ret =  stat(get_data_stream(input_socket), 'hlen')
    print time.time(), ret

if __name__ == "__main__":
    main()
