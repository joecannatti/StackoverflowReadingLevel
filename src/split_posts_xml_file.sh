#!/usr/bin/env bash
set -e

cd data

head -2 Posts.xml >> head.xml
tail -1 Posts.xml >> tail.xml

for i in {1..8}; do cp head.xml Posts$i.xml; done

split -l 2000000 Posts.xml

cat tail.xml >> xaa
cp xaa Posts1.xml 

cat xab >> Posts2.xml 
cat tail.xml >> Posts2.xml

cat xac >> Posts3.xml 
cat tail.xml >> Posts3.xml

cat xad >> Posts4.xml 
cat tail.xml >> Posts4.xml

cat xae >> Posts5.xml 
cat tail.xml >> Posts5.xml

cat xaf >> Posts6.xml 
cat tail.xml >> Posts6.xml

cat xag >> Posts7.xml 
cat tail.xml >> Posts7.xml

cat xah >> Posts8.xml 
cat tail.xml >> Posts8.xml

rm xaa xab xac xad xae xaf xag xah head.xml tail.xml
