#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sqlite3
from utils import *
import pandas as pd

db = 'data/chinook.db'  #data/chinook.db
con = make_con(db)
s = '''select BillingCountry, sum(Total) as Total_spent from Invoice group by BillingCountry'''
s1 = f'''select BillingCountry, Total_spent from ({s}) where Total_spent = (select max(Total_spent) from ({s}))'''
df = get_query(s1,con)
print("country that purchased the most music and how much it spent: ")
print(df)

