#!/usr/bin/env python
import pandas as pd
import numpy as np

langs = ['ruby', 'python', 'perl', 'php', 'c', 'c++', 'java', 'scala', 'clojure', 'c#', 'f#', 'matlab', 'mathematica', 'r', 'scheme', 'common-lisp', 'cobol','bash', 'javascript', 'coffeescript', 'dart', 'ocaml', 'haskell', 'ml', 'prolog']


data = pd.read_csv('data/results_with_tags_split.csv', 
                               names=('post_id', 'word_count', 'accepted_answer_id', 'fk_reading_level', 'tags', 'parent_id', 'creation_date'), 
                               parse_dates=['creation_date'],
                               header=None)
data.fk_reading_level = data.fk_reading_level.astype('object').convert_objects(convert_numeric=True)

tag_means = data.groupby(by='tags').mean()
levels = tag_means['fk_reading_level'].copy()

sorted_results = levels[langs]
sorted_results.sort()

sorted_results.plot(kind='bar', ylim=(6.7,9))
