import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://orteil.dashnet.org/experiments/cookie/"

MONEY_ID_SELECTOR = "money"
ITEM_CSS_SELECTOR = "#store div"
PRICE_CSS_SELECTOR = f"{ITEM_CSS_SELECTOR} b"
COOKIE_ID_SELECTOR = "cookie"
CPS_ID_SELECTOR = "cps"


def get_cookie_count(driver):
    """Returns the current cookie count"""
    money = driver.find_element(By.ID, MONEY_ID_SELECTOR).text
    return int(money.replace(",", ""))


def get_item_ids(driver):
    """ Returns a list of item ids"""
    items = driver.find_elements(By.CSS_SELECTOR, ITEM_CSS_SELECTOR)
    return [item.get_attribute("id") for item in items]


def get_item_prices(driver):
    """Returns a list of item prices"""
    prices = driver.find_elements(By.CSS_SELECTOR, PRICE_CSS_SELECTOR)
    return [int(price.text.split("-")[1].strip().replace(",", "")) for price in prices if price.text != ""]


def update_store(item_ids, item_prices):
    """Return an updated store dict"""
    return {item_ids[n]:item_prices[n] for n in range(len(item_prices))}


def buy_upgrade(driver, cookie_count, store):
    """Buy the most expensive upgrade that can be afforded"""
    can_buy = {item_id:item_price for (item_id, item_price) in store.items() if cookie_count > item_price}
    will_buy =  max(can_buy, key=can_buy.get)
    driver.find_element(By.ID, will_buy).click()


def play_cookie_clicker():
    """Play the cookie clicker game"""

    driver = webdriver.Chrome()
    driver.get(URL)

    cookie = driver.find_element(By.ID, COOKIE_ID_SELECTOR)

    # Only need to get the item_ids once
    item_ids = get_item_ids(driver)

    # For initialization sake
    item_prices = get_item_prices(driver)
    store = update_store(item_ids, item_prices)

    five_sec_timeout = time.time() + 5
    five_min_timeout = time.time() + 60*5

    while not time.time() > five_min_timeout:
        cookie.click()
        if time.time() > five_sec_timeout:
            cookie_count = get_cookie_count(driver)
            item_prices = get_item_prices(driver)
            store = update_store(item_ids, item_prices)
            buy_upgrade(driver, cookie_count, store)
            five_sec_timeout = time.time() + 5

    cps = driver.find_element(By.ID, CPS_ID_SELECTOR).text
    print(cps)
    driver.quit()


if __name__ == '__main__':
    play_cookie_clicker()

