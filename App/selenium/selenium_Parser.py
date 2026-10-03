import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from App.data.Product import Product

class SeleniumParser:

    def __init__(self):
        self.parsed_product:Product

        self.driver_options = Options()
        self.driver_options.add_argument("--headless=new")
        self.driver_options.add_argument("--width=1920")
        self.driver_options.add_argument("--height=1080")

        self.driver = webdriver.Chrome(options=self.driver_options)

    def test (self, url: str):
        try:
            #TODO Continue to work here:
            self.driver.get(url = url)


        except Exception as e:
            logging.error(f"{self.__name__} has failed")

    '''       
    def _parse_product(self, respond:Response):
        data = BeautifulSoup(respond.text, "html.parser")

        #__________________________________________________________
        try:
            title = data.find("h1", class_ = "h1-prod-name").get_text().strip()
        except AttributeError:
            title= None

        #__________________________________________________________
        try:
            vendor = data.find(class_ = "breadcrumb").select("li")[-2].get_text().strip()
        except AttributeError:
            vendor = None

        #__________________________________________________________
        try:
            price = data.find(class_ = "price").get_text().strip()
        except AttributeError:
            price = None

        #__________________________________________________________
        try:
            productKey = int(data.select_one('[class*="prod-code"]').get_text().split(": ")[1])
        except AttributeError:
            productKey = None

        self.parsed_product = Product(title, vendor, price, productKey)'''
