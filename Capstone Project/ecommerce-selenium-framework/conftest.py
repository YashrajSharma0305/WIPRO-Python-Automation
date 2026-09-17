import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import os
import base64
from utilities.read_config import ReadConfig
from datetime import datetime
import time as _time


# ─────────────────────────────────────────────────────────────────────────────
# CLI option
# ─────────────────────────────────────────────────────────────────────────────
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store",
        default=ReadConfig.get_browser_name(),
        help="Browser to use: chrome or firefox"
    )


# ─────────────────────────────────────────────────────────────────────────────
# Session-scoped WebDriver fixture — ONE browser for ALL tests
# ─────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="session")
def setup(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(ReadConfig.get_implicit_wait())
    driver.maximize_window()
    yield driver
    _time.sleep(2)
    driver.quit()


# ─────────────────────────────────────────────────────────────────────────────
# Auto-inject driver into every pytest test class + demo pause between tests
# NOTE: unittest.TestCase subclasses are explicitly skipped — they manage
#       their own browser via setUpClass / tearDownClass.
@pytest.fixture(autouse=True)
def inject_driver_and_pause(request, setup):
    import unittest
    is_unittest_class = (
        request.cls is not None
        and issubclass(request.cls, unittest.TestCase)
    )
    # Only inject the session driver into pure pytest test classes
    if request.cls is not None and not is_unittest_class:
        request.cls.driver = setup
    yield
    if not is_unittest_class:
        _time.sleep(2)


# ─────────────────────────────────────────────────────────────────────────────
# Screenshot on failure — embedded as base64 so it works in self-contained HTML
# ─────────────────────────────────────────────────────────────────────────────
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    plugin = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report  = outcome.get_result()
    extras  = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = None

        if item.instance is not None and hasattr(item.instance, "driver"):
            driver = item.instance.driver
        # Fallback: get from fixture args
        elif "setup" in item.fixturenames:
            driver = item.funcargs.get("setup")

        if driver:
            try:
                screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
                os.makedirs(screenshot_dir, exist_ok=True)

                timestamp     = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name     = f"{item.name}_{timestamp}.png"
                screenshot_path = os.path.join(screenshot_dir, file_name)

                # Save to file
                driver.save_screenshot(screenshot_path)
                print(f"\n[SCREENSHOT] Saved: {screenshot_path}")

                if plugin:
                    with open(screenshot_path, "rb") as img_file:
                        encoded = base64.b64encode(img_file.read()).decode("utf-8")
                    html_img = (
                        f'<div style="margin-top:10px;">'
                        f'<p><b>Screenshot on Failure:</b></p>'
                        f'<img src="data:image/png;base64,{encoded}" '
                        f'style="width:600px;border:2px solid red;cursor:pointer;" '
                        f'onclick="window.open(this.src)" />'
                        f'</div>'
                    )
                    extras.append(plugin.extras.html(html_img))

            except Exception as e:
                print(f"[WARNING] Could not take screenshot: {e}")

    report.extras = extras
