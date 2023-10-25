from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Firefox()
browser.get('https://google.com/')
def searchAndReturn(browser, search_term):
	time.sleep(5)
	assert "Google" in browser.title

	# type into search box
	ta = browser.find_element(By.TAG_NAME, 'textarea')  # Find the search box
	ta.send_keys(search_term)

	# wait a moment
	time.sleep(1/2)
	# press enter
	ta.send_keys(Keys.RETURN)
	# wait for results page
	time.sleep(5)
	# check if search term is in browser title
	assert search_term in browser.title

	# go back to search page
	browser.back()
	time.sleep(5)
	assert "Google" in browser.title

def imFeelingLuckyTest(browser, search_term):
	# retype search term
	ta = browser.find_element(By.TAG_NAME, 'textarea')  # Find the search box
	ta.send_keys(search_term)
	# navigate to "I'm feeling lucky" button by pressing tab key 5 times
	ta.send_keys(5 * Keys.TAB)
	# click highlighted button
	browser.switch_to.active_element.click()
	time.sleep(5)
	# check if Google is NOT in the title
	assert "Google" not in browser.title
	# go back and check if Google is in the title
	browser.back()
	time.sleep(5)
	assert "Google" in browser.title

def clearTest(browser, search_term):
	ta = browser.find_element(By.TAG_NAME, 'textarea')  # Find the search box
	ta.send_keys(search_term)
	# check if search term exists
	assert search_term == ta.get_attribute("value")
	# clear text
	ta.send_keys(Keys.TAB)
	time.sleep(1)
	ta.send_keys(Keys.SPACE)
	# check if search term is cleared
	assert not search_term == ta.get_attribute("value")

def acceptCookie(browser):
	# accept cookies/privacy policy
	body = browser.find_element(By.TAG_NAME, "body")
	body.send_keys(5 * Keys.TAB)
	acceptButton = browser.switch_to.active_element
	assert acceptButton.is_displayed()
	body.send_keys(Keys.RETURN)
	assert not acceptButton.is_displayed()

print("Test 1: Accepting cookies")
acceptCookie(browser)
print("Test 2: Regular search")
searchAndReturn(browser, "do a barrel roll")
print("Test 3: I'm feeling lucky function")
imFeelingLuckyTest(browser, "test")
print("Test 4: Text clear function")
clearTest(browser, "this text will be cleared")
browser.quit();
