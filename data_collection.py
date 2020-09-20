#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:29:57 2020

@author: sudippandey
"""

import glassdoor_scapper as gs
import pandas as pd

path="/Users/sudippandey/Documents/GitHub/postdoc_salary_proj/chromedriver"
df=gs.get_jobs('postdoc', 400, False, path, 10)
df.to_csv('glassdoor_postdoc_jobs.csv', index=False)