import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS estoque(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               codigo INTEGER NOT NULL,
               quantidade INTEGER NOT NULL
               )
               """)
conexao.commit()