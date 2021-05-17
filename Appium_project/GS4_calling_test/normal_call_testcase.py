import unittest
from GS4_calling_test.normal_call import NormalCall
from GS4_calling_test.create_driver import DriverCreater

class NormalCallTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = DriverCreater().super_driver
        self.a_call = NormalCall(self.driver)
        print('driver created!!!')

    def test_dialing(self):
        print('test dialing.......................')
        self.a_call.dialing()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



