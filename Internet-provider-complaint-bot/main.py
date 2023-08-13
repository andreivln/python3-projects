from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

PROMISED_DOWN = 500
PROMISED_UP = 400
TWITTER_EMAIL = os.environ['email']
TWITTER_PASSWORD = os.environ['password']
options = Options()
options.add_experimental_option("detach", True)
CHROME_DRIVER_PATH = webdriver.Chrome(options=options)


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        CHROME_DRIVER_PATH.get(url)
        CHROME_DRIVER_PATH.maximize_window()
        accept_termens = CHROME_DRIVER_PATH.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_termens.click()
        test_start = CHROME_DRIVER_PATH.find_element(By.CLASS_NAME, "start-text")
        test_start.click()
        sleep(50)
        x_button = CHROME_DRIVER_PATH.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
        x_button.click()
        self.down = CHROME_DRIVER_PATH.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = CHROME_DRIVER_PATH.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        url = "https://twitter.com/login"

        CHROME_DRIVER_PATH.get(url)
        CHROME_DRIVER_PATH.maximize_window()
        sleep(2)
        email = CHROME_DRIVER_PATH.find_element(By.XPATH, '//input[@name="text" and @autocomplete="username"]')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        sleep(2)
        password = CHROME_DRIVER_PATH.find_element(By.XPATH, '//input[@type="password" and @name="password"]')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)

        accept_cookies = CHROME_DRIVER_PATH.find_element(By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/div[2]/div[1]')
        accept_cookies.click()
        sleep(2)

        tweet_compose = CHROME_DRIVER_PATH.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]')
        tweet_compose.click()

        tweet = f"Hey @Internet-provider-exemple, why is my internet speed {self.down}down/{self.up}up when I pay 80 bucks per month for {PROMISED_DOWN}down/{PROMISED_UP}up?"

        tweet_compose.send_keys(tweet)
        sleep(2)

        post_button = CHROME_DRIVER_PATH.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        post_button.click()

        sleep(5)
        CHROME_DRIVER_PATH.quit()



bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
