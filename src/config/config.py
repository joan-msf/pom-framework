import os

CONFIG = {
    # Toggle for BrowserStack execution (True for remote, False for local)
    "USE_BROWSERSTACK": os.getenv("USE_BROWSERSTACK", "False") == "True",

    # BrowserStack credentials (to be provided)
    "BROWSERSTACK_USERNAME": os.getenv("BROWSERSTACK_USERNAME", "your_username"),
    "BROWSERSTACK_ACCESS_KEY": os.getenv("BROWSERSTACK_ACCESS_KEY", "your_access_key"),

    # Web capabilities for BrowserStack
    "BROWSER_NAME": os.getenv("BROWSER_NAME", "Chrome"),
    "BROWSER_VERSION": os.getenv("BROWSER_VERSION", "latest"),
    "OS": os.getenv("OS", "Mac OS"),
    "OS_VERSION": os.getenv("OS_VERSION", "14.6"),
    "TEST_NAME": os.getenv("TEST_NAME", "Sample Web Test"),

    # Mobile capabilities for BrowserStack
    "DEVICE_NAME": os.getenv("DEVICE_NAME", "Google Pixel 3"),
    "BROWSERSTACK_APP_ID": os.getenv("BROWSERSTACK_APP_ID", "bs://<app-id>"),
    "MOBILE_PLATFORM_NAME": os.getenv("MOBILE_PLATFORM_NAME", "Android"),

    # URL for Appium server (if needed in future for local mobile testing)
    "APPIUM_SERVER_URL": os.getenv("APPIUM_SERVER_URL", "http://localhost:4723/wd/hub"),

    # Base URL for the web application under test (to be set later)
    "BASE_URL": os.getenv("BASE_URL", "https://your-application-url.com"),
}