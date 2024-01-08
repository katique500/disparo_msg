import logging

# CONFIGURACAO DO LOG
logging.basicConfig(filename='error.log', level=logging.ERROR, format=f'%(asctime)s - %(levelname)s - %(message)s')

def except_erro(e):
    linha_erro = logging.error(f"Ocorreu um erro NO ARQUIVO {__name__.upper()} LINHA DO ERRO: {e.__traceback__.tb_lineno}, MOTIVO: {str(e)}")
    return linha_erro
