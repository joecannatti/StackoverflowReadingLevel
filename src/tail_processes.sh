#!/usr/bin/env bash
for i in {1..8}; do
  echo "Process $i"
  tail -1 log/process$i.txt
done
