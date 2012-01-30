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

def per_second_pm25_stat(data):
    for second, records in itertools.groupby(data, key=lambda x:int(x['time'])):
        #records = list(records)
        #all_recv = time.time()
        total,count,avg = stat(records, 'pm25')
        now = time.time()
        print 'time=%f second=%d total_record=%s, avg=%f ' %(now, now-second, second, count, avg)
        #print 'time=%f recv_take=%f calc=%f second=%d total_record=%s, avg=%f ' %(now, all_recv-second, now-all_recv, second, count, avg)

def get_data_stream(socket):
    while True:
        msg = socket.recv()
        yield json.loads(msg)

def main():
    input_addr = sys.argv[1]
    ctx = zmq.Context()
    input_socket = ctx.socket(zmq.SUB)
    input_socket.connect(input_addr)
    input_socket.setsockopt(zmq.SUBSCRIBE, '')
    per_second_pm25_stat(get_data_stream(input_socket))


if __name__ == "__main__":
    main()
