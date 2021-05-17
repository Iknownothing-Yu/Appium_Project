from appium import webdriver
import time

class DriverCreater():
    def __init__(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "10"
        caps["deviceName"] = "E940_2795_00"
        caps["appPackage"] = "com.google.android.dialer"
        caps["appActivity"] = "com.google.android.dialer.extensions.GoogleDialtactsActivity"
        caps["ensureWebviewsHavePages"] = True
        caps["'automationName"] = "UiAutomator1"

        self.super_driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


