# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time


caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "10"
caps["deviceName"] = "E940_2795_00"
caps["appPackage"] = "com.sneeze.penti"
caps["appActivity"] = ".MainActivity"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

class TouchAction():
    def __init__(self, d):
        self.driver = d

    def tap(self, x, y):
        self.driver.tap([(x, y)])

    def flick(self, start_x, start_y, end_x, end_y):
        self.driver.flick(start_x, start_y, end_x, end_y)


TouchAction(driver).tap(x=307, y=363)
time.sleep(2)
TouchAction(driver).tap(x=862, y=182)
time.sleep(2)
TouchAction(driver).flick(start_x=43, start_y=1275, end_x=1024, end_y=1265)
time.sleep(2)
TouchAction(driver).tap(x=1004, y=1912)
time.sleep(2)
TouchAction(driver).tap(x=122, y=162)
time.sleep(2)
TouchAction(driver).flick(start_x=337, start_y=317, end_x=429, end_y=1926)
time.sleep(2)
TouchAction(driver).tap(x=700, y=2203)
time.sleep(2)
TouchAction(driver).flick(start_x=664, start_y=2193, end_x=994, end_y=2203)
time.sleep(2)
TouchAction(driver).flick(start_x=486, start_y=1978, end_x=585, end_y=661)
time.sleep(2)
TouchAction(driver).flick(start_x=277, start_y=1919, end_x=363, end_y=251)

driver.quit()
