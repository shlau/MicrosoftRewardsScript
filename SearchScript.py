#!/usr/bin/env/python
import time
import requests
import json
import random
from selenium import webdriver


def startWebDriver(user_agent):
    opts = webdriver.ChromeOptions()
    opts.add_argument("user-agent={}".format(user_agent))
    driver_path = '$CHROME_DRIVER_PATH'
    driver = webdriver.Chrome(executable_path=driver_path,chrome_options=opts)
    return driver

def confirmSignIn(driver, isMobile):
    time.sleep(5)
    driver.get('https://account.microsoft.com/rewards/pointsbreakdown')
    time.sleep(5)
    driver.get('https://www.bing.com')
    time.sleep(5)
    if(isMobile):
        menu_btn = driver.find_element_by_css_selector('#mHamburger')
        menu_btn.click()
        time.sleep(2)
    signin_btn = driver.find_element_by_css_selector('#hb_s' if isMobile else '#id_s')
    try:
        signin_btn.click()
    except NoSuchElementException: 
        print("No sign in button")
    time.sleep(3)

def loginToRewards(driver, isMobile):
    login_url = 'https://login.live.com'
    driver.get(login_url)
    user_id_element = driver.find_element_by_css_selector('input[type="email"]')
    submit_button_element = driver.find_element_by_css_selector('input[type="submit"]')
    user_id_element.send_keys('$USERNAME')
    submit_button_element.click()

    passwd_element = driver.find_element_by_css_selector('input[type="password"]')
    passwd_element.send_keys('$PASSWORD')

    time.sleep(5)
    login_button = driver.find_element_by_css_selector('input[type="submit"]')
    actions = webdriver.ActionChains(driver)
    actions.move_to_element(login_button).click().perform()

    confirmSignIn(driver, isMobile)

def forceAlert(base_url, driver):
    trigger_word = 'my location'
    driver.get(base_url + trigger_word)
    time.sleep(3)
    try:
        alert = driver.switch_to_alert()
        alert.accept()
    except:
        print("No alert popup.")
    time.sleep(3)

def performSearches(num_to_search,base_url,driver):
    random_words_url = "https://www.randomlists.com/data/words.json"
    response = requests.get(random_words_url)
    word_list = response.json()['data']
    forceAlert(base_url,driver)
    start_idx= random.randint(0,1000)
    print('start_idx is ' + str(start_idx))
    for i in range(num_to_search):
        word = word_list[start_idx + i]
        driver.get(base_url + word)
        time.sleep(1)


def completeDailySearches(user_agent,num_searches,base_url,isMobile):
    driver = startWebDriver(user_agent)
    loginToRewards(driver,isMobile)
    time.sleep(3)
    performSearches(num_searches,base_url,driver)
    driver.quit()

base_url = 'https://www.bing.com/search?q='
edge_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
num_pc_searches = 35
android_user_agent = "Mozilla/5.0 (Android 6.0.1; Mobile; rv:63.0) Gecko/63.0 Firefox/63.0"
num_mobile_searches = 25
completeDailySearches(edge_user_agent,num_pc_searches,base_url,False);
completeDailySearches(android_user_agent,num_mobile_searches,base_url,True);
