import ext
from ext.bot_enviar import BotEnviar
from func import EnviarMsg
from ext.bd_sqlite import Conexao
import time
import traceback
from config import except_erro

if __name__ == '__main__':
    driver_enviar = ext.webdriver.Chrome(options = ext.chrome_option_enviar)
    driver_enviar.get('https://web.whatsapp.com/')
    iniciar = BotEnviar(driver_enviar)
    enviar = EnviarMsg()
    enviar.iniciar_status("bot","update status set tp_stt = 1")
    while True:
        time.sleep(1)
        #driver_enviar.delete_all_cookies()
        #iniciar.lista_contatos()
        try:
            enviar_resposta = enviar.buscar_dados("SELECT id, telefone, msg_bot FROM historico WHERE enviado = 0", 'bot')
            disparar_msg = enviar.buscar_dados("SELECT id, telefone, msg from enviar_msg", 'bot')
            fechar = enviar.buscar_dados("select * from status where tp_stt = 0", 'bot')
            if fechar:
                import sys
                sys.exit()
            if enviar_resposta:
                enviar.disparo_msg(iniciar, enviar_resposta, "atualizar")
            if disparar_msg:
                enviar.disparo_msg(iniciar, disparar_msg, "delete")
        except Exception:
            except_erro(Exception)
