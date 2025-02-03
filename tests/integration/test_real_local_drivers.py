import pytest

from src.drivers.driver_factory import DriverFactory


@pytest.mark.integration
def test_local_chrome_integration(real_webdriver):
    """
    Integration test that instantiates a real local Chrome driver,
    navigates to a blank page, and verifies that the driver is working.

    Note: The unified real_webdriver fixture (defined in tests/conftest.py)
    ensures that:
      - BrowserStack is disabled (USE_BROWSERSTACK=False)
      - BROWSER_NAME defaults to "chrome" (if not set otherwise)
      - The driver is properly instantiated and quit after the test.
    """
    # Navigate to a simple blank page.
    real_webdriver.get("about:blank")

    # Validate that the navigation was successful.
    current_url = real_webdriver.current_url
    assert "about:blank" in current_url, f"Expected 'about:blank' in URL, got {current_url}"


@pytest.mark.integration
def test_local_chrome_integration(set_test_config):
    """
    Instantiates a real local Chrome driver, navigates to a blank page,
    and validates that the driver is working.
    """
    new_config = {
        "USE_BROWSERSTACK": False,
        "BROWSER_NAME": "chrome"
    }
    set_test_config(new_config)

    driver = DriverFactory.get_driver("web")
    try:
        driver.get("about:blank")
        current_url = driver.current_url
        # Verify that the browser navigated to "about:blank"
        assert "about:blank" in current_url
    finally:
        driver.quit()


@pytest.mark.integration
def test_local_firefox_integration(set_test_config):
    """
    Instantiates a real local Firefox driver, navigates to a blank page,
    and validates that the driver is working.
    """
    new_config = {
        "USE_BROWSERSTACK": False,
        "BROWSER_NAME": "firefox"
    }
    set_test_config(new_config)

    driver = DriverFactory.get_driver("web")
    try:
        driver.get("about:blank")
        current_url = driver.current_url
        # Verify that the browser navigated to "about:blank"
        assert "about:blank" in current_url
    finally:
        driver.quit()


@pytest.mark.integration
def test_local_safari_integration(set_test_config):
    """
    Instantiates a real local Safari driver, navigates to a blank page,
    and validates that the driver is working.
    """
    new_config = {
        "USE_BROWSERSTACK": False,
        "BROWSER_NAME": "safari"
    }
    set_test_config(new_config)

    driver = DriverFactory.get_driver("web")
    try:
        driver.get("about:blank")
        current_url = driver.current_url
        # Verify that the browser navigated to "about:blank"
        assert "about:blank" in current_url
    finally:
        driver.quit()


@pytest.mark.integration
def test_local_edge_integration(set_test_config):
    """
    Instantiates a real local Edge driver, navigates to a blank page,
    and validates that the driver is working.
    """
    new_config = {
        "USE_BROWSERSTACK": False,
        "BROWSER_NAME": "edge"
    }
    set_test_config(new_config)

    driver = DriverFactory.get_driver("web")
    try:
        driver.get("about:blank")
        current_url = driver.current_url
        # Verify that the browser navigated to "about:blank"
        assert "about:blank" in current_url
    finally:
        driver.quit()
