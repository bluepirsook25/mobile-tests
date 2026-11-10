from appium.webdriver.common.appiumby import AppiumBy


def test_open_settings_about(native_driver):
    native_driver.activate_app("com.android.settings")
    el = native_driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().textContains("About"))',
    )
    el.click()
    assert native_driver.find_elements(AppiumBy.XPATH, '//*[contains(@text,"Android version") or contains(@text,"Model")]')
