# conftest.py

import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions

from config import DEVICES, APP_PATH

@pytest.fixture(scope="function")
def driver(request):
    worker_index = int(request.config.workerinput["workerid"].replace("gw", ""))
    device = DEVICES[worker_index]

    options = XCUITestOptions()
    options.set_capability("platformName", "iOS")
    options.set_capability("deviceName", device["deviceName"])
    options.set_capability("platformVersion", device["platformVersion"])
    options.set_capability("automationName", "XCUITest")
    options.set_capability("app", APP_PATH)
    options.set_capability("wdaLocalPort", device["wdaLocalPort"])
    options.set_capability("noReset", True)

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    bundle_id = driver.capabilities.get("bundleId")  # Retrieve bundleId before quitting
    driver.quit()
    try:
        if bundle_id:
            driver.remove_app(bundle_id)
            print(f"🧼 App ({bundle_id}) removed after test")
        else:
            print("⚠️ 無法取得 bundleId，未移除 App")
    except Exception as e:
        print(f"⚠️ Failed to remove app: {e}")