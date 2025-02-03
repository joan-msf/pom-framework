import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.utils.logger import get_logger  # Assuming a logger utility is implemented


class BasePage:
    """
    BasePage encapsulates common Selenium actions and interactions.
    It provides methods for element location, clicking, typing, scrolling,
    taking screenshots, and other frequent web operations.
    """

    def __init__(self, driver, timeout=10):
        """
        Initialize with a Selenium WebDriver instance and an optional default timeout.
        """
        self.driver = driver
        self.timeout = timeout
        self.logger = get_logger(self.__class__.__name__)

    def find_element(self, locator, timeout=None):
        """
        Wait until the element is present in the DOM and return it.

        :param locator: Tuple (By.<METHOD>, "value")
        :param timeout: Optional custom timeout
        :return: WebElement
        """
        timeout = timeout or self.timeout
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            self.logger.info(f"Element found: {locator}")
            return element
        except TimeoutException as te:
            self.logger.error(f"Timeout waiting for element: {locator}")
            raise te

    def find_elements(self, locator, timeout=None):
        """
        Wait until all elements matching the locator are present and return them as a list.

        :param locator: Tuple (By.<METHOD>, "value")
        :param timeout: Optional custom timeout
        :return: List of WebElements
        """
        timeout = timeout or self.timeout
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            self.logger.info(f"Found {len(elements)} elements: {locator}")
            return elements
        except TimeoutException as te:
            self.logger.error(f"Timeout waiting for elements: {locator}")
            raise te

    def click(self, locator, timeout=None):
        """
        Wait for the element to be clickable, then click it.

        :param locator: Tuple (By.<METHOD>, "value")
        :param timeout: Optional custom timeout
        """
        timeout = timeout or self.timeout
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            self.logger.info(f"Clicked element: {locator}")
        except TimeoutException as te:
            self.logger.error(f"Timeout waiting to click element: {locator}")
            raise te

    def enter_text(self, locator, text, timeout=None):
        """
        Wait for the element, clear any pre-existing text, and then enter the specified text.

        :param locator: Tuple (By.<METHOD>, "value")
        :param text: Text to input
        :param timeout: Optional custom timeout
        """
        timeout = timeout or self.timeout
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        self.logger.info(f"Entered text into element {locator}: '{text}'")

    def get_text(self, locator, timeout=None):
        """
        Retrieve and return the text of the specified element.

        :param locator: Tuple (By.<METHOD>, "value")
        :param timeout: Optional custom timeout
        :return: Text content of the element
        """
        element = self.find_element(locator, timeout)
        text = element.text
        self.logger.info(f"Retrieved text from {locator}: '{text}'")
        return text

    def is_element_displayed(self, locator, timeout=None):
        """
        Check if the element is visible on the page.

        :param locator: Tuple (By.<METHOD>, "value")
        :param timeout: Optional custom timeout
        :return: True if visible, False otherwise
        """
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.logger.info(f"Element is visible: {locator}")
            return True
        except TimeoutException:
            self.logger.warning(f"Element is not visible: {locator}")
            return False

    def wait_for_element_to_disappear(self, locator, timeout=None):
        """
        Wait until the element is no longer visible on the page.

        :param locator: Tuple (By.<METHOD>, "value")
        :param timeout: Optional custom timeout
        :return: True if the element disappears, raises TimeoutException otherwise
        """
        timeout = timeout or self.timeout
        try:
            result = WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            self.logger.info(f"Element disappeared: {locator}")
            return result
        except TimeoutException as te:
            self.logger.error(f"Element did not disappear: {locator}")
            raise te

    def take_screenshot(self, file_name=None):
        """
        Take a screenshot of the current window and save it.

        :param file_name: Optional file name; if not provided, a timestamp-based name is generated.
        :return: The path to the screenshot file.
        """
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file_name = file_name or f"screenshot_{timestamp}.png"
        screenshot_path = f"reports/screenshots/{file_name}"
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Screenshot saved: {screenshot_path}")
        return screenshot_path

    def scroll_to_element(self, locator, timeout=None):
        """
        Scroll the browser window until the specified element is in view.

        :param locator: Tuple (By.<METHOD>, "value")
        :param timeout: Optional custom timeout
        """
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.logger.info(f"Scrolled to element: {locator}")

    def get_title(self):
        """
        Retrieve the title of the current page.

        :return: The page title as a string.
        """
        title = self.driver.title
        self.logger.info(f"Page title: {title}")
        return title

    def refresh_page(self):
        """
        Refresh the current page.
        """
        self.driver.refresh()
        self.logger.info("Page refreshed.")

    def navigate_to(self, url):
        """
        Navigate the browser to the specified URL.

        :param url: The target URL.
        """
        self.driver.get(url)
        self.logger.info(f"Navigated to URL: {url}")
