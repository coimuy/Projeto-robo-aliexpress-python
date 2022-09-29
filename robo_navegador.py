from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    x = 1
    vectorLinks = []
    browser = webdriver.Chrome(executable_path=r'./chromedriver')
    browser.get('https://best.aliexpress.com')
    browser.find_element(By.ID,'search-key').send_keys('redmi')
    browser.find_element(By.CLASS_NAME,'search-button').click()

    while x <= 10:
        x += 1
        print (x)
        linkProduct = browser.find_element(By.XPATH,
                                           "/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/a[{}]".format(
                                               x)).get_attribute('href')
        print(linkProduct)
        vectorLinks.append(linkProduct)


if __name__ == "__main__":
    main()