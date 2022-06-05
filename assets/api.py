import pandas as pd
import json
import html

df = pd.read_csv ('Relatorio_cadop.csv', sep=',')

df.to_json (r'Relatorio_cadop.json')

with open('Relatorio_cadop.json', 'w', encoding='utf-8') as file:
    df.to_json(file, force_ascii=False)

col = list(df.columns)

print(col)
