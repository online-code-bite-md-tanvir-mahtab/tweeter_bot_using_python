
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# login info for the twiter
USER_EMAIL = 'tanvir15-13433@diu.edu.bd'
USER_NAME = 'MDTANVIRMAHTA14'
USER_PASSWORD = '01955005706#@'
TWITER_URL = 'https://twitter.com/'
SPEED_TESTING_URL = 'https://www.speedtest.net/'


class InternetspeedTweeter:
    def __init__(self,driver_path):
        self.driver = webdriver.Edge(executable_path=driver_path)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        try:
            self.driver.get(url=SPEED_TESTING_URL)
            go = self.driver.find_element_by_xpath(xpath='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
            go.click()
            sleep(20)
            self.down = self.driver.find_element_by_xpath(xpath='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            self.up = self.driver.find_element_by_xpath(xpath='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
            sleep(20)
            print(f"Download: {self.down.text}\nUpload:{self.up.text}")
        except NoSuchElementException:
            sleep(4)
            self.driver.quit()

    def tweet_at_provider(self):
        try:
            self.driver.get("https://twitter.com/login")

            sleep(3)
            print(self.driver.title)
            text = self.driver.find_element_by_xpath(xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/span')
            print(text.text)
            sign_in = self.driver.find_element_by_xpath(xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
            # sign_in = self.driver.find_element_by_xpath(xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label')
            print(sign_in.text)
            # sleep(2)
            sign_in.send_keys(USER_EMAIL)
            sign_in.send_keys(Keys.ENTER)
            sleep(4)
            username = self.driver.find_element_by_xpath(xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            print(username.text)
            username.send_keys(USER_NAME)
            username.send_keys(Keys.ENTER)
            sleep(4)
            password = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
            print(password.text)
            password.send_keys(USER_PASSWORD)
            password.send_keys(Keys.ENTER)
            sleep(1)
            post = self.driver.find_element_by_xpath(xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            print(post.text)
            post.send_keys(f"the speed of download :{self.down.text} and for upload :{self.up.text}for smile broadband but paying for 15mbps")
            sleep(4)
            tweet = self.driver.find_element_by_xpath(xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span')
            sleep(1)
            tweet.click()
        except NoSuchElementException:
            self.driver.close()
    