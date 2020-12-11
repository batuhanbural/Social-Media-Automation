import os
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys


class Whatsapp:
    def __init__(self):
        self.browser = webdriver.Edge("msedgedriver.exe")

    def login(self):
        print("Please scan the QR code.")
        sleep(2)
        self.browser.get("https://web.whatsapp.com/")

    def find_user(self, user_name: str):
        isSearched = 0
        while isSearched == 0:
            try:
                search_input = self.browser.find_element_by_xpath("""//*[@id="side"]/div[1]/div/label/div/div[2]""")
                search_input.send_keys(user_name)
                search_input.send_keys(Keys.ENTER)
                isSearched = 1
            except WebDriverException:
                continue

    def send_message(self, message: str):
        text_input = self.browser.find_element_by_xpath("""//*[@id="main"]/footer/div[1]/div[2]/div/div[2]""")
        text_input.send_keys(message)
        text_input.send_keys(Keys.ENTER)

    def spam_messages(self, target: str, spam: str, count: int):
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

    def spam_random_messages(self, target: str, spam_file: str):
        self.find_user(target)

        isReached = 0
        while isReached == 0:
            try:
                spam_file = open(r'{}'.format(spam_file), 'r', encoding="utf-8")
                Lines = spam_file.readlines()

                for line in Lines:
                    self.send_message(line.strip())
                isReached = 1
            except WebDriverException:
                continue

    def send_doc(self, file_path: str):
        isAttach = 0
        while isAttach == 0:
            try:
                attach_button = self.browser.find_element_by_xpath(
                    """//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div""")
                attach_button.click()

                image_box = self.browser.find_element_by_xpath(
                    """//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input""")
                image_box.send_keys(r"{}".format(file_path))

                isAttach = 1
            except WebDriverException:
                continue
        isSend = 0
        while isSend == 0:
            try:
                send_button = self.browser.find_element_by_xpath(
                    """//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div""")
                send_button.click()
                isSend = 1
            except WebDriverException:
                continue

    def send_docs(self, directory_path: str):
        files = ""
        try:
            files = os.listdir(r"{}".format(directory_path))
        except FileNotFoundError:
            print("Please enter a valid path!")

        for file in files:
            self.send_doc(directory_path + "/" + file)
            sleep(2)

    def online_tracker(self, target: str):  # Beta
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