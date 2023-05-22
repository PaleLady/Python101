#pyautogui

import pyautogui
import time
import webbrowser

def search(country):
	time.sleep(1)
	webbrowser.open('https://www.google.com/')
	time.sleep(1)
	pyautogui.click(515,54)
	pyautogui.write(country,)
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.screenshot('{}.jpg'.format(country))

search('china')