# autoweb.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = r'C:\Users\ACER\Desktop\PYTHON-CODING\AUTO WEB SELENIUM\chromedriver.exe'
driver = webdriver.Chrome(path)

url = 'https://www.google.com'
driver.get(url)
search = driver.find_element_by_name('q')
search.send_keys('python')
search.send_keys(Keys.RETURN) #press enter 
driver.maximize_window()
#driver.save_screenshot(r'test.png')



for i in range(5):
	driver.execute_script('window.scrollTo(0,{})'.format(500*i))
	driver.save_screenshot('test-{}.png'.format(i))
	time.sleep(1)

driver.close()