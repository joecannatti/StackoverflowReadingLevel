#!/usr/bin/env python
import pandas as pd
import numpy as np


data = pd.read_csv('data/results.csv', names=('id', 'word_count', 'accepted_answer_id', 'fk_reading_level', 'tags', 'parent_id', 'creation_date'),
                               dtype={'fk_reading_level': np.float},
                               parse_dates=['creation_date'],
                               header=None, 
                               index_col='id')

data = pd.merge(data, data, how='left', left_on='parent_id', right_index=True, suffixes=('', '_parent'), copy=True)
data['tags'] = data['tags'].fillna(data['tags_parent'])
data = data.ix[:,:'creation_date']
data.to_csv('data/results_with_tags_denormalized.csv')


