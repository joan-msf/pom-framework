import pytest
from unittest.mock import MagicMock, patch
from src.pages.base_page import BasePage
from src.utils.logger import get_logger


class DummyDriver:
    """
    A simple dummy driver to simulate a Selenium WebDriver.
    """

    def __init__(self):
        self.title = "Dummy Title"

    def save_screenshot(self, file_name):
        return file_name


def test_get_title():
    """
    Verify that BasePage.get_title() returns the correct title.
    """
    logger = get_logger("test_get_title")
    logger.info("Starting test_get_title")

    dummy_driver = DummyDriver()
    base_page = BasePage(dummy_driver)

    title = base_page.get_title()
    logger.info("Retrieved title: %s", title)

    assert title == "Dummy Title"


def test_find_element_success():
    """
    Verify that BasePage.find_element() returns the element when found.
    """
    logger = get_logger("test_find_element_success")
    dummy_driver = DummyDriver()
    base_page = BasePage(dummy_driver)
    fake_element = MagicMock(name="FakeElement")

    # Patch WebDriverWait to simulate waiting for element presence.
    with patch("src.pages.base_page.WebDriverWait") as MockWebDriverWait:
        instance = MockWebDriverWait.return_value
        instance.until.return_value = fake_element

        locator = ("id", "sample")
        element = base_page.find_element(locator)
        logger.info("Element found for locator %s", locator)

        assert element == fake_element
        instance.until.assert_called_once()


def test_click_method():
    """
    Verify that BasePage.click() waits for an element and clicks it.
    """
    logger = get_logger("test_click_method")
    dummy_driver = DummyDriver()
    base_page = BasePage(dummy_driver)
    fake_element = MagicMock(name="FakeClickableElement")

    # Patch WebDriverWait to simulate waiting until the element is clickable.
    with patch("src.pages.base_page.WebDriverWait") as MockWebDriverWait:
        instance = MockWebDriverWait.return_value
        instance.until.return_value = fake_element

        locator = ("id", "clickable")
        base_page.click(locator)
        logger.info("Click method executed for locator %s", locator)

        fake_element.click.assert_called_once()
