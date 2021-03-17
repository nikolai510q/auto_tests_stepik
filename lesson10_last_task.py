from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_id("book")
button.click()

x_value = browser.find_element_by_id("input_value").text
x = calc(int(x_value))

input_answer = browser.find_element_by_id("answer")
input_answer.send_keys(x)

button_submit = browser.find_element_by_xpath("//button[@type='submit'][@class='btn btn-primary']")
button_submit.click()

time.sleep(10)
browser.quit()
