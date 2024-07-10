from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
#Para o selenium usar o teclado
from selenium.webdriver.common.keys import Keys
#Esperar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)

browser.get('https://www.amazon.com.br/?&tag=hydrbrabk-20&ref=pd_sl_7rwd1q78df_e&adgrpid=155790195778&hvpone=&hvptwo=&hvadid=677606588104&hvpos=&hvnetw=g&hvrand=11779293125743238176&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001625&hvtargid=kwd-10573980&hydadcr=26346_11691057&gad_source=1')

lista = ['rico','batata','bone','celular','headphone','motorola','capacete','Caneca Para Chopp Mass Krug','banana']

for i in lista:
    #Indo na aba de busca
    browser.find_element(By.ID,'twotabsearchtextbox').clear()
    browser.find_element(By.ID,'twotabsearchtextbox').send_keys('batata',Keys.ENTER)
    #Clicando na imagem 
    # WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'a-section a-spacing-base')))
    sleep(2)
    
    browser.find_element(By.CLASS_NAME,'s-product-image-container').click()
    sleep(2)
    browser.save_screenshot(f'batata.png')
    