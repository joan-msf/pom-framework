import sys
import os
import logging
import pytest
from src.config.config import CONFIG
from src.drivers.driver_factory import DriverFactory

# Ensure the project root is in the Python path.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def setup_logging():
    """
    Configures the root logger to output logs to a centralized directory.
    Logs are written to reports/logs/automation.log and also output to the console.
    """
    log_dir = os.path.join(os.getcwd(), "reports", "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(os.path.join(log_dir, "automation.log")),
            logging.StreamHandler()
        ]
    )

# Setup logging once when tests are collected.
setup_logging()

@pytest.fixture
def set_test_config(monkeypatch):
    """
    Fixture to override values in the global CONFIG dictionary.
    Usage: call the returned function with a dictionary of new configuration values.
    """

    def _set_config(new_config: dict):
        for key, value in new_config.items():
            monkeypatch.setitem(CONFIG, key, value)

    return _set_config


@pytest.fixture(scope="function")
def real_webdriver(monkeypatch):
    """
    Fixture for integration tests requiring a real local webdriver.

    This fixture:
      - Forces local execution (USE_BROWSERSTACK=False)
      - Optionally sets a default BROWSER_NAME if not already specified.
      - Instantiates the driver via DriverFactory.get_driver("web").
      - Yields the driver for use in tests.
      - Ensures proper teardown by calling driver.quit() after the test.
    """
    monkeypatch.setitem(CONFIG, "USE_BROWSERSTACK", False)
    if "BROWSER_NAME" not in CONFIG or not CONFIG["BROWSER_NAME"]:
        monkeypatch.setitem(CONFIG, "BROWSER_NAME", "chrome")

    driver = DriverFactory.get_driver("web")
    yield driver
    driver.quit()
