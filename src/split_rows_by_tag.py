#!/usr/bin/env python
import csv

out = open('data/results_with_tags_split.csv', 'w+')
f = open('data/results_with_tags_denormalized.csv')
writer = csv.writer(out)
for line in f:                                 
    parts = line.rstrip().split(',')
    tags = parts[4].split('|')
    for tag in tags:
        writer.writerow(parts[0:4] + [tag] + [parts[5]])
out.flush()
out.close()
