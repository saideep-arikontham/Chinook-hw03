#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
from utils import *
import pandas as pd

db = 'data/chinook.db'  #data/chinook.db
con = make_con(db)
query = '''select count(*) as composer_count_with_jimmy_name from Track where Composer like '%Jimmy%';'''
df = get_query(query,con)
print("composers having 'Jimmy' in their name")
print(df)




