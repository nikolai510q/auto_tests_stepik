from selenium import webdriver
import os
import time

try:
  link = "http://suninjuly.github.io/file_input.html"
  browser = webdriver.Chrome()
  browser.get(link)

  input1 = browser.find_element_by_xpath("//input[@name='firstname'][@required]")
  input1.send_keys("Nick")
  input2 = browser.find_element_by_xpath("//input[@name='lastname'][@required]")
  input2.send_keys("Lion")
  input3 = browser.find_element_by_xpath("//input[@name='email'][@required]")
  input3.send_keys("goodQA@mail.ru")

  current_dir = os.path.abspath(os.path.dirname(__file__))
  file_path = os.path.join(current_dir, 'file.txt')
  load_file_button = browser.find_element_by_id("file")
  load_file_button.send_keys(file_path)
  
  submit_button = browser.find_element_by_xpath("//button[@type='submit'][@class='btn btn-primary']")
  submit_button.click()

finally:
  time.sleep(10)
  browser.quit()