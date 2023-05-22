import sqlite3
import pandas as pd

df = pd.read_csv('data/задача 1/Задача3_Книги.csv', encoding = '1251',sep=';')
df.columns = df.columns.str.strip()
connection = sqlite3.connect('test.db')
df.to_sql('Книги',connection,if_exists='replace')
connection.close()
