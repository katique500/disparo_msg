import mysql.connector
import time
from ext.bd_sqlite import Conexao


class EnviarMsg:

    def __conexao(self, db) -> mysql.connector.connect:
        try:
            con = mysql.connector.connect(host="localhost", user="enviar", passwd="enviar", database=db)
            cursor = con.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS ENVIAR_MSG(
                                    id integer not null primary key AUTO_INCREMENT,
                                    telefone varchar(255),
                                    msg varchar(255),
                                    enviado int default 1);
                           """)
            cursor.execute("""CREATE TABLE IF NOT EXISTS STATUS(
                                    tp_stt int default 1
                                );""")
            con.commit()
            cursor.close()
            return con
        except Exception as e:
            print("Conexao err:", str(e))
            print('tentando novamente..')
            time.sleep(5)
            self.conexao()

    def executar_query(self, db: str ='bot', query: str = None, buscar: bool = False) -> tuple:
        conexao = self.__conexao(db)
        cursor = conexao.cursor()
        try:
            cursor.execute(query)
            if buscar:
                dados = cursor.fetchall()
                return dados
            conexao.commit()
        except Exception as e:
            print("Deu erro. erro:", str(e))
            conexao.rollback()
        finally:
            cursor.close()
            conexao.close()

    def iniciar_status(self, db, sql) -> None:
        self.executar_query(db, sql)        
        return None

    def buscar_dados(self, sql, db) -> tuple:
        dados = self.executar_query(db, sql, True)
        return dados

    def action(self, acao, id):
        match acao:
            case "atualizar":
                sql = f"UPDATE historico SET enviado = 1 WHERE id = {id}"
                self.executar_query('bot', sql)

            case "delete":
                sql = f"DELETE FROM enviar_msg WHERE id = {id}"
                self.executar_query('bot', sql)
                
            case "bd_sqlite_delete":
                Conexao.delete(id)
                
            case _:
                print("Action nao existe, escolha entre delete ou atualizar.")

    def disparo_msg(self, driver, lista : list, acao : str) -> None:
        if lista:
            for id, numero, msg in lista:
                status = self.buscar_dados("select * from status","bot")
                if status[0][0] == 1:
                    driver.mandar_msg(numero, msg)
                    self.action(acao, id)

                elif status[0][0] == 0:
                    import sys
                    sys.exit()

                break