import requests
from selenium import webdriver

from scripts.scrapper import Scrapper, ScrapperArticle

def runScrapper(scrapper):
    scrapper.send('//*[@id="root"]/div/header/div[1]/div[3]/div/div/span/form/input', 'carte graphiques')
    scrapper.click('//*[@id="root"]/div/header/div[2]/div[2]/div/ul/li[1]/button')

    elements = scrapper.findElements('//li[@data-test="ProductListRow"]', 5)
    for element in elements:

        data = {
            'name': ScrapperArticle.find(element, 'a[2]/div[1]/div[@data-test="ProductName"]'),
            'price': ScrapperArticle.find(element, 'a[3]/span[@data-test="PriceLabel"]', float),
            'type': ScrapperArticle.find(element, 'a[4]/div'),
            'memoryCapacity': ScrapperArticle.find(element, 'a[5]/div', int),
            'memoryType': ScrapperArticle.find(element, 'a[6]/div')
        }

        req = requests.post('http://127.0.0.1:8000/articles', json=data)
        print(req)

def init_ChromeDriver():
    scrapper = Scrapper(webdriver.Chrome(r'drivers/chromedriver'), 'https://ledenicheur.fr/')
    scrapper.switchToFrame('//*[@id="sp_message_iframe_511014"]')
    scrapper.click('//*[@id="notice"]/div[6]/button[2]')
    scrapper.switchToDefault()

    return scrapper

def init_EdgeDriver():
    scrapper = Scrapper(webdriver.Edge(r'drivers/msedgedriver'), 'https://ledenicheur.fr/')
    scrapper.click('//*[@id="RejectButton-cookie-banner"]')

    return scrapper 

def run():
    # Décommenter pour utilise le Chrome Driver et commenter scrapper = init_EdgeDriver()
    # scrapper = init_ChromeDriver()
    scrapper = init_EdgeDriver()
    runScrapper(scrapper)
    scrapper.driver.close()