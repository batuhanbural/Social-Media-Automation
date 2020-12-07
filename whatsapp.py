from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from time import sleep


class Whatsapp:
    def __init__(self):
        self.browser = webdriver.Edge("msedgedriver.exe")

    def login(self):
        print("Please scan the QR code.")
        sleep(2)
        self.browser.get("https://web.whatsapp.com/")
        # sleep(3)
        # input("Press any key for continue...")

    def spam_messages(self, target, spam, count):
        isLoggedIn = 0
        while isLoggedIn == 0:
            try:
                search_input = self.browser.find_element_by_xpath("""//*[@id="side"]/div[1]/div/label/div/div[2]""")
                search_input.send_keys(target)
                search_input.send_keys(Keys.ENTER)

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
        pass

# x = Whatsapp()
#
# x.login()
# x.spam_messages("Kendim", "a", 5)