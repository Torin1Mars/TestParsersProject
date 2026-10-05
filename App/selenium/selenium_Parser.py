import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from App.data.Product import Product

class SeleniumParser:

    def __init__(self):
        self.parsed_product:Product

        self.renderTimeout = 2

        self.driver_options = Options()
        self.driver_options.add_argument("--headless=new")
        self.driver_options.add_argument("--width=1920")
        self.driver_options.add_argument("--height=1080")

        self.driver = webdriver.Chrome(options=self.driver_options)

    def test (self, url: str):
        try:
            self.driver.get(url = url)
            WebDriverWait(self.driver, timeout=self.renderTimeout)

            self._parse_product(self.driver)

            print(f"{self.__class__.__name__} has result: {self.parsed_product}")

        except Exception as e:
            logging.error(f"{self.__name__} has failed")


    def _parse_product(self, driver_with_page:webdriver.Chrome):

        #__________________________________________________________
        try:
            title = driver_with_page.find_element(By.CSS_SELECTOR, "h1.product_name").text.strip()
        except AttributeError:
            title= None

        #__________________________________________________________
        try:
            vendor = driver_with_page.find_element(By.CSS_SELECTOR, "ol.breadcrumbs li:nth-child(3) span[itemprop='name']").text.strip().lower()
        except AttributeError:
            vendor = None

        #__________________________________________________________
        try:
            price = driver_with_page.find_element(By.CSS_SELECTOR, "div.product_price-block > :first-child > span").text.strip()
        except AttributeError:
            price = None

        #__________________________________________________________
        try:
            productKey = int(driver_with_page.find_element(By.CSS_SELECTOR, "div.product_id span:first-child").get_attribute("textContent").strip())
        except AttributeError:
            productKey = None

        self.parsed_product = Product(title, vendor, price, productKey)
