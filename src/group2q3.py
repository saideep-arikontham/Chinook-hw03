#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sqlite3
from utils import *
import pandas as pd

db = 'data/chinook.db'  #data/chinook.db
con = make_con(db)
s = '''select il.TrackId, il.UnitPrice from InvoiceLine il inner join Invoice i on il.InvoiceId = i.InvoiceId
        where i.BillingCountry = 'USA' '''
s1 = f'''select t.GenreId, s.UnitPrice from Track t inner join ({s}) s on t.TrackId=s.TrackId'''
s2 = f'''select g.Name, sum(s1.UnitPrice) sales from Genre g inner join ({s1}) s1 on s1.GenreId = g.GenreId 
    group by g.Name'''
s3 = f'''select Name,sales from ({s2}) where sales = (select max(sales) from ({s2}))'''

df = get_query(s3,con)
print("the most popular genre in the U.S. and its sales")
print(df)

