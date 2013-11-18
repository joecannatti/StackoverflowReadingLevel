#!/usr/bin/env bash
set -e

for i in {2..8}; do
  cat data/raw_output$i.csv >> data/raw_output1.csv
  rm -v data/raw_output$i.csv
done
mv data/raw_output1.csv data/results.csv
