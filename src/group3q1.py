#!/usr/bin/env python
# coding: utf-8

# In[19]:


import sqlite3
from utils import *
import pandas as pd

db = 'data/chinook.db'  #data/chinook.db
con = make_con(db)
query = '''select * from Track where Name like '%rock%' and Composer!='NULL' order by Composer limit 5'''
df = get_query(query,con)
print("List of first 5 tracks with 'rock' in their titles, ordered by (non-null) Composer")
print(df)

