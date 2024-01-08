import sqlite3

class Conexao:
    def __init__(self):
        self.conexao = sqlite3.Connection('enviar.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS enviar_msg(
                                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    telefone text,
                                    msg text,
                                    enviado int default 1
                                )
                            """)

    def buscar(self, query: str) -> tuple:
        self.cursor.execute(query)
        dados = self.cursor.fetchall()
        return dados

    def delete(self, id: int | str) -> None:
        sql = f"DELETE FROM enviar_msg WHERE id = {id}"
        self.cursor.execute(sql)