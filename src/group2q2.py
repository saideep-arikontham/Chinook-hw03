#!/usr/bin/env python
# coding: utf-8

# In[15]:


import sqlite3
from utils import *
import pandas as pd

db = 'data/chinook.db'  #data/chinook.db
con = make_con(db)
s1 = '''select t.GenreId, il.UnitPrice from Track t inner join InvoiceLine il on t.TrackId=il.TrackId'''
s2 = f'''select g.Name, sum(s1.UnitPrice) sales from Genre g inner join ({s1}) s1 on s1.GenreId = g.GenreId group by g.Name'''
s3 = f'''select Name,sales from ({s2}) where sales = (select max(sales) from ({s2}))'''

df = get_query(s3,con)
print("the most popular genre and sales it generated")
print(df)

