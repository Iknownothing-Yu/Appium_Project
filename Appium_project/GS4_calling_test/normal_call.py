import time

class NormalCall():
    def __init__(self, driver):
        self.driver = driver
        self.first_part_id = 'com.google.android.dialer:id/'

    def dialing(self):
        # open dialer pad
        self.dialer_pad = self.driver.find_element_by_accessibility_id('key pad')
        self.dialer_pad.click()
        print('dialer pad is opened')
        time.sleep(1)

        #dialing
        self.nums = ['zero', 'one', 'seven', 'six', 'four', 'seven', 'one', 'three', 'five', 'five', 'six', 'zero']
        for ele in self.nums:
            self.dialer = self.driver.find_element_by_id(self.first_part_id + ele)
            print('current number is : ',self.first_part_id + ele)
            self.dialer.click()

        #self.driver.find_element_by_id('com.google.android.dialer:id/dialpad_voice_call_button').click()
        self.driver.find_element_by_accessibility_id('dial').click()






