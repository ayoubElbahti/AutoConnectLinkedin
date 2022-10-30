from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://www.linkedin.com')


def sleep_for_period_of_time():
    limit = random.randint(60,120)
    time.sleep(limit)
#********** LOG IN *************
try:
    driver.implicitly_wait(600)   
    username = driver.find_element(By.XPATH,"//input[@name='session_key']")
    password = driver.find_element(By.XPATH,"//input[@name='session_password']")

    username.send_keys(email)
    password.send_keys(password')


    submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()

    #***************** ADD CONTACTS ***********************

    for num_page in range(1,100):
        link_page = "https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={}".format(num_page)

        driver.get(link_page)


        all_buttons = driver.find_elements(By.TAG_NAME,'button')
        connect_buttons = [btn for btn in all_buttons if btn.text == "Se connecter"]

        for btn in connect_buttons:
            driver.execute_script("arguments[0].click();", btn)        
            send = driver.find_element(By.XPATH,"//button[@aria-label='Envoyer maintenant']")
            driver.execute_script("arguments[0].click();", send)
            close = driver.find_element(By.XPATH,"//button[@aria-label='Ignorer']")
            driver.execute_script("arguments[0].click();", close)
            sleep_for_period_of_time()
except Exception as e:
    print('e  => ',e)