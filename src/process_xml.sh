#!/usr/bin/env bash
for i in {1..8}; do 
  python src/readability_calculator_map.py data/Posts$i.xml data/raw_output$i.csv log/process$i.txt &
done
watch 'bash src/tail_processes.sh'
