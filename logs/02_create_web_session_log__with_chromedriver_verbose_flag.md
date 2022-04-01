# Log when executing `pytest test/test_android_create_web_session.py` in the docker setup

## test_script_container

```bash
root@5c306eec718b:/code# pytest test/test_android_create_web_session.py
=================================================================================================================== test session starts ====================================================================================================================
platform linux -- Python 3.8.10, pytest-7.1.1, pluggy-1.0.0
rootdir: /code
collected 1 item

test/test_android_create_web_session.py F                                                                                                                                                                                                            [100%]

========================================================================================================================= FAILURES =========================================================================================================================
______________________________________________________________________________________ TestAndroidCreateWebSession.test_should_create_and_destroy_android_web_session ______________________________________________________________________________________

self = <test_android_create_web_session.TestAndroidCreateWebSession testMethod=test_should_create_and_destroy_android_web_session>

    def test_should_create_and_destroy_android_web_session(self):
        caps = copy.copy(ANDROID_CAPS)
        caps['name'] = 'test_should_create_and_destroy_android_web_session'
        # can only specify one of `app` and `browserName`
        caps['browserName'] = 'Chrome'
        caps.pop('app')

>       self.driver = get_android_webdriver(caps)

test/test_android_create_web_session.py:14:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
test/helpers.py:40: in get_android_webdriver
    return get_webdriver(appium_server_host, 4723, '/wd/hub', caps)
test/helpers.py:36: in get_webdriver
    driver = webdriver.Remote(appium_server_url, capabilities)
/usr/local/lib/python3.8/dist-packages/appium/webdriver/webdriver.py:274: in __init__
    super().__init__(
/usr/local/lib/python3.8/dist-packages/selenium/webdriver/remote/webdriver.py:269: in __init__
    self.start_session(capabilities, browser_profile)
/usr/local/lib/python3.8/dist-packages/appium/webdriver/webdriver.py:369: in start_session
    response = self.execute(RemoteCommand.NEW_SESSION, parameters)
/usr/local/lib/python3.8/dist-packages/selenium/webdriver/remote/webdriver.py:425: in execute
    self.error_handler.check_response(response)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <selenium.webdriver.remote.errorhandler.ErrorHandler object at 0x7f93aae9dd30>
response = {'status': 500, 'value': '{"value":{"error":"unknown error","message":"An unknown server-side error occurred while pro...    at asyncHandler (/usr/lib/node_modules/appium/node_modules/appium-base-driver/lib/protocol/protocol.js:380:37)"}}'}

    def check_response(self, response: Dict[str, Any]) -> None:
        """
        Checks that a JSON response from the WebDriver does not have an error.

        :Args:
         - response - The JSON response from the WebDriver server as a dictionary
           object.

        :Raises: If the response contains an error message.
        """
        status = response.get('status', None)
        if not status or status == ErrorCode.SUCCESS:
            return
        value = None
        message = response.get("message", "")
        screen: str = response.get("screen", "")
        stacktrace = None
        if isinstance(status, int):
            value_json = response.get('value', None)
            if value_json and isinstance(value_json, str):
                import json
                try:
                    value = json.loads(value_json)
                    if len(value.keys()) == 1:
                        value = value['value']
                    status = value.get('error', None)
                    if not status:
                        status = value.get("status", ErrorCode.UNKNOWN_ERROR)
                        message = value.get("value") or value.get("message")
                        if not isinstance(message, str):
                            value = message
                            message = message.get('message')
                    else:
                        message = value.get('message', None)
                except ValueError:
                    pass

        exception_class: Type[WebDriverException]
        if status in ErrorCode.NO_SUCH_ELEMENT:
            exception_class = NoSuchElementException
        elif status in ErrorCode.NO_SUCH_FRAME:
            exception_class = NoSuchFrameException
        elif status in ErrorCode.NO_SUCH_SHADOW_ROOT:
            exception_class = NoSuchShadowRootException
        elif status in ErrorCode.NO_SUCH_WINDOW:
            exception_class = NoSuchWindowException
        elif status in ErrorCode.STALE_ELEMENT_REFERENCE:
            exception_class = StaleElementReferenceException
        elif status in ErrorCode.ELEMENT_NOT_VISIBLE:
            exception_class = ElementNotVisibleException
        elif status in ErrorCode.INVALID_ELEMENT_STATE:
            exception_class = InvalidElementStateException
        elif status in ErrorCode.INVALID_SELECTOR \
                or status in ErrorCode.INVALID_XPATH_SELECTOR \
                or status in ErrorCode.INVALID_XPATH_SELECTOR_RETURN_TYPER:
            exception_class = InvalidSelectorException
        elif status in ErrorCode.ELEMENT_IS_NOT_SELECTABLE:
            exception_class = ElementNotSelectableException
        elif status in ErrorCode.ELEMENT_NOT_INTERACTABLE:
            exception_class = ElementNotInteractableException
        elif status in ErrorCode.INVALID_COOKIE_DOMAIN:
            exception_class = InvalidCookieDomainException
        elif status in ErrorCode.UNABLE_TO_SET_COOKIE:
            exception_class = UnableToSetCookieException
        elif status in ErrorCode.TIMEOUT:
            exception_class = TimeoutException
        elif status in ErrorCode.SCRIPT_TIMEOUT:
            exception_class = TimeoutException
        elif status in ErrorCode.UNKNOWN_ERROR:
            exception_class = WebDriverException
        elif status in ErrorCode.UNEXPECTED_ALERT_OPEN:
            exception_class = UnexpectedAlertPresentException
        elif status in ErrorCode.NO_ALERT_OPEN:
            exception_class = NoAlertPresentException
        elif status in ErrorCode.IME_NOT_AVAILABLE:
            exception_class = ImeNotAvailableException
        elif status in ErrorCode.IME_ENGINE_ACTIVATION_FAILED:
            exception_class = ImeActivationFailedException
        elif status in ErrorCode.MOVE_TARGET_OUT_OF_BOUNDS:
            exception_class = MoveTargetOutOfBoundsException
        elif status in ErrorCode.JAVASCRIPT_ERROR:
            exception_class = JavascriptException
        elif status in ErrorCode.SESSION_NOT_CREATED:
            exception_class = SessionNotCreatedException
        elif status in ErrorCode.INVALID_ARGUMENT:
            exception_class = InvalidArgumentException
        elif status in ErrorCode.NO_SUCH_COOKIE:
            exception_class = NoSuchCookieException
        elif status in ErrorCode.UNABLE_TO_CAPTURE_SCREEN:
            exception_class = ScreenshotException
        elif status in ErrorCode.ELEMENT_CLICK_INTERCEPTED:
            exception_class = ElementClickInterceptedException
        elif status in ErrorCode.INSECURE_CERTIFICATE:
            exception_class = InsecureCertificateException
        elif status in ErrorCode.INVALID_COORDINATES:
            exception_class = InvalidCoordinatesException
        elif status in ErrorCode.INVALID_SESSION_ID:
            exception_class = InvalidSessionIdException
        elif status in ErrorCode.UNKNOWN_METHOD:
            exception_class = UnknownMethodException
        else:
            exception_class = WebDriverException
        if not value:
            value = response['value']
        if isinstance(value, str):
            raise exception_class(value)
        if message == "" and 'message' in value:
            message = value['message']

        screen = None  # type: ignore[assignment]
        if 'screen' in value:
            screen = value['screen']

        stacktrace = None
        st_value = value.get('stackTrace') or value.get('stacktrace')
        if st_value:
            if isinstance(st_value, str):
                stacktrace = st_value.split('\n')
            else:
                stacktrace = []
                try:
                    for frame in st_value:
                        line = self._value_or_default(frame, 'lineNumber', '')
                        file = self._value_or_default(frame, 'fileName', '<anonymous>')
                        if line:
                            file = "%s:%s" % (file, line)
                        meth = self._value_or_default(frame, 'methodName', '<anonymous>')
                        if 'className' in frame:
                            meth = "%s.%s" % (frame['className'], meth)
                        msg = "    at %s (%s)"
                        msg = msg % (meth, file)
                        stacktrace.append(msg)
                except TypeError:
                    pass
        if exception_class == UnexpectedAlertPresentException:
            alert_text = None
            if 'data' in value:
                alert_text = value['data'].get('text')
            elif 'alert' in value:
                alert_text = value['alert'].get('text')
            raise exception_class(message, screen, stacktrace, alert_text)  # type: ignore[call-arg]  # mypy is not smart enough here
>       raise exception_class(message, screen, stacktrace)
E       selenium.common.exceptions.WebDriverException: Message: An unknown server-side error occurred while processing the command. Original error: An unknown server-side error occurred while processing the command. Original error: unknown error: Failed to run adb command with networking error: net::ERR_ADDRESS_INVALID. Is the adb server running? Extra response: <>.
E       Stacktrace:
E       UnknownError: An unknown server-side error occurred while processing the command. Original error: An unknown server-side error occurred while processing the command. Original error: unknown error: Failed to run adb command with networking error: net::ERR_ADDRESS_INVALID. Is the adb server running? Extra response: <>.
E           at getResponseForW3CError (/usr/lib/node_modules/appium/node_modules/appium-base-driver/lib/protocol/errors.js:804:9)
E           at asyncHandler (/usr/lib/node_modules/appium/node_modules/appium-base-driver/lib/protocol/protocol.js:380:37)

/usr/local/lib/python3.8/dist-packages/selenium/webdriver/remote/errorhandler.py:247: WebDriverException
===================================================================================================================== warnings summary =====================================================================================================================
test/test_android_create_web_session.py::TestAndroidCreateWebSession::test_should_create_and_destroy_android_web_session
  /usr/local/lib/python3.8/dist-packages/appium/webdriver/webdriver.py:274: DeprecationWarning: desired_capabilities has been deprecated, please pass in an Options object with options kwarg
    super().__init__(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================================================================================= short test summary info ==================================================================================================================
FAILED test/test_android_create_web_session.py::TestAndroidCreateWebSession::test_should_create_and_destroy_android_web_session - selenium.common.exceptions.WebDriverException: Message: An unknown server-side error occurred while processing the comm...
============================================================================================================== 1 failed, 1 warning in 11.49s ===============================================================================================================
root@5c306eec718b:/code#
```

## appium_container

Note: I have replaced the original identifier of the device with `DEVICE_UDID`.

```bash
root@886ee5a5eff6:~# appium
[Appium] Welcome to Appium v1.22.0
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
[debug] [HTTP] Request idempotency key: 6081146a-0e2b-4e30-93e5-be1433e2638a
[HTTP] --> POST /wd/hub/session
[HTTP] {"capabilities":{"alwaysMatch":{"appium:chromedriverExecutable":"chromedrivers/linux/chromedriver","appium:automationName":"UIAutomator2","platformName":"Android","appium:deviceName":"device","appium:showChromedriverLog":true,"appium:remoteAdbHost":"gateway.docker.internal","appium:name":"test_should_create_and_destroy_android_web_session","browserName":"Chrome"},"firstMatch":[{}]},"desiredCapabilities":{"chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","platformName":"Android","deviceName":"device","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","name":"test_should_create_and_destroy_android_web_session","browserName":"Chrome"}}
[debug] [W3C] Calling AppiumDriver.createSession() with args: [{"chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","platformName":"Android","deviceName":"device","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","name":"test_should_create_and_destroy_android_web_session","browserName":"Chrome"},null,{"alwaysMatch":{"appium:chromedriverExecutable":"chromedrivers/linux/chromedriver","appium:automationName":"UIAutomator2","platformName":"Android","appium:deviceName":"device","appium:showChromedriverLog":true,"appium:remoteAdbHost":"gateway.docker.internal","appium:name":"test_should_create_and_destroy_android_web_session","browserName":"Chrome"},"firstMatch":[{}]}]
[debug] [BaseDriver] Event 'newSessionRequested' logged at 1648835715120 (10:55:15 GMT-0700 (Pacific Daylight Time))
[Appium] Appium v1.22.0 creating new AndroidUiautomator2Driver (v1.69.0) session
[debug] [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
[debug] [BaseDriver] Creating session with W3C capabilities: {
[debug] [BaseDriver]   "alwaysMatch": {
[debug] [BaseDriver]     "platformName": "Android",
[debug] [BaseDriver]     "browserName": "Chrome",
[debug] [BaseDriver]     "appium:chromedriverExecutable": "chromedrivers/linux/chromedriver",
[debug] [BaseDriver]     "appium:automationName": "UIAutomator2",
[debug] [BaseDriver]     "appium:deviceName": "device",
[debug] [BaseDriver]     "appium:showChromedriverLog": true,
[debug] [BaseDriver]     "appium:remoteAdbHost": "gateway.docker.internal",
[debug] [BaseDriver]     "appium:name": "test_should_create_and_destroy_android_web_session"
[debug] [BaseDriver]   },
[debug] [BaseDriver]   "firstMatch": [
[debug] [BaseDriver]     {}
[debug] [BaseDriver]   ]
[debug] [BaseDriver] }
[BaseDriver] The following capabilities were provided, but are not recognized by Appium:
[BaseDriver]   name
[BaseDriver] Session created with session id: a04720a5-72b1-4b0e-a468-f52c62064f4f
[UiAutomator2] We're going to run a Chrome-based session
[UiAutomator2] Chrome-type package and activity are com.android.chrome and com.google.android.apps.chrome.Main
[UiAutomator2] Starting 'com.android.chrome' directly on the device
[ADB] Found 1 'build-tools' folders under '/root' (newest first):
[ADB]     /root/build-tools/31.0.0
[ADB] Using 'adb' from '/root/platform-tools/adb'
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 start-server'
[AndroidDriver] Retrieving device list
[debug] [ADB] Trying to find a connected android device
[debug] [ADB] Getting connected devices
[debug] [ADB] Connected devices: [{"udid":"DEVICE_UDID","state":"device"}]
[AndroidDriver] Using device: DEVICE_UDID
[ADB] Using 'adb' from '/root/platform-tools/adb'
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 start-server'
[debug] [ADB] Setting device id to DEVICE_UDID
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell getprop ro.build.version.sdk'
[debug] [ADB] Current device property 'ro.build.version.sdk': 28
[ADB] Getting device platform version
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell getprop ro.build.version.release'
[debug] [ADB] Current device property 'ro.build.version.release': 9
[debug] [ADB] Device API level: 28
[UiAutomator2] Relaxing hidden api policy
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell 'settings put global hidden_api_policy_pre_p_apps 1;settings put global hidden_api_policy_p_apps 1;settings put global hidden_api_policy 1''
[AndroidDriver] No app sent in, not parsing package/activity
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID wait-for-device'
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell echo ping'
[debug] [AndroidDriver] Pushing settings apk to device...
[debug] [ADB] Getting install status for io.appium.settings
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell dumpsys package io.appium.settings'
[debug] [ADB] 'io.appium.settings' is installed
[debug] [ADB] Getting package info for 'io.appium.settings'
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell dumpsys package io.appium.settings'
[debug] [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.4.0' >= '3.4.0')
[debug] [ADB] There is no need to install/upgrade '/usr/lib/node_modules/appium/node_modules/io.appium.settings/apks/settings_apk-debug.apk'
[debug] [ADB] Getting IDs of all 'io.appium.settings' processes
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell 'pgrep --help; echo $?''
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell pgrep -f \(\[\[:blank:\]\]\|\^\)io\.appium\.settings\(\[\[:blank:\]\]\|\$\)'
[debug] [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell appops set io.appium.settings android:mock_location allow'
[debug] [Logcat] Starting logs capture with command: /root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID logcat -v threadtime
[debug] [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
[debug] [ADB] Forwarding system: 8200 to device: 6790
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID forward tcp:8200 tcp:6790'
[debug] [ADB] Getting install status for io.appium.uiautomator2.server
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell dumpsys package io.appium.uiautomator2.server'
[debug] [ADB] 'io.appium.uiautomator2.server' is installed
[debug] [ADB] Getting package info for 'io.appium.uiautomator2.server'
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell dumpsys package io.appium.uiautomator2.server'
[debug] [ADB] The version name of the installed 'io.appium.uiautomator2.server' is greater or equal to the application version name ('4.24.0' >= '4.24.0')
[debug] [UiAutomator2] io.appium.uiautomator2.server installation state: sameVersionInstalled
[debug] [ADB] Checking app cert for /usr/lib/node_modules/appium/node_modules/appium-uiautomator2-server/apks/appium-uiautomator2-server-v4.24.0.apk
[ADB] Using 'apksigner.jar' from '/root/build-tools/31.0.0/lib/apksigner.jar'
[debug] [ADB] Starting apksigner: /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java -Xmx1024M -Xss1m -jar /root/build-tools/31.0.0/lib/apksigner.jar verify --print-certs /usr/lib/node_modules/appium/node_modules/appium-uiautomator2-server/apks/appium-uiautomator2-server-v4.24.0.apk
[debug] [ADB] apksigner stdout: Signer #1 certificate DN: EMAILADDRESS=android@android.com, CN=Android, OU=Android, O=Android, L=Mountain View, ST=California, C=US
[debug] [ADB] Signer #1 certificate SHA-256 digest: a40da80a59d170caa950cf15c18c454d47a39b26989d8b640ecd745ba71bf5dc
[debug] [ADB] Signer #1 certificate SHA-1 digest: 61ed377e85d386a8dfee6b864bd85b0bfaa5af81
[debug] [ADB] Signer #1 certificate MD5 digest: e89b158e4bcf988ebd09eb83f5378e87
[debug] [ADB]
[debug] [ADB] sha256 hash did match for 'appium-uiautomator2-server-v4.24.0.apk'
[ADB] '/usr/lib/node_modules/appium/node_modules/appium-uiautomator2-server/apks/appium-uiautomator2-server-v4.24.0.apk' is signed with the default certificate
[debug] [ADB] Getting install status for io.appium.uiautomator2.server.test
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell dumpsys package io.appium.uiautomator2.server.test'
[debug] [ADB] 'io.appium.uiautomator2.server.test' is installed
[debug] [ADB] Checking app cert for /usr/lib/node_modules/appium/node_modules/appium-uiautomator2-server/apks/appium-uiautomator2-server-debug-androidTest.apk
[debug] [ADB] Starting apksigner: /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java -Xmx1024M -Xss1m -jar /root/build-tools/31.0.0/lib/apksigner.jar verify --print-certs /usr/lib/node_modules/appium/node_modules/appium-uiautomator2-server/apks/appium-uiautomator2-server-debug-androidTest.apk
[debug] [ADB] apksigner stdout: Signer #1 certificate DN: EMAILADDRESS=android@android.com, CN=Android, OU=Android, O=Android, L=Mountain View, ST=California, C=US
[debug] [ADB] Signer #1 certificate SHA-256 digest: a40da80a59d170caa950cf15c18c454d47a39b26989d8b640ecd745ba71bf5dc
[debug] [ADB] Signer #1 certificate SHA-1 digest: 61ed377e85d386a8dfee6b864bd85b0bfaa5af81
[debug] [ADB] Signer #1 certificate MD5 digest: e89b158e4bcf988ebd09eb83f5378e87
[debug] [ADB]
[debug] [ADB] sha256 hash did match for 'appium-uiautomator2-server-debug-androidTest.apk'
[ADB] '/usr/lib/node_modules/appium/node_modules/appium-uiautomator2-server/apks/appium-uiautomator2-server-debug-androidTest.apk' is signed with the default certificate
[UiAutomator2] Server packages are not going to be (re)installed
[debug] [UiAutomator2] Waiting up to 30000ms for services to be available
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell pm list instrumentation'
[debug] [UiAutomator2] Instrumentation target 'io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner' is available
[ADB] Adding packages ["io.appium.settings","io.appium.uiautomator2.server","io.appium.uiautomator2.server.test"] to Doze whitelist
[debug] [ADB] Got the following command chunks to execute: [["dumpsys","deviceidle","whitelist","+io.appium.settings",";","dumpsys","deviceidle","whitelist","+io.appium.uiautomator2.server",";","dumpsys","deviceidle","whitelist","+io.appium.uiautomator2.server.test",";"]]
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell dumpsys deviceidle whitelist +io.appium.settings ; dumpsys deviceidle whitelist +io.appium.uiautomator2.server ; dumpsys deviceidle whitelist +io.appium.uiautomator2.server.test ;'
[debug] [UiAutomator2] No app capability. Assuming it is already on the device
[debug] [ADB] Getting install status for com.android.chrome
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell dumpsys package com.android.chrome'
[debug] [ADB] 'com.android.chrome' is installed
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell am force-stop com.android.chrome'
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell pm clear com.android.chrome'
[debug] [AndroidDriver] Performed fast reset on the installed 'com.android.chrome' application (stop and clear)
[debug] [UiAutomator2] Performing shallow cleanup of automation leftovers
[debug] [UiAutomator2] No obsolete sessions have been detected (socket hang up)
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell am force-stop io.appium.uiautomator2.server.test'
[UiAutomator2] Starting UIAutomator2 server 4.24.0
[UiAutomator2] Using UIAutomator2 server from '/usr/lib/node_modules/appium/node_modules/appium-uiautomator2-server/apks/appium-uiautomator2-server-v4.24.0.apk' and test from '/usr/lib/node_modules/appium/node_modules/appium-uiautomator2-server/apks/appium-uiautomator2-server-debug-androidTest.apk'
[UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
[debug] [ADB] Creating ADB subprocess with args: ["-H","gateway.docker.internal","-P",5037,"-s","DEVICE_UDID","shell","am","instrument","-w","-e","disableAnalytics",true,"io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
[debug] [WD Proxy] Matched '/status' to command name 'getStatus'
[debug] [WD Proxy] Proxying [GET /status] to [GET http://gateway.docker.internal:8200/wd/hub/status] with no body
[WD Proxy] socket hang up
[debug] [WD Proxy] Matched '/status' to command name 'getStatus'
[debug] [WD Proxy] Proxying [GET /status] to [GET http://gateway.docker.internal:8200/wd/hub/status] with no body
[WD Proxy] socket hang up
[debug] [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
[debug] [WD Proxy] Matched '/status' to command name 'getStatus'
[debug] [WD Proxy] Proxying [GET /status] to [GET http://gateway.docker.internal:8200/wd/hub/status] with no body
[WD Proxy] socket hang up
[debug] [WD Proxy] Matched '/status' to command name 'getStatus'
[debug] [WD Proxy] Proxying [GET /status] to [GET http://gateway.docker.internal:8200/wd/hub/status] with no body
[debug] [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
[debug] [UiAutomator2] The initialization of the instrumentation process took 3277ms
[debug] [WD Proxy] Matched '/session' to command name 'createSession'
[debug] [WD Proxy] Proxying [POST /session] to [POST http://gateway.docker.internal:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","browserName":"Chrome","chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","deviceName":"device","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","name":"test_should_create_and_destroy_android_web_session"},"platformName":"Android","browserName":"Chrome","chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","deviceName":"DEVICE_UDID","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","name":"test_should_create_and_destroy_android_web_session","appPackage":"com.android.chrome","appActivity":"com.google.android.apps.chrome.Main","deviceUDID":"DEVICE_UDID"}],"alwaysMatch":{}}}
[debug] [WD Proxy] Got response with status 200: {"sessionId":"10d01d68-2db5-4a80-ad8a-e348a99cad8f","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","browserName":"Chrome","chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","deviceName":"device","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","name":"test_should_create_and_destroy_android_web_session"},"platformName":"Android","browserName":"Chrome","chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","deviceName":"DEVICE_UDID","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","name":"test_should_create_and_destroy_android_web_session","appPackage":"com.android.chrome","appActivity":"com.google.android.apps.chrome.Main","deviceUDID":"DEVICE_UDID"}],"always...
[WD Proxy] Determined the downstream protocol as 'W3C'
[debug] [WD Proxy] Proxying [GET /appium/device/info] to [GET http://gateway.docker.internal:8200/wd/hub/session/10d01d68-2db5-4a80-ad8a-e348a99cad8f/appium/device/info] with no body
[debug] [WD Proxy] Got response with status 200: {"sessionId":"10d01d68-2db5-4a80-ad8a-e348a99cad8f","value":{"androidId":"8e2f3e3b1d2a8f39","apiVersion":"28","bluetooth":{"state":"OFF"},"brand":"samsung","carrierName":"Telenor DK","displayDensity":640,"locale":"en_GB","manufacturer":"samsung","model":"SM-G950F","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":102400,"linkUpstreamBandwidthKbps":51200,"networkCapabilities":"NET_CAPABILITY_IMS,NET_CAPABILITY_NOT_METERED,NET_CAPABILITY_TRUSTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_VALIDATED,NET_CAPABILITY_NOT_ROAMING,NET_CAPABILITY_FOREGROUND,NET_CAPABILITY_NOT_CONGESTED,NET_CAPABILITY_NOT_SUSPENDED","signalStrength":-2147483648,"transportTypes":"TRANSPORT_CELLULAR"},"detailedState":"CONNECTED","extraInfo":"ims","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":13,"subtypeName":"LTE","type":0,"typeName":"MOBILE"},{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CA...
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell dumpsys window'
[AndroidDriver] Screen already unlocked, doing nothing
[AndroidDriver] Starting a chrome-based browser session
[debug] [AndroidDriver] A port was not given, using random free port: 8000
[debug] [AndroidDriver] Automated Chromedriver download is disabled. Use 'chromedriver_autodownload' server feature to enable it
[debug] [AndroidDriver] Precalculated Chromedriver capabilities: {
[debug] [AndroidDriver]   "androidPackage": "com.android.chrome",
[debug] [AndroidDriver]   "androidDeviceSerial": "DEVICE_UDID"
[debug] [AndroidDriver] }
[debug] [AndroidDriver] Before starting chromedriver, androidPackage is 'com.android.chrome'
[debug] [Chromedriver] Changed state to 'starting'
[Chromedriver] Set chromedriver binary as: chromedrivers/linux/chromedriver
[debug] [Chromedriver] Killing any old chromedrivers, running: pkill -15 -f "chromedrivers/linux/chromedriver.*--port=8000"
[Chromedriver] No old chromedrivers seem to exist
[debug] [Chromedriver] Cleaning this device's adb forwarded port socket connections: DEVICE_UDID
[debug] [ADB] List forwarding ports
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID forward --list'
[Chromedriver] Spawning chromedriver with: chromedrivers/linux/chromedriver --url-base=wd/hub --port=8000 --adb-port=5037 --verbose
[debug] [Chromedriver] Chromedriver version: '100.0.4896.60'
[debug] [Chromedriver] [STDOUT] Starting ChromeDriver 100.0.4896.60 (6a5d10861ce8de5fce22564658033b43cb7de047-refs/branch-heads/4896@{#875}) on port 8000
[debug] [Chromedriver] [STDOUT] Only local connections are allowed.
[debug] [Chromedriver] [STDOUT] Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
[debug] [WD Proxy] Matched '/status' to command name 'getStatus'
[debug] [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8000/wd/hub/status] with no body
[debug] [Chromedriver] [STDOUT] ChromeDriver was started successfully.
[Chromedriver] [STDERR] [1648835725.598][SEVERE]: bind() failed: Cannot assign requested address (99)
[Chromedriver] [STDERR] [1648835725.598][INFO]: listen on IPv6 failed with error ERR_ADDRESS_INVALID
[debug] [WD Proxy] Got response with status 200: {"value":{"build":{"version":"100.0.4896.60 (6a5d10861ce8de5fce22564658033b43cb7de047-refs/branch-heads/4896@{#875})"},"message":"ChromeDriver ready for new sessions.","os":{"arch":"x86_64","name":"Linux","version":"5.10.47-linuxkit"},"ready":true}}
[Chromedriver] Starting W3C Chromedriver session with capabilities: {
[Chromedriver]   "capabilities": {
[Chromedriver]     "alwaysMatch": {
[Chromedriver]       "goog:chromeOptions": {
[Chromedriver]         "androidPackage": "com.android.chrome",
[Chromedriver]         "androidDeviceSerial": "DEVICE_UDID"
[Chromedriver]       },
[Chromedriver]       "goog:loggingPrefs": {
[Chromedriver]         "browser": "ALL"
[Chromedriver]       }
[Chromedriver]     }
[Chromedriver]   }
[Chromedriver] }
[debug] [WD Proxy] Matched '/session' to command name 'createSession'
[debug] [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8000/wd/hub/session] with body: {"capabilities":{"alwaysMatch":{"goog:chromeOptions":{"androidPackage":"com.android.chrome","androidDeviceSerial":"DEVICE_UDID"},"goog:loggingPrefs":{"browser":"ALL"}}}}
[Chromedriver] [STDERR] [1648835725.645][INFO]: [5048f7269210af8a2a267854e4db3ec3] COMMAND InitSession {
[Chromedriver] [STDERR]    "capabilities": {
[Chromedriver] [STDERR]       "alwaysMatch": {
[Chromedriver] [STDERR]          "goog:chromeOptions": {
[Chromedriver] [STDERR]             "androidDeviceSerial": "DEVICE_UDID",
[Chromedriver] [STDERR]             "androidPackage": "com.android.chrome"
[Chromedriver] [STDERR]          },
[Chromedriver] [STDERR]          "goog:loggingPrefs": {
[Chromedriver] [STDERR]             "browser": "ALL"
[Chromedriver] [STDERR]          }
[Chromedriver] [STDERR]       }
[Chromedriver] [STDERR]    }
[Chromedriver] [STDERR] }
[Chromedriver] [STDERR] [1648835725.646][DEBUG]: Sending adb command: host:devices
[Chromedriver] [STDERR] [1648835725.649][INFO]: [5048f7269210af8a2a267854e4db3ec3] RESPONSE InitSession ERROR unknown error: Failed to run adb command with networking error: net::ERR_ADDRESS_INVALID. Is the adb server running? Extra response: <>.
[Chromedriver] [STDERR] [1648835725.650][DEBUG]: Log type 'driver' lost 0 entries on destruction
[Chromedriver] [STDERR] [1648835725.650][DEBUG]: Log type 'browser' lost 0 entries on destruction
[WD Proxy] Got response with status 500: {"value":{"error":"unknown error","message":"unknown error: Failed to run adb command with networking error: net::ERR_ADDRESS_INVALID. Is the adb server running? Extra response: <>.","stacktrace":"#0 0x559c09a93ad3 <unknown>\n#1 0x559c097f3568 <unknown>\n#2 0x559c097cd7e7 <unknown>\n#3 0x559c097cbfa4 <unknown>\n#4 0x559c097cb9fb <unknown>\n#5 0x559c097daef8 <unknown>\n#6 0x559c09812003 <unknown>\n#7 0x559c0984d2ba <unknown>\n#8 0x559c098474e3 <unknown>\n#9 0x559c0981cd1a <unknown>\n#10 0x559c0981de75 <unknown>\n#11 0x559c09ac1efd <unknown>\n#12 0x559c09adb19b <unknown>\n#13 0x559c09ac3c65 <unknown>\n#14 0x559c09adbec8 <unknown>\n#15 0x559c09ab7360 <unknown>\n#16 0x559c09af7a68 <unknown>\n#17 0x559c09af7be8 <unknown>\n#18 0x559c09b117fd <unknown>\n#19 0x7f26149da6db <unknown>\n"}}
[debug] [W3C] Matched W3C error code 'unknown error' to UnknownError
[debug] [Chromedriver] UnknownError: An unknown server-side error occurred while processing the command. Original error: unknown error: Failed to run adb command with networking error: net::ERR_ADDRESS_INVALID. Is the adb server running? Extra response: <>.
[debug] [Chromedriver]     at errorFromW3CJsonCode (/usr/lib/node_modules/appium/node_modules/appium-base-driver/lib/protocol/errors.js:780:25)
[debug] [Chromedriver]     at ProxyRequestError.getActualError (/usr/lib/node_modules/appium/node_modules/appium-base-driver/lib/protocol/errors.js:663:14)
[debug] [Chromedriver]     at JWProxy.command (/usr/lib/node_modules/appium/node_modules/appium-base-driver/lib/jsonwp-proxy/proxy.js:272:19)
[debug] [Chromedriver]     at processTicksAndRejections (internal/process/task_queues.js:97:5)
[Chromedriver] Chromedriver exited unexpectedly with code null, signal SIGTERM
[debug] [Chromedriver] Changed state to 'stopped'
[Chromedriver] An unknown server-side error occurred while processing the command. Original error: unknown error: Failed to run adb command with networking error: net::ERR_ADDRESS_INVALID. Is the adb server running? Extra response: <>.
[debug] [UiAutomator2] Deleting UiAutomator2 session
[debug] [UiAutomator2] Deleting UiAutomator2 server session
[debug] [WD Proxy] Matched '/' to command name 'deleteSession'
[debug] [WD Proxy] Proxying [DELETE /] to [DELETE http://gateway.docker.internal:8200/wd/hub/session/10d01d68-2db5-4a80-ad8a-e348a99cad8f] with no body
[debug] [WD Proxy] Got response with status 200: {"sessionId":"10d01d68-2db5-4a80-ad8a-e348a99cad8f","value":null}
[debug] [Logcat] Stopping logcat capture
[debug] [ADB] Removing forwarded port socket connection: 8200
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID forward --remove tcp:8200'
[UiAutomator2] Restoring hidden api policy to the device default configuration
[debug] [ADB] Running '/root/platform-tools/adb -H gateway.docker.internal -P 5037 -s DEVICE_UDID shell 'settings delete global hidden_api_policy_pre_p_apps;settings delete global hidden_api_policy_p_apps;settings delete global hidden_api_policy''
[debug] [BaseDriver] Event 'newSessionStarted' logged at 1648835726178 (10:55:26 GMT-0700 (Pacific Daylight Time))
[debug] [W3C] Encountered internal error running command: Error: An unknown server-side error occurred while processing the command. Original error: unknown error: Failed to run adb command with networking error: net::ERR_ADDRESS_INVALID. Is the adb server running? Extra response: <>.
[debug] [W3C]     at Object.errorAndThrow (/usr/lib/node_modules/appium/node_modules/appium-support/lib/logging.js:94:35)
[debug] [W3C]     at Chromedriver.start (/usr/lib/node_modules/appium/node_modules/appium-chromedriver/lib/chromedriver.js:541:11)
[debug] [W3C]     at AndroidUiautomator2Driver.setupNewChromedriver (/usr/lib/node_modules/appium/node_modules/appium-android-driver/lib/commands/context.js:472:3)
[debug] [W3C]     at AndroidUiautomator2Driver.startChromeSession (/usr/lib/node_modules/appium/node_modules/appium-android-driver/lib/commands/context.js:326:23)
[debug] [W3C]     at AndroidUiautomator2Driver.startUiAutomator2Session (/usr/lib/node_modules/appium/node_modules/appium-uiautomator2-driver/lib/driver.js:429:7)
[debug] [W3C]     at AndroidUiautomator2Driver.createSession (/usr/lib/node_modules/appium/node_modules/appium-uiautomator2-driver/lib/driver.js:229:7)
[debug] [W3C]     at AppiumDriver.createSession (/usr/lib/node_modules/appium/lib/appium.js:387:35)
[HTTP] <-- POST /wd/hub/session 500 11152 ms - 925
[HTTP]
[debug] [Instrumentation] .
[debug] [Instrumentation] Time: 3.173
[debug] [Instrumentation]
[debug] [Instrumentation] OK (1 test)
[debug] [Instrumentation] The process has exited with code 0
```