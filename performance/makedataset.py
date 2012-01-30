#!/usr/bin/env python
import sys
import json
import random 

def make_data_set(size):
    data = []

    for i in xrange(size):
        data.append({
            'seq' : i,
            'from' : random.randrange(0,10),
            'to' : random.randrange(0,10),
            'flag_foo' : random.randrange(0,1),
            'flag_bar' : random.randrange(0,1),
            'flag_far' : random.randrange(0,1),
            'flag_boo' : random.randrange(0,1),
            'flag_fao' : random.randrange(0,1),
            'flag_bor' : random.randrange(0,1),
            'hlen' : random.randrange(20, 512),
            'blen' : random.randrange(0, 10240)
        })

    return data


def load_data(input_file):
    data = []
    for line in input_file:
        data.append(json.loads(line.strip()))
    return data

def gen_data(size):
    outf = sys.stdout
    for record in make_data_set(size):
        json.dump(record, outf)
        outf.write('\n')

if __name__ == "__main__":
    size = int(sys.argv[1])
    gen_data(size)

