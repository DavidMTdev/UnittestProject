import re
import time

class Scrapper:
    def __init__(self, driver, url: str, sleep: int = 0):
        self.driver = driver
        self.driver.get(url)     
        self.driver.maximize_window()
        time.sleep(sleep)

    def click(self, xpath: str):
        element = self.findElement(xpath, 2)
        element.click()

    def send(self, xpath: str, key: str):
        element = self.findElement(xpath)
        element.send_keys(key)

    def findElement(self, xpath: str, sleep: int = 0):
        time.sleep(sleep)
        return self.driver.find_element_by_xpath(xpath)

    def findElements(self, xpath: str, sleep: int = 0):
        time.sleep(sleep)
        return self.driver.find_elements_by_xpath(xpath)

    def switchToFrame(self, xpath: str):
        self.driver.switch_to.frame(self.findElement(xpath))

    def switchToDefault(self):
        self.driver.switch_to.default_content()

class ScrapperArticle:
    @staticmethod
    def find(element, xpath: str, type = str, sleep: int = 0):
        time.sleep(sleep)

        result = element.find_element_by_xpath(xpath).text

        if type is int:
            result = int(re.match(r'-?\d+', result).group())
            
        if type is float:
            result = result.replace(',', '.')
            result = float(re.match(r'-?\d+\.?\d*', result).group())

        return result

