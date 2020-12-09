<h1 align="center">Welcome to Social Media Automation 👋</h1>

> This is a ***__selenium based__*** social media automation application made with python. **instagram.py** and **whatsapp.py** are our main codes. **app.py** is sample code for **instagram.py** and **whatsapp.py** used together. It will be available for *****all social media platforms***** very soon...

## ✨ Usage of Instagram

This is how to use instagram.py


<p align="center">
  <img width="700" align="center" src="" alt="demo"/>
</p>

### Sending messages

`login()` : Use for login to your account.

`get_main_page()` : Use for reach the home page of instagram. 
- ###### If you don't use this code you can get some errors.


`reply_message()` : Use for add targets to message list.

`send_message()` : Use for send message to targets.

###### The sample usage of code below. :point_down:

```python
from instagram import Instagram

# Create an Instagram object.
intgrm = Instagram("Your username", "Your password")

# Login to your account.
intgrm.login() 

# Send message to target.
intgrm.get_main_page()
intgrm.reply_message(["List of targets"])
intgrm.send_message("Your message")
```

#### Unfollow all users

`unfollow_all()` : Use for  __unfollow all users__.

###### The sample usage of code below. :point_down:

```python
from instagram import Instagram

# Create an Instagram object.
intgrm = Instagram("Your username", "Your password")

# Login to your account.
intgrm.login() 

# Reach the homepage and unfollow all.
intgrm.get_main_page()
intgrm.unfollow_all()
```
  
  
## ✨ Usage of WhatsApp

This is how to use whatsapp.py

### Spam messages

It is easy to send message with this code!

`login()` : Use for login your WhatsApp acoount. (In this part it will ask you for scan the QR code. And if you ***don't scan the QR code*** code will **__not__** continue.)

`spam_messages()` : Use for spam messages to target.

###### The sample usage of code below. :point_down:

```python
from whatsapp import Whatsapp

# Create an Whatsapp object.
wp = Whatsapp()

# Login to your account. 
wp.login()

# Spam messages
wp.spam_messages("Target", "Spam message", spam_count)
```
