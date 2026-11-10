import os, time, pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import config


def _options(browser=False):
    o = UiAutomator2Options()
    o.platform_name = "Android"
    o.automation_name = "UiAutomator2"
    o.udid = config.DEVICE
    o.new_command_timeout = 300
    if browser:
        o.browser_name = "Chrome"
        o.set_capability("appium:chromedriverAutodownload", True)
    elif config.APP_PATH:
        o.app = config.APP_PATH
    return o


@pytest.fixture
def web_driver():
    d = webdriver.Remote(config.APPIUM_URL, options=_options(browser=True))
    yield d
    d.quit()


@pytest.fixture
def native_driver():
    d = webdriver.Remote(config.APPIUM_URL, options=_options())
    yield d
    d.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    rep = (yield).get_result()
    if rep.when != "call":
        return
    drv = item.funcargs.get("web_driver") or item.funcargs.get("native_driver")
    if drv:
        name = f"{item.name}_{'PASS' if rep.passed else 'FAIL'}_{int(time.time())}.png"
        try:
            drv.save_screenshot(os.path.join(config.SHOTS_DIR, name))
        except Exception as e:  # never let a screenshot crash pytest
            print(f"screenshot failed: {str(e).splitlines()[0]}")
