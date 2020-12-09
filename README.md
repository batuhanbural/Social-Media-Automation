# Social Media Automation
It's a Selenium based social media automation app.

### Usage of Instagram

This is how to use instagram.py

#### Sending messages

`login()` : Use for login to your account.

`get_main_page()` : Use for reach the home page of instagram. 
>If you don't use this code wou can get some errors.

\
`reply_message()` : Use for add targets to message list.\
``send_message()` : Use for send message to tagets.

```python
from instagram import Instagram

# Create an Instagram object.
intgrm = Instagram("Your username", "Your password")

# This part for login to your account.
intgrm.login() 

# For send send message to target use this code.
intgrm.get_main_page()
intgrm.reply_message(["List of targets"])
intgrm.send_message("Your message")

