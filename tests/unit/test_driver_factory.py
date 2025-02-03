import pytest
from unittest.mock import MagicMock
from src.drivers.driver_factory import DriverFactory
from src.utils.logger import get_logger


def test_local_chrome_driver(set_test_config, monkeypatch):
    logger = get_logger("test_local_chrome_driver")
    logger.info("Starting test: Local Chrome driver instantiation.")

    # Set configuration for local Chrome testing.
    new_config = {
        "USE_BROWSERSTACK": False,
        "BROWSER_NAME": "chrome"
    }
    set_test_config(new_config)

    # Patch webdriver.Chrome to return a dummy driver.
    dummy_driver = MagicMock(name="LocalChromeDriver")
    monkeypatch.setattr(
        "src.drivers.driver_factory.webdriver.Chrome",
        lambda options=None: dummy_driver
    )

    # Instantiate the driver via DriverFactory.
    driver = DriverFactory.get_driver("web")
    logger.info("Instantiated driver: %s", driver)
    assert driver == dummy_driver

    # Teardown: Quit the driver and verify quit() was called.
    driver.quit()
    dummy_driver.quit.assert_called_once()
    logger.info("Local Chrome driver test passed.")


def test_local_firefox_driver(set_test_config, monkeypatch):
    logger = get_logger("test_local_firefox_driver")
    logger.info("Starting test: Local Firefox driver instantiation.")

    # Set configuration for local Firefox testing.
    new_config = {
        "USE_BROWSERSTACK": False,
        "BROWSER_NAME": "firefox"
    }
    set_test_config(new_config)

    # Patch webdriver.Firefox to return a dummy driver.
    dummy_driver = MagicMock(name="LocalFirefoxDriver")
    monkeypatch.setattr(
        "src.drivers.driver_factory.webdriver.Firefox",
        lambda options=None: dummy_driver
    )

    # Instantiate the driver.
    driver = DriverFactory.get_driver("web")
    logger.info("Instantiated driver: %s", driver)
    assert driver == dummy_driver

    # Teardown: Quit and verify.
    driver.quit()
    dummy_driver.quit.assert_called_once()
    logger.info("Local Firefox driver test passed.")


def test_local_safari_driver(set_test_config, monkeypatch):
    logger = get_logger("test_local_safari_driver")
    logger.info("Starting test: Local Safari driver instantiation.")

    # Set configuration for local Safari testing.
    new_config = {
        "USE_BROWSERSTACK": False,
        "BROWSER_NAME": "safari"
    }
    set_test_config(new_config)

    # Patch webdriver.Safari to return a dummy driver.
    dummy_driver = MagicMock(name="LocalSafariDriver")
    monkeypatch.setattr(
        "src.drivers.driver_factory.webdriver.Safari",
        lambda: dummy_driver
    )

    # Instantiate the driver.
    driver = DriverFactory.get_driver("web")
    logger.info("Instantiated driver: %s", driver)
    assert driver == dummy_driver

    # Teardown: Quit and verify.
    driver.quit()
    dummy_driver.quit.assert_called_once()
    logger.info("Local Safari driver test passed.")


def test_local_edge_driver(set_test_config, monkeypatch):
    logger = get_logger("test_local_edge_driver")
    logger.info("Starting test: Local Edge driver instantiation.")

    # Set configuration for local Edge testing.
    new_config = {
        "USE_BROWSERSTACK": False,
        "BROWSER_NAME": "edge"
    }
    set_test_config(new_config)

    # Patch webdriver.Edge to return a dummy driver.
    dummy_driver = MagicMock(name="LocalEdgeDriver")
    monkeypatch.setattr(
        "src.drivers.driver_factory.webdriver.Edge",
        lambda options=None: dummy_driver
    )

    # Instantiate the driver.
    driver = DriverFactory.get_driver("web")
    logger.info("Instantiated driver: %s", driver)
    assert driver == dummy_driver

    # Teardown: Quit and verify.
    driver.quit()
    dummy_driver.quit.assert_called_once()
    logger.info("Local Edge driver test passed.")


def test_invalid_platform(set_test_config):
    logger = get_logger("test_invalid_platform")
    logger.info("Starting test: Invalid platform should raise ValueError.")

    # Set configuration for local execution.
    new_config = {"USE_BROWSERSTACK": False}
    set_test_config(new_config)

    with pytest.raises(ValueError) as excinfo:
        DriverFactory.get_driver("invalid")
    logger.info("Expected exception received: %s", excinfo.value)
    logger.info("Invalid platform test passed.")
