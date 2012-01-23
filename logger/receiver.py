#!/usr/bin/env python
import sys
import zmq

def start_receiver(addr, topics):
    ctx = zmq.Context()
    sub = ctx.socket(zmq.SUB)
    for topic in topics:
        sub.setsockopt(zmq.SUBSCRIBE, topic)
    sub.connect(addr)
    while True:
        topic, msg = sub.recv_multipart()
        print topic, msg

if __name__ == "__main__":
    addr = "tcp://localhost:%d" % int(sys.argv[1])
    start_receiver(addr, sys.argv[1:])
