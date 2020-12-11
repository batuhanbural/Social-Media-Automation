from instagram import Instagram
from whatsapp import Whatsapp


class App:
    def __init__(self, application: str, **kwargs):
        self.username = ""
        self.password = ""

        for key, value in kwargs.items():
            if key == "username":
                self.username = value
            elif key == "password":
                self.password = value
            else:
                pass

        if application == "instagram":
            self.insta = Instagram(self.username, self.password)
        elif application == "whatsapp":
            self.wp = Whatsapp()

    def spam_wp(self, user_target, i_spam_message, i_spam_count):
        self.wp.login()
        self.wp.spam_messages(user_target, i_spam_message, i_spam_count)

    def message_insta(self, user_targets, user_message):
        self.insta.login()
        self.insta.reply_message(user_targets)
        self.insta.send_message(user_message)


while True:
    operation = input("İşlem yapmak istediğiniz uygulamayı seçiniz.\n1- WhatsApp\n2- Instagram\n")
    if operation == "1":
        wp_operation = input("Yapmak istediğiniz işlemi seçin.\n1- Message Spammer\n2- Online Tracker\n")
        if wp_operation == "1":
            target = input("Hedefinizi seçin.")
            spam_message = input("Spam mesajı girin.")
            spam_count = int(input("Spam miktarını giriniz."))

            app = App("whatsapp")
            app.spam_wp(target, spam_message, spam_count)
            app.wp.browser.quit()
            del app
        elif wp_operation == "2":
            app = App("whatsapp")
            app.wp.online_tracker("babaannem")
    elif operation == "2":
        insta_operation = input("Yapmak istediğiniz işlemi seçin.\n1- Message Sender\n2- **********\n")
        if insta_operation == "1":
            username = input("Kullanıcı adınızı veya e-postanızı giriniz.")
            password = input("Şifrenizi giriniz.")
            targets = input("Hedeflerinizi seçin.").replace(" ", "").split(",")
            message = input("Spam mesajı girin.")

            app = App("instagram", username=username, password=password)
            app.message_insta(targets, message)
            app.insta.browser.quit()
            del app
        elif insta_operation == "2":
            pass