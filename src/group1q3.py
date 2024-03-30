#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
from utils import *
import pandas as pd

db = 'data/chinook.db'  #data/chinook.db
con = make_con(db)
sub_query_Invoice = '''(select InvoiceId from Invoice where total = (select max(total) from Invoice))'''
query = f'''select t.Name from InvoiceLine il inner join Track t on t.TrackId = il.TrackId 
where il.InvoiceId={sub_query_Invoice} order by t.Name'''
df = get_query(query,con)
print("List of song titles from the most expensive invoice in alphabetical order:")
print(df)

