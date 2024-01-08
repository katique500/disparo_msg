from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
import json
from urllib.parse import unquote

dir_path = os.getcwd()
chrome_option = Options()
chrome_option.add_argument(r'user-data-dir='+ dir_path + 'profile/wpp')
chrome_option.add_argument("--headless=new")
chrome_option.add_argument('--log-level=0')

chrome_option_enviar = webdriver.ChromeOptions()
chrome_option_enviar.add_argument(r'user-data-dir='+ dir_path + 'profile/wpp_enviar')
#chrome_option_enviar.add_argument("--headless=new")