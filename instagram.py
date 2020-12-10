from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Edge("msedgedriver.exe")
        self.username = username
        self.password = password

    def get_main_page(self):
        self.browser.get("https://www.instagram.com/?hl=tr")

    def login(self):
        self.get_main_page()
        isLoggedIn = 0

        while isLoggedIn == 0:
            try:
                user_name_input = self.browser.find_element_by_xpath("""//*[@id="loginForm"]/div/div[
                1]/div/label/input""")
                user_name_input.send_keys(self.username)

                password_input = self.browser.find_element_by_xpath("""//*[@id="loginForm"]/div/div[
                2]/div/label/input""")
                password_input.send_keys(self.password)
                password_input.send_keys(Keys.ENTER)
                isLoggedIn = 1
            except WebDriverException:
                continue

    def send_message(self, message):
        isConnected = 0
        while isConnected == 0:
            try:
                text_box = self.browser.find_element_by_xpath("""//*[@id="react-root"]/section/div/div[
                                2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea""")
                text_box.send_keys(message)
                text_box.send_keys(Keys.ENTER)
                isConnected = 1
            except WebDriverException:
                continue

    def reply_message(self, targets: list):
        isDmBox = 0
        isMessageBox = 0

        while isDmBox == 0:
            try:
                dm_box = self.browser.find_element_by_xpath(
                    """//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]""")
                dm_box.click()
                isDmBox = 1
            except WebDriverException:
                continue

        while isMessageBox == 0:
            try:
                message_button = self.browser.find_element_by_xpath("""//*[@id="react-root"]/section/div/div[
                2]/div/div/div[ 2]/div/button""")
                message_button.click()
                isMessageBox = 1
            except WebDriverException:
                notifications = self.browser.find_element_by_xpath("""/html/body/div[5]/div/div/div/div[3]/button[2]""")
                notifications.click()
            finally:
                continue

        for target in targets:
            try:
                find_user = self.browser.find_element_by_xpath("""/html/body/div[5]/div/div/div[2]/div[1]/div/div[
                2]/input""")
                for i in range(len(target)):
                    find_user.send_keys(Keys.BACK_SPACE)
                find_user.send_keys(target)
                find_user.send_keys(Keys.ENTER)

                # get element  after explicitly waiting for 10 seconds
                element = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.RnEpo.Yx5HN > div > div > "
                                                                     "div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > "
                                                                     "div.Igw0E.IwRSH.eGOV_.vwCYk._3wFWr > div > div > "
                                                                     "div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > "
                                                                     "button > span")))
                element.click()

            except WebDriverException:
                pass

        next_button = self.browser.find_element_by_xpath("""/html/body/div[5]/div/div/div[1]/div/div[2]/div""")
        next_button.click()

    def unfollow_all(self):
        isClicked = 0
        isReached = 0
        isGot = 0
        while isClicked == 0:
            try:
                profile_box = self.browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[
                2]/div/div/div[ 3]/div/div[5]""")
                profile_box.click()

                profile_button = self.browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[
                2]/div/div/div[ 3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]""")
                profile_button.click()
                isClicked = 1
            except WebDriverException:
                continue

        while isReached == 0:
            try:
                follow_box = self.browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header
                /section/ul/li[3]/a""")
                follow_box.click()
                isReached = 1
            except WebDriverException:
                continue
        while isGot == 0:
            try:
                followers = self.browser.find_element_by_xpath("""/html/body/div[5]/div/div/div[2]/ul/div""")
                div = followers.find_elements_by_css_selector("button")

                for i in range(len(div)):
                    div[i].click()

                    unfollow_button = self.browser.find_element_by_xpath(
                        """/html/body/div[6]/div/div/div/div[3]/button[1]""")
                    unfollow_button.click()
                isGot = 1
            except WebDriverException:
                continue


y = Instagram("denemedeneme0342@gmail.com", "123456deneme")

y.login()
#
y.reply_message(["utkuhayrat", "efekanhezer"])
y.send_message("Bu batunun saçma sapan denemelerinden  biridir. (Python ile gönderildi.)")
#
# y.get_main_page()
# y.unfollow_all()
# index