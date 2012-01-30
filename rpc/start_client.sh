#!/bin/sh

python client.py tcp://127.0.0.1:5555 0 10000 &
python client.py tcp://127.0.0.1:5555 10000 10000 &
python client.py tcp://127.0.0.1:5555 20000 30000 &
