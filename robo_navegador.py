from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class tabelas:
    price = 0.0
    priceIsValid = False


def main():
    x = 1
    vector = []
    scroll = 1080

    browser = webdriver.Chrome(executable_path=r'./chromedriver')
    browser.get('https://best.aliexpress.com')
    browser.fullscreen_window()
    
    browser.find_element(By.ID,'search-key').send_keys('redmi')
    browser.find_element(By.CLASS_NAME,'search-button').click()

    while scroll <= 5400:
        print (scroll)
        browser.execute_script('window.scrollTo(0, {});'.format(scroll))
        time.sleep(1)
        scroll += 1080
    
    driver = BeautifulSoup(browser.page_source,'html.parser')
    elements = driver.find('div', attrs={'class': 'JIIxO'}).findAll('a', attrs={'class': '_3t7zg _2f4Ho'})

    for element in elements: 
        print(x)

        price = ''

        linkProduct = browser.find_element(By.XPATH,
                                    "/html/body/div[4]/div/div/div[2]/div[2]/div/div[2]/a[{}]".format(
                                            x)).get_attribute('href')

        nameProduct = browser.find_element(By.XPATH,
                                           '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/a[{}]/div[2]/div[1]'.format(
                                               x)).text

        if len(nameProduct) == 0:
            nameProduct = browser.find_element(By.XPATH,
                                           '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/a[{}]/div[2]/div[2]'.format(
                                               x)).text

        priceProduct = browser.find_element(By.XPATH,
                                            '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/a[{}]/div[2]/div[2]'.format(
                                              x)).text

        if len(priceProduct) > 13 or len(priceProduct) == 0:
            priceProduct = browser.find_element(By.XPATH,
                                            '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/a[{}]/div[2]/div[3]'.format(
                                               x)).text

        if len(priceProduct) > 3:
            tabelas.price = float(priceProduct.replace('R$', '').replace('.', '').replace(',', '.'))
            tabelas.priceIsValid = True

        x += 1
        vector.append(linkProduct)
        vector.append(nameProduct)
        vector.append(tabelas.price)

    print(vector)   
 
    
if __name__ == "__main__":
    main()