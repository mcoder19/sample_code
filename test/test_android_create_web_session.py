import unittest
import copy

from helpers import ANDROID_CAPS, get_android_webdriver

class TestAndroidCreateWebSession(unittest.TestCase):
    def test_should_create_and_destroy_android_web_session(self):
        caps = copy.copy(ANDROID_CAPS)
        caps['name'] = 'test_should_create_and_destroy_android_web_session'
        # can only specify one of `app` and `browserName`
        caps['browserName'] = 'Chrome'
        caps.pop('app')

        self.driver = get_android_webdriver(caps)
        self.driver.implicitly_wait(10)

        self.driver.get('https://www.google.com')

        assert 'Google' == self.driver.title

        self.driver.quit()



