# Social-Media-Automation
Its a Selenium based social media automation app.

## Usage of Instagram

This is how to use instagram.py

### Sending messages

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

