from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome(executable_path=r'./chromedriver')
navegador.get('https://best.aliexpress.com')
navegador.find_element(By.ID,'search-key').send_keys('redmi')
navegador.find_element(By.CLASS_NAME,'search-button').click()
while x < 10:
    x += 1
    print (x)
    #print(type(x))
    Link_produtos = navegador.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/a[{}]".format(x)).get_attribute('href')
    print(Link_produtos)
    Vetor_Links.append(Link_produtos)
#print (Vetor_Links)
