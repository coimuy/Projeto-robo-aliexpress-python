from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    x = 1
    vectorLinks = []
    vectorName = []
    vectorPrice = []
    browser = webdriver.Chrome(executable_path=r'./chromedriver')
    browser.get('https://best.aliexpress.com')
    browser.find_element(By.ID,'search-key').send_keys('redmi')
    browser.find_element(By.CLASS_NAME,'search-button').click()

    while x <= 10:
        print (x)
        linkProduct = browser.find_element(By.XPATH,
                                           "/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/a[{}]".format(
                                               x)).get_attribute('href')
        nameProduct = browser.find_element(By.XPATH,
                                           '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/a[{}]/div[2]/div[1]'.format(
                                               x)).text
        priceProduct = browser.find_element(By.XPATH,
                                            '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/a[{}]/div[2]/div[2]'.format(
                                               x)).text
        vectorLinks.append(linkProduct)
        vectorName.append(nameProduct)
        vectorPrice.append(priceProduct)
        x += 1
    
    
if __name__ == "__main__":
    main()