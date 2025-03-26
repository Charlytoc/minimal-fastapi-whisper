#!/bin/bash

nohup python main.py > fastapi.log 2>&1 &
echo $! >> pids.txt
echo "FastAPI started with PID: $!"
