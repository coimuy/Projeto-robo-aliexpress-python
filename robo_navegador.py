import json
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import psycopg2

# TODO: Criar metodo para consulta ao banco de dados
# def execute_query_select(query):


class Product:
    name = ''
    price = 0.0
    url = ''


def search(browser, item):
    browser.find_element('xpath', '//*[@id="search-key"]').send_keys(item)
    browser.find_element('xpath', '//*[@id="form-searchbar"]/div[1]/input').click()
    

    for roll in range(6):
        browser.execute_script('window.scrollTo(0, {});'.format(roll*1080))
        time.sleep(1)
    

def getItensInPage(driver):
    x = 1
    page = BeautifulSoup(driver.page_source, 'html.parser')
    listProducts = []
    elements = page.find('div', attrs={'class': 'JIIxO'}).find_all('a', attrs={'class': '_3t7zg _2f4Ho'})

    for element in elements:
        spans = element.find('div', attrs={'class': 'mGXnE _37W_B'}).find_all('span')
        price = ''

        for span in spans:
            price = price + span.getText()

        product = Product()
        product.name = element.find('h1').getText()

        product.url = driver.find_element(By.XPATH,
                                    "/html/body/div[4]/div/div/div[2]/div[2]/div/div[2]/a[{}]".format(
                                            x)).get_attribute('href')
                                
        if len(price) > 3:
            product.price = float(price.replace('R$', '').replace('.', '').replace(',', '.'))
        x += 1

        listProducts.append([product.url, product.name, product.price])

    return listProducts
    
    
def main():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get('https://pt.aliexpress.com/?spm=a2g0o.productlist.1000002.1.3cc16dbfvgZy5D&gatewayAdapt=glo2bra')
    search(driver, 'redmi')
    listProducts = getItensInPage(driver)
    print(listProducts[0])
    # TODO: Criar metodo para insersão de todos elementos da lista listProducts
    #query = "INSERT INTO public.products ( name, price, url) VALUES ('redmi', 10.2, 'http://hjkhsadj]')"
    #execute_query_insert(query)
    # TODO: Efetuar o filtro dos 5 mais baratos
    # TODO: Criar um metodo para envio de email ( para braullio.goncalves@easyc.com.br ) com o raking dos 5


if __name__ == "__main__":
    main()