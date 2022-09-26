from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome(executable_path=r'./chromedriver')
navegador.get('https://best.aliexpress.com')
navegador.find_element(By.ID,'search-key').send_keys('redmi')
navegador.find_element(By.CLASS_NAME,'search-button').click()
navegador.find_element(By.TAG_NAME,'a')


