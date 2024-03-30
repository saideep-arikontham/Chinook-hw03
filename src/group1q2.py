#!/usr/bin/env python
# coding: utf-8

# In[11]:


import sqlite3
from utils import *
import pandas as pd

db = 'data/chinook.db'  #data/chinook.db - this is required
con = make_con(db)
sub_query_Invoice = '''(select InvoiceId from Invoice where total = (select max(total) from Invoice))'''
query = '''select t.TrackId, t.UnitPrice from InvoiceLine il inner join Track t on t.TrackId = il.TrackId where il.InvoiceId='''+sub_query_Invoice
#query1 = '''select TrackId from InvoiceLine where InvoiceId = 404''' --cross check with this query.
df = get_query(query,con)
print("list of the tracks (id and price) on the most expensive invoice: ")
print(df)

