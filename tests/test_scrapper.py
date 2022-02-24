from unittest import TestCase
from selenium import webdriver

from scripts.scrapper import Scrapper, ScrapperArticle

class TestScrapper(TestCase):
    
    def setUp(self):
        # Chrome
        # self.scrapper = Scrapper(webdriver.Chrome(r'drivers/chromedriver'), 'https://ledenicheur.fr/')
        # scrapper.switchToFrame('//*[@id="sp_message_iframe_511014"]')
        # scrapper.click('//*[@id="notice"]/div[6]/button[2]')
        # scrapper.switchToDefault()

        # Edge 
        self.scrapper = Scrapper(webdriver.Edge(r'drivers/msedgedriver'), 'https://ledenicheur.fr/')
        self.scrapper.click('//*[@id="RejectButton-cookie-banner"]')

        # Search
        self.scrapper.send('//*[@id="root"]/div/header/div[1]/div[3]/div/div/span/form/input', 'carte graphiques')
        self.scrapper.click('//*[@id="root"]/div/header/div[2]/div[2]/div/ul/li[1]/button')

    def teardown(self):
        self.scrapper.driver.close()

    def test_findElements(self):
        elements = self.scrapper.findElements('//li[@data-test="ProductListRow"]', 5)
        self.assertIsInstance(elements, list)

    def test_findElement(self):
        self.element = self.scrapper.findElement('//li[@data-test="ProductListRow"][1]', 5)

        self.assertIsInstance(ScrapperArticle.find(self.element, 'a[2]/div[1]/div[@data-test="ProductName"]'), str)
        self.assertIsInstance(ScrapperArticle.find(self.element, 'a[3]/span[@data-test="PriceLabel"]', float), float)
        self.assertIsInstance(ScrapperArticle.find(self.element, 'a[4]/div'), str)
        self.assertIsInstance(ScrapperArticle.find(self.element, 'a[5]/div', int), int)
        self.assertIsInstance(ScrapperArticle.find(self.element, 'a[6]/div'), str)
