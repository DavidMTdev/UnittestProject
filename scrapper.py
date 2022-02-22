import re
import time

import requests
from selenium import webdriver

# from app.models.article import Article 

class Scrapper:
    
    def __init__(self, url: str):
        self.driver = webdriver.Chrome(r'drivers/chromedriver')
        self.driver.get(url)     

    def click(self, xpath: str):
        element = self.driver.find_element_by_xpath(xpath)
        element.click()

    def send(self, xpath: str, key: str):
        element = self.driver.find_element_by_xpath(xpath)
        element.send_keys(key)

    def switchToFrame(self, xpath: str):
        self.browser.switch_to.frame(browser.find_element_by_xpath(xpath))

    def switchToDefault(self):
        self.browser.switch_to.default_content()
        

class ScrapperArticle(Scrapper):

    def __init__(self):
        super.__init__('https://ledenicheur.fr/')
    

browser = webdriver.Chrome(r'drivers/chromedriver')
# browser.get('https://ledenicheur.fr/')
# browser.maximize_window()

time.sleep(5)

browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="sp_message_iframe_511014"]'))

cookies = browser.find_element_by_xpath('//*[@id="notice"]/div[6]/button[2]')
cookies.click()

browser.switch_to.default_content()

time.sleep(2)

search = browser.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div[3]/div/div/span/form/input')
search.send_keys('carte graphiques')

time.sleep(2)

search = browser.find_element_by_xpath('//*[@id="root"]/div/header/div[2]/div[2]/div/ul/li[1]/button')
search.click()

articles = []

for i in range(0, 1):
    time.sleep(5)

    elements = browser.find_elements_by_xpath('//li[@data-test="ProductListRow"]')
    for element in elements:
        name = element.find_element_by_xpath('a[2]/div[1]/div[@data-test="ProductName"]').text
        price = element.find_element_by_xpath('a[3]/span[@data-test="PriceLabel"]').text
        type = element.find_element_by_xpath('a[4]/div').text
        memoryCapacity = element.find_element_by_xpath('a[5]/div').text
        memoryType = element.find_element_by_xpath('a[6]/div').text

        price = price.replace(',', '.')
        price = float(re.match(r'-?\d+\.?\d*', price).group())
        memoryCapacity = int(re.match(r'-?\d+', memoryCapacity).group())
       
        data = {'name': name, 'price': price, 'type': type, 'memoryCapacity': memoryCapacity, 'memoryType': memoryType}
        # articles.append(Article(name, price, type, memoryCapacity, memoryType))
        req = requests.post('http://127.0.0.1:8000/articles', json=data)
        print(req.status_code, req.content)
        articles.append(data)

    time.sleep(2)

    nextPage = browser.find_element_by_xpath('//a[@data-test="PaginationButtonNext"]')
    nextPage.click()

browser.close()

# db.article.drop()
# db.article.insert_many([item.__dict__ for item in articles])
