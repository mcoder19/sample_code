# Log when executing `pytest test/test_android_create_web_session.py` in the docker setup

Passing the argument `--whitelisted-ips=""` to chromedriver should apparently whitelist all IP's, however, it does not work when provided as argument to appium's chromedriver wrapper.

## test_script_container

```bash
root@8689b25c3836:/code# pytest test/test_android_create_web_session.py
================================================================================================================ test session starts =================================================================================================================
platform linux -- Python 3.8.10, pytest-7.1.1, pluggy-1.0.0
rootdir: /code
collected 1 item

test/test_android_create_web_session.py

```

## appium_container 

Note: I have replaced the original identifier of the device with `DEVICE_UDID`.

```bash
root@886ee5a5eff6:~# appium
[Appium] Welcome to Appium v1.22.0
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
[debug] [HTTP] Request idempotency key: 36bd140c-0bb5-46f6-9ad0-44dc1ba92744
[HTTP] --> POST /wd/hub/session
[HTTP] {"capabilities":{"alwaysMatch":{"appium:chromedriverExecutable":"chromedrivers/linux/chromedriver","appium:automationName":"UIAutomator2","platformName":"Android","appium:deviceName":"device","appium:showChromedriverLog":true,"appium:remoteAdbHost":"gateway.docker.internal","appium:chromedriverArgs":["--whitelisted-ips=''"],"appium:name":"test_should_create_and_destroy_android_web_session","browserName":"Chrome"},"firstMatch":[{}]},"desiredCapabilities":{"chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","platformName":"Android","deviceName":"device","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","chromedriverArgs":["--whitelisted-ips=''"],"name":"test_should_create_and_destroy_android_web_session","browserName":"Chrome"}}
[debug] [W3C] Calling AppiumDriver.createSession() with args: [{"chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","platformName":"Android","deviceName":"device","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","chromedriverArgs":["--whitelisted-ips=''"],"name":"test_should_create_and_destroy_android_web_session","browserName":"Chrome"},null,{"alwaysMatch":{"appium:chromedriverExecutable":"chromedrivers/linux/chromedriver","appium:automationName":"UIAutomator2","platformName":"Android","appium:deviceName":"device","appium:showChromedriverLog":true,"appium:remoteAdbHost":"gateway.docker.internal","appium:chromedriverArgs":["--whitelisted-ips=''"],"appium:name":"test_should_create_and_destroy_android_web_session","browserName":"Chrome"},"firstMatch":[{}]}]
[debug] [BaseDriver] Event 'newSessionRequested' logged at 1648840596241 (12:16:36 GMT-0700 (Pacific Daylight Time))
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
[debug] [BaseDriver]     "appium:chromedriverArgs": [
[debug] [BaseDriver]       "--whitelisted-ips=''"
[debug] [BaseDriver]     ],
[debug] [BaseDriver]     "appium:name": "test_should_create_and_destroy_android_web_session"
[debug] [BaseDriver]   },
[debug] [BaseDriver]   "firstMatch": [
[debug] [BaseDriver]     {}
[debug] [BaseDriver]   ]
[debug] [BaseDriver] }
[BaseDriver] The following capabilities were provided, but are not recognized by Appium:
[BaseDriver]   name
[BaseDriver] Session created with session id: f1db1282-1965-4e46-86a3-1b1ea74902cc
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
[debug] [UiAutomator2] The initialization of the instrumentation process took 3304ms
[debug] [WD Proxy] Matched '/session' to command name 'createSession'
[debug] [WD Proxy] Proxying [POST /session] to [POST http://gateway.docker.internal:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","browserName":"Chrome","chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","deviceName":"device","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","chromedriverArgs":["--whitelisted-ips=''"],"name":"test_should_create_and_destroy_android_web_session"},"platformName":"Android","browserName":"Chrome","chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","deviceName":"DEVICE_UDID","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","chromedriverArgs":["--whitelisted-ips=''"],"name":"test_should_create_and_destroy_android_web_session","appPackage":"com.android.chrome","appActivity":"com.google.android.apps.chrome.Main","deviceUDID":"9...
[debug] [WD Proxy] Got response with status 200: {"sessionId":"05e649a8-8b73-4408-9729-ad532ca6bd7f","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","browserName":"Chrome","chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","deviceName":"device","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","chromedriverArgs":["--whitelisted-ips=''"],"name":"test_should_create_and_destroy_android_web_session"},"platformName":"Android","browserName":"Chrome","chromedriverExecutable":"chromedrivers/linux/chromedriver","automationName":"UIAutomator2","deviceName":"DEVICE_UDID","showChromedriverLog":true,"remoteAdbHost":"gateway.docker.internal","chromedriverArgs":["--whitelisted-ips=''"],"name":"test_should_create_and_destroy_android_web_session","appPackage":"com.android.chrome","appAct...
[WD Proxy] Determined the downstream protocol as 'W3C'
[debug] [WD Proxy] Proxying [GET /appium/device/info] to [GET http://gateway.docker.internal:8200/wd/hub/session/05e649a8-8b73-4408-9729-ad532ca6bd7f/appium/device/info] with no body
[debug] [WD Proxy] Got response with status 200: {"sessionId":"05e649a8-8b73-4408-9729-ad532ca6bd7f","value":{"androidId":"8e2f3e3b1d2a8f39","apiVersion":"28","bluetooth":{"state":"OFF"},"brand":"samsung","carrierName":"Telenor DK","displayDensity":640,"locale":"en_GB","manufacturer":"samsung","model":"SM-G950F","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":102400,"linkUpstreamBandwidthKbps":51200,"networkCapabilities":"NET_CAPABILITY_IMS,NET_CAPABILITY_NOT_METERED,NET_CAPABILITY_TRUSTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_VALIDATED,NET_CAPABILITY_NOT_ROAMING,NET_CAPABILITY_FOREGROUND,NET_CAPABILITY_NOT_CONGESTED,NET_CAPABILITY_NOT_SUSPENDED","signalStrength":-2147483648,"transportTypes":"TRANSPORT_CELLULAR"},"detailedState":"CONNECTED","extraInfo":"ims","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":13,"subtypeName":"LTE","type":0,"typeName":"MOBILE"},{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CA...
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
[Chromedriver] Spawning chromedriver with: chromedrivers/linux/chromedriver --url-base=wd/hub --port=8000 --adb-port=5037 --whitelisted-ips='' --verbose
[debug] [Chromedriver] [STDOUT] Invalid IP address ''. Exiting...
[Chromedriver] Chromedriver exited unexpectedly with code 1, signal null
[debug] [Chromedriver] Changed state to 'stopped'

```

