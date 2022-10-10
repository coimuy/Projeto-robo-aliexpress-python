import database, smtplib, email.message
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

class Product:
    name = ''
    price = 0.0
    url = ''

sendName = 'Redmi'
link = 'https://best.aliexpress.com/?lan=en&gatewayAdapt=glo2bra'

def search(driver, item):
    driver.find_element('xpath', '//*[@id="search-key"]').send_keys(item)
    driver.find_element('xpath', '//*[@id="form-searchbar"]/div[1]/input').click()

    for roll in range(6):
        driver.execute_script(f'window.scrollTo(0, {roll * 1080});')
        time.sleep(1)


def getItensInPage(driver):
    page = BeautifulSoup(driver.page_source, 'html.parser')
    listProducts = []
    time.sleep(1.5)

    elements = page.find('div', attrs={'class': 'JIIxO'}).find_all('a', attrs={'class': '_3t7zg _2f4Ho'})

    for element in elements:
        spans = element.find('div', attrs={'class': 'mGXnE _37W_B'}).find_all('span')
        price = ''

        for span in spans:
            price = price + span.getText()

        product = Product()
        product.name = element.find('h1').getText()
        product.url = element.attrs['href'].replace('//', 'https://')

        if len(price) > 3:
            product.price = float(price.replace('R$', '').replace('.', '').replace(',', '.'))

        listProducts.append(product)

    return listProducts


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    search(driver, sendName)
    listProducts = getItensInPage(driver)
    database.insert_products(listProducts)
    select_list = database.execute_query_select('SELECT name, price, url from public.products  order by price limit 5')
    print(select_list)
    
    text_email = """<p>Resultado da pesquisa sobres o produto {}:</p
                <p> estes são o top 5 produtos mais baratos.</p>
                <p>{}</p>""".format(sendName, listProducts)
    msg = email.message.Message()
    msg['Subject'] = "Top 4 produtos mais baratos {}".format(sendName)
    msg['From'] = 'matheussena311@gmail.com'
    msg['To'] = 'braullio.goncalves@easyc.com.br '
    password = 'tofhubblvebqqmkc' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(text_email)

    send = smtplib.SMTP('smtp.gmail.com: 587')
    send.starttls()
    send.login(msg['From'], password)
    send.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


if __name__ == "__main__":
    main()