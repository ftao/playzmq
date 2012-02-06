#coding=utf-8
# Task ventilator
# Binds PUSH socket to tcp://localhost:5557
# Sends batch of tasks to workers via that socket
#
# Author: Lev Givon <lev(at)columbia(dot)edu>

import zmq
import random
import time

context = zmq.Context()

# Socket to send messages on
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

# Socket with direct access to the sink: used to syncronize start of batch
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

print "Press Enter when the workers are ready: "
_ = raw_input()
print "Sending tasks to workers…"

# The first message is "0" and signals start of batch
sink.send('0')

for line in open('word.txt', 'r'):
    sender.send(line)

sender.send('\0')

print 'All data are sent'
#print "Total expected cost: %s msec" % total_msec

# Give 0MQ time to deliver
time.sleep(1)
