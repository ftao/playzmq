#!/usr/bin/env python
'''
Produce test data and send to zeromq socket
'''
import time
import json
import random
import zmq

def produce(addr, speed):
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.bind(addr)
    second = int(time.time())
    while True:

        start = time.time()

        for i in xrange(speed):
#            latitude = random.randrange(0, 360) - 180
#            longitude = random.randrange(0, 360) - 180
#            temperature =  random.randrange(1, 40) - 20
            pm25 = random.randrange(0, 500)
            socket.send(json.dumps({
#                'latitude' : latitude,
#                'longitude' : longitude,
                'time' : second + i * 1.0 / speed,
#                'temperature' : temperature,
                'pm25' :  pm25
            }))

        end = time.time()
        print 'second=%d all data sent at %f, took %f' %(second, end, end-start)

        if end-start < 1:
            time.sleep(start + 1 - end)
        second += 1

def main():
    import sys
    produce(sys.argv[1], int(sys.argv[2]))

if __name__ == "__main__":
    main()
