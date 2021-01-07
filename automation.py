from selenium import webdriver
import time

# Testing selenium using their demo site, closing the advert when it pops up, entering a message, and
# showing said message

chrome_browser = webdriver.Chrome(".\chromedriver")

chrome_browser.maximize_window()
chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

time.sleep(2) #gives time for the ad to show up

close_advert = chrome_browser.find_element_by_id("at-cv-lightbox-close")
close_advert.click() #closes the pop up ad

assert "Selenium Easy Demo" in chrome_browser.title
show_msg_button = chrome_browser.find_element_by_class_name("btn-default")

# print(show_msg_button.get_attribute("innerHTML"))

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_message.clear()
user_message.send_keys("Hello World!")

show_msg_button.click()

output_msg = chrome_browser.find_element_by_id("display")

assert "Hello World!" in output_msg.text

time.sleep(2) #just to see the results before closing
chrome_browser.close() #kinda buggy, .quit() also works
