import pandas as pd
import json
import os
import sqlalchemy
import psycopg2

from pandas.io.json import json_normalize
from sqlalchemy import create_engine
# from os import environ as env

print(os.environ)
with open("./.env") as env:
   uri  = env.read()
   # print(uri)


# with open('assets/Relatorio_cadop.json') as data_file:    
#     d = json.load(data_file)

# uri = os.environ["PGUSER"]
# print(uri)

# def create_table():
#    conn=psycopg2.connect(os.environ['DATABASE_URL']) 
#    cur=conn.cursor() 
#    cur.execute("CREATE TABLE IF NOT EXISTS new_table (color TEXT, fruit TEXT, size TEXT)")  
#    conn.commit() 
#    conn.close() 

# create_table()

# df = json_normalize(d)

# engine = create_engine("postgresql+psycopg2://thisuser:"+os.environ['DATABASE_URL'])
# df.to_sql("new_table", engine, index=False, if_exists='append')
# print("Done")