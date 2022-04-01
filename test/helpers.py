import os
from selenium.common.exceptions import InvalidSessionIdException
from pathlib import Path
from appium import webdriver

IS_DOCKER = True
project_path = Path(__file__).parent.parent
appium_server_host = "127.0.0.1" if not IS_DOCKER else "appium_container"
APP_PATH = 'apps/ApiDemos-debug.apk'
CHROMEDRIVER_MAC_PATH = 'chromedrivers/mac/chromedriver'
CHROMEDRIVER_LINUX_PATH = 'chromedrivers/linux/chromedriver'

ANDROID_BASE_CAPS = {
    'app':  str(Path.joinpath(project_path, APP_PATH)),  
    'chromedriverExecutable': str(Path.joinpath(project_path, CHROMEDRIVER_MAC_PATH)),
    # 'chromedriverExecutableDir': str(Path.joinpath(project_path, 'chromedrivers/mac')),
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'deviceName': 'device' 
}

ANDROID_DOCKER_CAPS = {
    'app': APP_PATH,  
    'chromedriverExecutable': CHROMEDRIVER_LINUX_PATH,
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'deviceName': 'device',
    'showChromedriverLog': True,
    'remoteAdbHost': 'gateway.docker.internal',
    'chromedriverArgs': ["--whitelisted-ips='gateway.docker.internal'"] 
}

ANDROID_CAPS = ANDROID_BASE_CAPS if not IS_DOCKER else ANDROID_DOCKER_CAPS

def get_webdriver(host, port, endpoint, capabilities):
    appium_server_url = 'http://{}:{}{}'.format(host, port, endpoint)
    driver = webdriver.Remote(appium_server_url, capabilities)
    return driver

def get_android_webdriver(caps):
    return get_webdriver(appium_server_host, 4723, '/wd/hub', caps)


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def take_screenshot_and_logcat(driver, device_logger, calling_request):
    __save_log_type(driver, device_logger, calling_request, 'logcat')


def take_screenshot_and_syslog(driver, device_logger, calling_request):
    __save_log_type(driver, device_logger, calling_request, 'syslog')


def __save_log_type(driver, device_logger, calling_request, type):
    logcat_dir = device_logger.logcat_dir
    screenshot_dir = device_logger.screenshot_dir

    try:
        driver.save_screenshot(os.path.join(screenshot_dir, calling_request + '.png'))
        logcat_data = driver.get_log(type)
    except InvalidSessionIdException:
        logcat_data = ''

    with open(os.path.join(logcat_dir, '{}_{}.log'.format(calling_request, type)), 'w') as logcat_file:
        for data in logcat_data:
            data_string = '%s:  %s\n' % (data['timestamp'], data['message'].encode('utf-8'))
            logcat_file.write(data_string)

