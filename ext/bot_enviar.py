import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, \
                TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BotEnviar:
    """
        ESTA CLASS BOT ENVIAR SERVE PARA DISPARO DE MENSAGEM
        E ENVIO DE MSG
    """
    def __init__(self, driver):
        self.driver= driver
        self.nova_conversa = ActionChains(self.driver).key_down(Keys.CONTROL)\
                                    .key_down(Keys.ALT)\
                                    .key_down(Keys.SHIFT)\
                                    .send_keys("N")\
                                    .key_up(Keys.CONTROL)\
                                    .key_up(Keys.ALT)\
                                    .key_up(Keys.SHIFT)
        self.input_contato = 'to2l77zo'
        self.caixa_msg = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        #'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]'

    def enviar_msg(self, resposta : str , esc : bool = True) -> None:
        self.driver.implicitly_wait(20)
        campo_texto = self.driver.find_element(By.XPATH, self.caixa_msg)
        campo_texto.click()
        campo_texto.send_keys(resposta, Keys.ENTER, Keys.ENTER)
        if esc:
            time.sleep(1)
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def abrir_nova_aba(self, contato, msg):
        self.driver.implicitly_wait(20)
        try:
            self.driver.execute_script(f"window.open('https://web.whatsapp.com/send?phone=+55{contato}');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            self.enviar_msg(msg)
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        finally:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/button[2]/div/div').click()

    def achado(self, msg):
        self.enviar_msg(msg)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def mandar_msg(self, contato: str | list, msg: str) -> None:
        if isinstance(contato, str):
            self.driver.implicitly_wait(5)
            self.nova_conversa.perform()
            campo_contato = self.driver.find_element(By.CLASS_NAME, self.input_contato)
            campo_contato.clear()
            campo_contato.send_keys(contato, Keys.ENTER)
            start = time.time()
            class_teste = ['VfC3c', '_11JPr', 'f8jlpxt4']  # _11JPr f8jlpxt4 _21S-L
            erros = [NoSuchElementException,TimeoutException, StaleElementReferenceException]
            for elemento in class_teste:
                try:
                    self.driver.implicitly_wait(2)
                    WebDriverWait(self.driver, 1, poll_frequency= 0.1, ignored_exceptions=erros).until(
                        EC.presence_of_element_located((By.CLASS_NAME, elemento))
                    )
                    if elemento == class_teste[0]:
                        self.achado(msg)
                        return None
                    else:
                        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                        self.abrir_nova_aba(contato, msg)
                        end = time.time()

                except Exception:
                    ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                    self.abrir_nova_aba(contato, msg)
                    return None

        for cont in contato:
            self.nova_conversa.perform()
            campo_contato = self.driver.find_element(By.CLASS_NAME, self.input_contato)
            campo_contato.send_keys(cont, Keys.ENTER)
            self.enviar_msg(msg)
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        return None

    def qr_code(self):
        self.driver.implictly_wait(5)
        try:
            self.driver.find_elements(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas')
            return True
        except:
            return False
