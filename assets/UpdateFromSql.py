import pandas as pd
import os
import json
import sqlalchemy
import psycopg2
import sys

from pandas.io.json import json_normalize
from numpy import array
from sqlalchemy import create_engine, true
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
    col = str(list_col)
    col_paramns = col.replace(" ", "_").replace("'", "").replace(",_", " text, ").replace("[", "").replace("]", " text").replace("ANS text", "ANS integer").replace("CNPJ text", "CNPJ integer unique not null").replace(
        "ANS integer, CNPJ", "ANS integer primary key, CNPJ").replace("Número text", "Numero integer").replace("CEP text", "CEP integer").replace("DDD text", "DDD integer").replace("Telefone text", "Telefone integer").replace("Fax text", "Fax integer").replace("Endereço_eletrônico", "Email")

    value_paramns = str(record_list.head(3))
    print(value_paramns)


def create_table(json_data):
    try:
        conn = psycopg2.connect(DATABASE_URL)
    except(Exception, psycopg2.Error) as error:
        print("Connection not established", error)

    cur = conn.cursor()
    print("connect")

    cur.execute(
        "SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='relatorio')")
    table_exist = cur.fetchone()[0]
    print(table_exist)

    if bool(table_exist):
        cur.execute("CREATE TABLE IF NOT EXISTS relatorio (" +
                    col_paramns + ")")
        conn.commit()
        print("create")
        conn.close()
        print("Done")
    else:
        conn.close()
        print('Relatorio table exists. Moving On.')


# create_table(col_paramns)

def insert_into_table(json_data):
    try:
        conn = psycopg2.connect(DATABASE_URL)
    except(Exception, psycopg2.Error) as error:
        print("Connection not established", error)

    cur = conn.cursor()
    print("connect")

    query = "INSERT INTO relatorio VALUES (%s)"
    cur.executemany(query, value_paramns)
    conn.commit()
    print("commit")
    conn.close()
    print("close")


insert_into_table(value_paramns)
