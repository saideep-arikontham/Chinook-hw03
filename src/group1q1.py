#!/usr/bin/env python
# coding: utf-8

# In[29]:


import sqlite3
from utils import *
import pandas as pd

db = 'data/chinook.db'  #data/chinook.db
con = make_con(db)
query1 = '''select InvoiceId, total from Invoice where total = (select max(total) from Invoice)'''
df = get_query(query1,con)
print(f'The maximum Invoice price is: {df.Total[0]}')
print(f"The Invoice id with maximum invoice price of {df.Total[0]} is {df.InvoiceId[0]}")

