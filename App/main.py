
from App.requests.soup_request_Parser import RequestParser
from App.playwright.playWright_Parser import PlayWrightParser
from App.selenium.selenium_Parser import SeleniumParser

if __name__ == "__main__":
    #Creating parsers
    requestsParser = RequestParser()

    playWrightParser = PlayWrightParser()

    selenium = SeleniumParser()

    #Runinig
    try :
        requestsParser.test("https://tehnotop.ua/ru/smartfon-samsung-a17-sm-a175f-8-256gb-gray-23331")
    except Exception as e:
        print(f"Request Parser has failed.")
        print(e)

    try :
        playWrightParser.test()
    except Exception as e:
        print(f"Play Wright Parser has failed.")
        print(e)

    try :
        selenium.test("https://www.moyo.ua/ua/smartfon_samsung_galaxy_s25_12_512gb_navy_sm-s931bdbheuc_/628572.html")
    except Exception as e:
        print(f"Selenium Parser has failed.")
        print(e)
