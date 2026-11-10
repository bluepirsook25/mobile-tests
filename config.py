import os

APPIUM_URL = os.getenv("APPIUM_URL", "http://127.0.0.1:4723")
DEVICE = os.getenv("DEVICE", "emulator-5554")
TEST_URL = os.getenv("TEST_URL", "https://example.com")
APP_PATH = os.getenv("APP_PATH", "")  # optional .apk for native app tests
SHOTS_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(SHOTS_DIR, exist_ok=True)
