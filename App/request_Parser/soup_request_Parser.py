import logging

import requests
from bs4 import BeautifulSoup
from requests import Response
from App.data.Product import Product

class RequestParser:
    def __init__(self):
        self.parsed_product:Product

        self.request_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'Connection': 'keep-alive',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }

    def test (self, url: str):
        with requests.Session() as session:
            respond = session.get(url, headers=self.request_headers)

        if respond.ok:
            self._parse_product(respond)

            print(f"{self.__class__.__name__} has result: {self.parsed_product}")
        else:
            logging.error(f"{RequestParser.__name__} has failed")


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

        self.parsed_product = Product(title, vendor, price, productKey)
