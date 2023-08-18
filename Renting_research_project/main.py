from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import time

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSececEgbJHxec4vL-AWvagHuwcwokj3YqHItuqTCcwVJQx0RA/viewform?usp=sf_link"
ZILLIO_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "User-Agent": "Chrome/116.0.0.0",
    "Accept-Language": "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6"

}

response = requests.get(ZILLIO_LINK, headers=headers)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.prettify())
parsed_addresses = soup.find_all(name="address")
addresses = [address.text for address in parsed_addresses]
# print(addresses)

parsed_links = soup.find_all("a", class_="property-card-link")
links = [link.get("href") for link in parsed_links]
links = list(dict.fromkeys(links))
correct_links = []
for link in links:
    if link.startswith("http"):
        correct_links.append(link)
    else:
        link = f'https://www.zillow.com/{link}'
        correct_links.append(link)


parsed_prices = soup.find_all(attrs={'data-test': 'property-card-price'})
prices = [price.text.split("+")[0] for price in parsed_prices]


class EntryData:

    def __init__(self):
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.options.add_experimental_option("detach", True))

    def data_entry(self, n):

        self.driver.get(ZILLIO_LINK)
        time.sleep(2)

        address_driver = self.driver.find_element(By.XPATH,
                                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_driver.send_keys(addresses[n])
        time.sleep(2)

        price_driver = self.driver.find_element(By.XPATH,
                                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_driver.send_keys(prices[n])
        time.sleep(2)

        link_driver = self.driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_driver.send_keys(correct_links[n])
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()


entry_bot = EntryData()

for n in range(len(addresses)):
    entry_bot.data_entry(n)

