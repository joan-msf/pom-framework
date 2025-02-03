import os
from selenium import webdriver
from appium import webdriver as appium_webdriver
from src.config.config import CONFIG


class DriverFactory:
    @staticmethod
    def get_driver(platform: str):
        """
        Returns a driver instance based on the platform and configuration.
        For BrowserStack execution (USE_BROWSERSTACK True), it returns a remote driver.
        Otherwise, it returns a local driver.

        :param platform: 'web' or 'mobile'
        :return: WebDriver or Appium driver instance
        """
        if CONFIG['USE_BROWSERSTACK']:
            return DriverFactory._get_browserstack_driver(platform)
        else:
            return DriverFactory._get_local_driver(platform)

    @staticmethod
    def _get_browserstack_driver(platform: str):
        username = CONFIG['BROWSERSTACK_USERNAME']
        access_key = CONFIG['BROWSERSTACK_ACCESS_KEY']
        bs_url = f"http://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub"

        if platform.lower() == "web":
            desired_capabilities = {
                'browserName': CONFIG.get('BROWSER_NAME', 'Chrome'),
                'browserVersion': CONFIG.get('BROWSER_VERSION', 'latest'),
                'os': CONFIG.get('OS', 'Windows'),
                'osVersion': CONFIG.get('OS_VERSION', '10'),
                'name': CONFIG.get('TEST_NAME', 'Sample Web Test'),
                # Additional BrowserStack options can be added here.
            }
            return webdriver.Remote(command_executor=bs_url, desired_capabilities=desired_capabilities)

        elif platform.lower() == "mobile":
            desired_capabilities = {
                'device': CONFIG.get('DEVICE_NAME', 'Google Pixel 3'),
                'realMobile': 'true',
                'os_version': CONFIG.get('OS_VERSION', '9.0'),
                'app': CONFIG.get('BROWSERSTACK_APP_ID'),
                'name': CONFIG.get('TEST_NAME', 'Sample Mobile Test'),
                # Additional mobile capabilities can be added here.
            }
            return appium_webdriver.Remote(command_executor=bs_url, desired_capabilities=desired_capabilities)
        else:
            raise ValueError("Invalid platform specified. Use 'web' or 'mobile'.")

    @staticmethod
    def _get_local_driver(platform: str):
        if platform.lower() == "web":
            # Retrieve the desired browser from configuration.
            browser = CONFIG.get('BROWSER_NAME', 'chrome').lower()
            if browser == "chrome":
                options = webdriver.ChromeOptions()
                # You can add additional ChromeOptions here.
                return webdriver.Chrome(options=options)
            elif browser in ["firefox", "gecko"]:
                options = webdriver.FirefoxOptions()
                # You can add additional FirefoxOptions here.
                return webdriver.Firefox(options=options)
            elif browser == "safari":
                # Safari driver generally does not require options.
                return webdriver.Safari()
            elif browser == "edge":
                options = webdriver.EdgeOptions()
                # You can add additional EdgeOptions here.
                return webdriver.Edge(options=options)
            else:
                raise ValueError(f"Unsupported browser: {browser}")
        elif platform.lower() == "mobile":
            # Local mobile testing is not supported in the current implementation.
            raise NotImplementedError("Local mobile testing is not supported at this time.")
        else:
            raise ValueError("Invalid platform specified. Use 'web' or 'mobile'.")
