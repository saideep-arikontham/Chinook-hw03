import pandas as pd
import sqlite3

# See: https://pandas.pydata.org/docs/user_guide/options.html
pd.set_option('display.max_columns', None)

def printit(query, con):
    print(query)
    cur = con.cursor()
    cur.execute(query)
    print(cur.fetchall())

def pretty(query, con):
    print(query)
    df = pd.read_sql(query, con)
    print(df)
    return df

def get_query(query, con):
    df = pd.read_sql(query, con)
    return df

def make_con(db):
    con = sqlite3.connect(db)
    return con
