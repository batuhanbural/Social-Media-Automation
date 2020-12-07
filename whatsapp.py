from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep


class Whatsapp:
    def __init__(self):
        self.browser = webdriver.Edge("msedgedriver.exe")

    def login(self):
        print("Please scan the QR code.")
        sleep(2)
        self.browser.get("https://web.whatsapp.com/")

    def find_user(self, user_name):
        isSearched = 0
        while isSearched == 0:
            try:
                search_input = self.browser.find_element_by_xpath("""//*[@id="side"]/div[1]/div/label/div/div[2]""")
                search_input.send_keys(user_name)
                search_input.send_keys(Keys.ENTER)
                isSearched = 1
            except WebDriverException:
                continue

    def spam_messages(self, target, spam, count):
        isLoggedIn = 0
        while isLoggedIn == 0:
            try:
                self.find_user(target)

                text_input = self.browser.find_element_by_xpath("""//*[@id="main"]/footer/div[1]/div[2]/div/div[2]""")
                start_count = 0
                while start_count < count:
                    text_input.send_keys(spam)
                    text_input.send_keys(Keys.ENTER)
                    start_count += 1
                text_input.send_keys("Sended via Python")
                text_input.send_keys(Keys.ENTER)
                start_count += 1
                isLoggedIn = 1
            except WebDriverException:
                continue

    def online_tracker(self, target):
        self.login()
        self.find_user(target)
        while True:
            try:
                isOnline = self.browser.find_element_by_xpath("""//*[@id="main"]/header/div[2]/div[2]/span""")
                if isOnline.text == "online":
                    print("Kullanıcı Online")
            except NoSuchElementException:
                print("Kullanıcı Offline")
            except StaleElementReferenceException:
                print("Kullanıcı Offline")

# x = Whatsapp()
#
# x.login()
# x.spam_messages("Kendim", "a", 5)