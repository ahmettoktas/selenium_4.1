from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = "C:/Users/User/Desktop/Selenium/chromedriver.exe"
browser = webdriver.Chrome(driver_path)
browser.maximize_window()
browser.get("")

browser.implicitly_wait(20)
browser.find_element_by_id("email").send_keys("ahmet.toktas@useinsider.com")
browser.find_element_by_id("password").send_keys("")
browser.find_element_by_id("login-button").click()
browser.implicitly_wait(20)


#exercise 1
##browser.find_element_by_xpath("//label[@for = 'enableUtmSettings']").click()

#exercise 3
#input_SMS = browser.find_element_by_xpath("//div[@id = 'smsMessageAttribute']")
#input_SMS.send_keys(" ")
#print(browser.find_element_by_xpath("//p[contains(text(), 'Message')]").text)

#exercise 4
#input_SearchJourney = browser.find_element_by_xpath("//input[contains(@placeholder, 'Filter')]")
#input_SearchJourney.send_keys("test")

#exercise 5
#radiobutton_Test = browser.find_element_by_xpath("//label[@for = 'test']")
#radiobutton_Test.click()

#exercise 6
#browser.find_element_by_xpath("//img[@class = 'close']").click()
#button_statistic = browser.find_element_by_xpath("(//td[contains(@class, 'statistics')]//a//i)[1]")
#button_statistic.click()

#exercise 7
#button_Delete_Variation = browser.find_element_by_xpath("//button[@id = 'delete']").click()

#exercise 8
#button_Delete = browser.find_element_by_xpath("(//p[text() = 'Delete'])[1]")
#button_Change = browser.find_element_by_xpath("(//p[text() = 'Change'])[1]")

#exercise 9
#browser.find_element_by_xpath("//p[text() = 'SMS']").click()
#browser.implicitly_wait(20)
#browser.find_element_by_id("smsMessageAttribute").send_keys(" ")
#browser.find_element_by_name("submitButton").click()
#print(browser.find_element_by_xpath("//p[contains(text(), 'fields')]").text)

#exercise 10
#create_camp = browser.find_element(By.XPATH,"//a[contains(@class, 'btnBlue')]")
