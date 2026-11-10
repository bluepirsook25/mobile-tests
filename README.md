# Mobile tests (Appium + Android emulator)

## One-time setup (PowerShell)
1. Install Node.js LTS (20.19+) from nodejs.org
2. npm i -g appium
3. appium driver install uiautomator2
4. setx ANDROID_HOME "$env:LOCALAPPDATA\Android\Sdk"
5. setx JAVA_HOME "C:\Program Files\Android\Android Studio\jbr"
6. Close and reopen PowerShell
7. appium driver doctor uiautomator2   (fix anything red)

## Every run
1. Start emulator in Android Studio (Medium Phone API 37) and wait for home screen
2. adb devices                          -> should show emulator-5554
3. Terminal 1: appium --allow-insecure "*:chromedriver_autodownload"
4. Terminal 2 (this folder): .\run_mobile.ps1 -Url "https://your-site.com"

## Run one test
.\run_mobile.ps1 -Url "https://your-site.com" -Test test_mobile_web.py::test_open_url

## Output
- report.html          -> pass/fail report
- screenshots\         -> screenshot per test (PASS/FAIL in name)
