# tests/test_login.py

from appium.webdriver.common.appiumby import AppiumBy
import time

def test_profile_button(driver):
    time.sleep(3)
    login_btn = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="btn_profile")
    login_btn.click()
    time.sleep(1)
    assert True  # 實際可以驗證下一個頁面的元素

def test_profile_button_2(driver):
    time.sleep(3)
    login_btn = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="btn_profile")
    login_btn.click()
    time.sleep(1)
    assert True  # 實際可以驗證下一個頁面的元素

def test_profile_button_3(driver):
    time.sleep(3)
    login_btn = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="btn_profile")
    login_btn.click()
    time.sleep(1)
    assert True  # 實際可以驗證下一個頁面的元素

def test_profile_button_4(driver):
    time.sleep(3)
    login_btn = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="btn_profile")
    login_btn.click()
    time.sleep(1)
    assert True  # 實際可以驗證下一個頁面的元素