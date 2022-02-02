
# from selenium import webdriver
from time import sleep
from InternetspeedTweeter import InternetspeedTweeter

edge_path = "G:\edgedriver_win64\msedgedriver.exe"


# now inisializing the bot
bot = InternetspeedTweeter(driver_path=edge_path)
bot.get_internet_speed()
# sleep(30)
bot.tweet_at_provider()