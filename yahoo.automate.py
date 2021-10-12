from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC        
browser = webdriver.Firefox()
allspamemails= []
browser.get('https://mail.yahoo.com/d/folders/6')
WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='phone-no ' and @id='login-username']"))).send_keys('') #enter email here
browser.find_element_by_id("login-signin").click()
WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-passwd']"))).send_keys('') #enter Email password here
browser.find_element_by_id("login-signin").click()
#browser.get('https://mail.yahoo.com/d/folders/6')
#d = browser.find_element_by_id("div[aria-label='Message list']")

elems = browser.find_elements_by_xpath("//a[@href]")
for elem in elems:
    if 'mail.yahoo.com/d/folders/6/messages/71031' in elem.get_attribute("href"):
        #allspamemails.append(elem.get_attribute("href"))
        print(elem.get_attribute("href"))
        browser.get(elem.get_attribute("href"))
        #spamicon = browser.find_elements_by_xpath("//svg[@href]")
        WebDriverWait(browser, 15)
        elems = browser.find_element(By.XPATH, '//button[@aria-label="Mark as not spam"]').click()
#print(d)
#driver.close()
