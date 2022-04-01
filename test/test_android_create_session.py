import unittest
import copy

from helpers import ANDROID_CAPS, get_android_webdriver

class TestAndroidCreateSession(unittest.TestCase):
    def test_should_create_and_destroy_android_session(self):
        caps = copy.copy(ANDROID_CAPS)
        caps['name'] = 'test_should_create_and_destroy_android_session'

        self.driver = get_android_webdriver(caps)
        self.driver.implicitly_wait(10)

        # make sure the right package and activity were started
        self.assertEquals('io.appium.android.apis', self.driver.current_package)
        self.assertEquals('.ApiDemos', self.driver.current_activity)

        self.driver.quit()

