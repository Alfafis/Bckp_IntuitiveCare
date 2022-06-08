import pandas as pd
import os
import json
import sqlalchemy
import psycopg2
import sys

from pandas.io.json import json_normalize
from numpy import array
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

PGUSER = os.getenv("PGUSER")
PGPORT = os.getenv("PGPORT")
PGPASSWORD = os.getenv("PGPASSWORD")
PGHOST = os.getenv("PGHOST")
PGDATABASE = os.getenv("PGDATABASE")
DATABASE_URL = "postgresql://" + PGUSER + ":" + PGPASSWORD + \
    "@" + PGHOST + ":" + PGPORT + "/" + PGDATABASE

record_list = pd.read_csv('assets/Relatorio_cadop.csv', sep=',')

record_list.to_json(r'assets/Relatorio_cadop.json')

with open('assets/Relatorio_cadop.json', 'w', encoding='utf-8') as file:
    record_list.to_json(file, force_ascii=False)
    list_col = list(record_list.columns)
    col = array(list_col)
    print("teste -> ", col)

# def create_table(json_data):
#     try:
#         with psycopg2.connect(DATABASE_URL) as conn:
#             cur = conn.cursor()
#             print("connect")
#             cur.execute("CREATE TABLE IF NOT EXISTS Relatorio " +
#                         (str(list_col)))
#             print("create")
#             conn.commit()
#             conn.close()
#             print("Done")
#     except(Exception, psycopg2.Error) as error:
#         print("Failed json import: {}".format(error))


# create_table(col)

# engine = create_engine("postgresql+psycopg2://thisuser:"+DATABASE_URL)
# col.to_sql("new_table", engine, index=False, if_exists='append')
# print("Done").str.split(pat="\n", expand=True)


# def insert_into_table(json_data):
#     try:
#         with psycopg2.connect(DATABASE_URL) as conn:
#             cur = conn.cursor()
#             lines_json_all = data_base.readlines()
#             query = "INSERT INTO new_table VALUES (%s)"
#             cur.executemany(query, (lines_json_all))
#             conn.commit()
#             conn.close()
#     except(Exception, psycopg2.Error) as error:
#         print("Failed json import: {}".format(error))


# insert_into_table(data_base)

# create_table()

# df = pd.json_normalize(data_base)
