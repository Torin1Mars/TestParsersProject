import logging

from playwright.sync_api import sync_playwright, Page

from App.data.Product import Product


class PlayWrightParser:

    def __init__(self):
        self.parsed_product:Product

        self.playWrightMngr = sync_playwright()

    def test (self, url: str):
        try:
            with sync_playwright() as mngr:
                browser = mngr.chromium.launch(headless=True)

                page = browser.new_page()
                respond  = page.goto(url)

                if respond.ok:
                    self._parse_product(page)
                else:
                    raise ValueError(f"{self.__class__.__name__} has loading error!")

                print(f"{self.__class__.__name__} has result: {self.parsed_product}")

        except Exception as e:
            logging.error(f"{self.__name__} has failed")

    def _parse_product(self, current_page:Page):
        #__________________________________________________________
        try:
            title = current_page.locator(".pdp-main-heading h1.pdp-main-title").inner_text().strip()
        except AttributeError:
            title= None

        #__________________________________________________________
        try:
            vendor = current_page.locator(".breadcrumbs-container .breadcrumbs-item").nth(-3).inner_text().strip().split(" ")[1].lower()
        except AttributeError:
            vendor = None

        #__________________________________________________________
        try:
            price = current_page.locator(".pdp-buy-main-price-wrap").nth(0).inner_text().strip()
        except AttributeError:
            price = None

        #__________________________________________________________
        try:
            productKey = int(current_page.locator(".pdp-menu-code").inner_text().strip().split(" ")[1])
        except AttributeError:
            productKey = None

        self.parsed_product = Product(title, vendor, price, productKey)
