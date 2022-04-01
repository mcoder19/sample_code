# Python Sample Code

This repo is a modification of [the python code in the official appium sample-code](https://github.com/appium/appium/tree/master/sample-code) using [the provided .apk](https://github.com/appium/appium/blob/master/sample-code/apps/ApiDemos-debug.apk).

## General setup

```
pip install -r requirements.txt
```

## About

### Environment 

|               **Variable**            |    **Value**    |
|:-------------------------------------:|-----------------|
| Appium version                        |      1.22.1     |
| Node.js version                       |      v17.5.0    |
| Npm or Yarn package manager           |       npm       |
| Appium CLI or Appium.app              |    Appium CLI   |
| Mobile platform/version under test    |     Android     |
| Real device or emulator/simulator     |    Real device  |
| Desktop OS/version used to run Appium |     MacOS       |
| Chromedriver version                  |       100       |

Additional comments:
- All "variables" refers to the local environment not running in docker. 
- Device runs chromedriver version 100.
- Chromedriver download link: [https://chromedriver.storage.googleapis.com/index.html?path=100.0.4896.60/](https://chromedriver.storage.googleapis.com/index.html?path=100.0.4896.60/)
    - Ensure a compatible chromedriver is placed in the respective folders: 
        - `chromedriver/mac` (local execution on MacOS without docker) 
        - `chromedriver/linux` (execution in docker).

#### About the docker image 

[appium.yml](appium.yml) is a small wrapper around this docker image: [https://hub.docker.com/r/appium/appium/dockerfile](https://hub.docker.com/r/appium/appium/dockerfile)

These are the values inside the docker environment:

|               **Variable**            |    **Value**    |
|:-------------------------------------:|-----------------|
| Appium version                        |     v1.22.0     |
| Node.js version                       |     v12.22.6    |
| Npm or Yarn package manager           |       npm       |
| Docker Desktop version                | Version 4.0.0 (4.0.0.12) |


## Run tests
Remark: Ensure the device is unlocked. 

### Run all tests

```
py.test test
```


### Run an arbitrary file

```
py.test test/test_ios_selectors.py
```

## TestCase
### unittest based
- test/test_android_create_session.py
- test/test_ios_create_session.py

### pytest based
- Rest of the above


# Docker setup

Ensure the flag `IS_DOCKER` is set to true inside [test/helpers.py](test/helpers.py).

- Note: If you don't want to run the tests in docker, set this flag to false. 

## Ensure a host connected to devices is setup before running anything and that the ip address of this host is used 
Connecting `adb` in the appium docker container to `adb` on the host.
- Post providing a way to do this: [How can I deploy and execute an application on a device connected to a remote system?](https://stackoverflow.com/questions/27245597/how-can-i-deploy-and-execute-an-application-on-a-device-connected-to-a-remote-sy)

### Start `adb` server locally on MacOS

On MacOS host

    adb -a -P 5037 nodaemon server

The idea is that the `adb` instance in the appium container connects to this `adb` server instead of starting its own.

It may be practical to perform a `adb kill-server` before the above command. 

## Create network for the docker containers

    docker network create mobile_test_network


## Test script container

Build image from root dir of the source code (parent dir of the dockerfile directoy): 

    docker build -t test_scripts:v0.1 -f Dockerfile .


Enter a container of the image in bash:

    docker run -it --rm --name test_script_container --network mobile_test_network test_scripts:v0.1 /bin/bash


## Appium container

Build image

    docker build -t appium/appium -f appium.yml .

Run container

    docker run -it --rm --name appium_container --network mobile_test_network appium/appium /bin/bash


# Status

## Not running in docker

|              **Test**             | **Can execute sucessfully** |
|:---------------------------------:|-----------------------------|
| `test_android_create_session`     |             YES             |
| `test_android_basic_interactions` |             YES             |
| `test_android_selectors`          |             YES             |
| `test_android_create_web_session` |             YES             |



## Running in docker 

|              **Test**             | **Can execute sucessfully** |
|:---------------------------------:|-----------------------------|
| `test_android_create_session`     |             YES             |
| `test_android_basic_interactions` |             YES             |
| `test_android_selectors`          |             YES             |
| `test_android_create_web_session` |              NO             |

