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

def confirmMobileSignIn(driver):
    time.sleep(5)
    driver.get('https://account.microsoft.com/rewards/pointsbreakdown')
    time.sleep(5)
    driver.get('https://www.bing.com/rewards/signin?ru=https%3a%2f%2fwww.bing.com%2fsearch%3fq%3dpopular+now+on+bing%26filters%3dsegment%3a%22popularnow.carousel%22%26form%3dml10ns%26crea%3dml10ns&vt=Signin&ra=')
    time.sleep(5)
    driver.get('https://www.bing.com/fd/auth/signin?action=interactive&provider=windows_live_id&src=rewardssi&perms=&sig=0D1B6415EBC0646513956A1DEAE2659E&device=mobile&return_url=https%3a%2f%2fwww.bing.com%2frewards%2fsignin%3fru%3dhttps%253a%252f%252fwww.bing.com%252fsearch%253fq%253dpopular%2bnow%2bon%2bbing%2526filters%253dsegment%253a%2522popularnow.carousel%2522%2526form%253dml10ns%2526crea%253dml10ns%26vt%3dSignin%26ra%3d&Token=1')
    time.sleep(5)

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

    if(isMobile):
        confirmMobileSignIn(driver)

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
    start_idx= random.randint(0,2600)
    print('start_idx is ' + str(start_idx))
    for i in range(num_to_search):
        word = word_list[start_idx + i]
        driver.get(base_url + word)
        time.sleep(1)


def completeDailySearches(user_agent,num_searches,base_url,isMobile):
    driver = startWebDriver(user_agent)
    loginToRewards(driver,isMobile)
    performSearches(num_searches,base_url,driver)
    driver.quit()

base_url = 'https://www.bing.com/search?q='
edge_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
num_pc_searches = 35
android_user_agent = "Mozilla/5.0 (Android 6.0.1; Mobile; rv:63.0) Gecko/63.0 Firefox/63.0"
num_mobile_searches = 25
completeDailySearches(edge_user_agent,num_pc_searches,base_url,False);
completeDailySearches(android_user_agent,num_mobile_searches,base_url,True);
