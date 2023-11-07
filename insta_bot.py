from instabot import Bot
from PIL import Image  

import os 
import glob

cookie_del = glob.glob("config/*cookie.json")
if cookie_del : os.remove(cookie_del[0])

im = Image.open("YOUR_FILE_NAME.jpg")  
newsize = (1080, 1080) 
im1 = im.resize(newsize) 
im1.save('resized_YOUR_FILE_NAME.jpg')


bot = Bot()

bot.login(username="YOUR_USER_NAME", password = "YOUR_MDP")

bot.upload_photo("./resized_japan.jpg", caption = "Pink Cherry Blossom Tree Under Blue Sky")