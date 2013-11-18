#!/usr/bin/env python
import xml.etree.cElementTree
import csv
import time
from readability_score.calculators.fleschkincaid import *
from bs4 import BeautifulSoup
import re
import gc
import json
from multiprocessing.pool import ThreadPool
import sys

context = xml.etree.cElementTree.iterparse(open(sys.argv[1]), events=('end',))
current_title = None
rows = 0
writes = 0
start_time = time.time()
outfile = open(sys.argv[2], 'w+')
logfile = open(sys.argv[3], 'w+')
writer = csv.writer(outfile)

def parseTags(tagsStr):
    tagsStr = re.sub("^<", '', tagsStr)
    tagsStr = re.sub(">$", '', tagsStr)
    return [tag for tag in tagsStr.split("><") if tag]

def cleanBody(bodyStr):
    soup = BeautifulSoup(bodyStr)
    to_extract = soup.findAll(['pre', 'code', 'ul'])
    for item in to_extract:
        item.extract()
    bodyStr = str(soup)
    return re.sub("<[^>]*>", '', bodyStr)

def log(goodRows, badRows, results):
  return "Good Rows: " + str(goodRows) + "\tBad Rows: " + str(badRows) + "\t%: " + str((goodRows + badRows) / (15979180.0 / 8)) + "\tTime Elapsed: " + str((time.time() - start_time) / 60) + "\n"

results = []
badRows = 0
goodRows = 0
for event, elem in context:
  try:
    body = cleanBody(elem.attrib["Body"])
    tags = ''
    if ("Tags" in elem.attrib):
      tags = elem.attrib["Tags"] 
    accepted_answer_id = 0
    if ("AcceptedAnswerId" in elem.attrib):
      accepted_answer_id = elem.attrib["AcceptedAnswerId"] 
    tags = parseTags(tags)
    fk = FleschKincaid(body, locale='en_US')
    gradeLevel = fk.us_grade
    word_count = fk.scores['word_count']
    rows = []
    if len(tags) > 0:
      results.append((elem.attrib["Id"], word_count, accepted_answer_id, gradeLevel, "|".join(tags), 0))
    else:
      results.append((elem.attrib["Id"], word_count, accepted_answer_id, gradeLevel, None, elem.attrib["ParentId"]))
    goodRows += 1
  except:
    badRows += 1
  if (goodRows + badRows) % 5000 == 0:
      logfile.write(log(goodRows, badRows, results))
      logfile.flush()
      [writer.writerow(row) for row in results]
      outfile.flush()
      results=[]
      gc.collect()
  elem.clear()

[writer.writerow(row) for row in results]
outfile.flush()
outfile.close()
logfile.flush()
logfile.close()
