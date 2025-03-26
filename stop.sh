#!/bin/bash

if [ ! -f pids.txt ]; then
    echo "No pids.txt file found!"
    exit 1
fi

while read -r pid; do
    echo "Stopping process $pid..."
    kill -9 "$pid" 2>/dev/null
done < pids.txt

rm -f pids.txt
echo "All FastAPI processes stopped."
