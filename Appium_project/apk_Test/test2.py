from appium import webdriver
import time

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "10"
caps["deviceName"] = "E940_2795_00"
caps["appPackage"] = "com.google.android.dialer"
caps["appActivity"] = "com.google.android.dialer.extensions.GoogleDialtactsActivity"
caps["ensureWebviewsHavePages"] = True
caps["'automationName' "] = "UiAutomator1"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

nums = ['one', 'seven', 'six', 'four', 'seven']
dialer_pad = driver.find_element_by_accessibility_id('key pad')
dialer_pad.click()
time.sleep(3)

first_part_id = 'com.google.android.dialer:id/'
for ele in nums:
    dialer = driver.find_element_by_id(first_part_id + ele)
    print(first_part_id + ele)
    dialer.click()
    time.sleep(2)


'''
dialer = driver.find_element_by_id('com.google.android.dialer:id/five')
dialer.click()
time.sleep(2)
dialer = driver.find_element_by_id('com.google.android.dialer:id/one')
dialer.click()
'''





