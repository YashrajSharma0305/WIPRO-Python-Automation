🛒 E-Commerce Web Automation Framework
A production-style Selenium + Python + Pytest automation framework built on the Page Object Model (POM) design pattern. This project automates an end-to-end E-Commerce testing journey on TutorialsNinja Demo — covering login, product search, cart management, and logout — with data-driven testing, automatic screenshot capture, and a self-contained HTML report.
---
📽️ Demo Video
> Add your video link here — e.g., `[▶ Watch Demo on Google Drive](your-link-here)`
---
🧰 Tech Stack
Tool	Purpose
Python 3.x	Core programming language
Selenium 4	Browser automation
Pytest	Test runner and assertions
pytest-html	Self-contained HTML test report
WebDriver Manager	Auto-manages ChromeDriver / GeckoDriver
Page Object Model	Design pattern for maintainability
CSV	Data-driven test inputs
Python `logging`	Runtime log generation
---
📁 Project Structure
```
ecommerce-selenium-framework/
│
├── config/
│   └── config.ini            # Base URL, browser settings, credentials, timeouts
│
├── pages/                    # Page Object classes (one per web page)
│   ├── base_page.py          # Common reusable methods (click, type, screenshot)
│   ├── home_page.py          # Search functionality
│   ├── login_page.py         # Login / Logout actions
│   ├── search_results_page.py
│   ├── product_page.py       # Add to cart, success message
│   └── cart_page.py          # Cart verification and cleanup
│
├── tests/                    # Test scripts
│   ├── test_01_master_e2e.py # Main E2E journey (Pytest)
│   ├── test_02_screenshot_demo.py
│   └── unittest_login.py     # Negative login (unittest)
│
├── utilities/                # Helper modules
│   ├── read_config.py        # Reads config.ini values
│   ├── config_reader.py
│   ├── custom_logger.py      # Generates timestamped log files
│   └── read_data.py          # Reads CSV test data files
│
├── test_data/                # Data-driven test inputs
│   ├── login_data.csv        # Invalid credentials for negative login test
│   └── search_data.csv       # Product names for search test
│
├── screenshots/              # Auto-captured screenshots (manual + on-failure)
├── reports/                  # Generated pytest-html report
├── logs/                     # Runtime log files
│
├── conftest.py               # Pytest fixtures (WebDriver setup, teardown, failure screenshot)
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Python dependencies
└── run_demo.bat              # One-click demo runner (Windows)
```
---
✅ Test Cases
#	Test Name	Type	Description
1	`test_01_invalid_login`	Negative / Data-Driven	Attempts login with fake credentials from `login_data.csv`, asserts warning message
2	`test_02_valid_login`	Positive	Logs in with valid credentials from `config.ini`, verifies "My Account" page
3	`test_03_search_and_view_product`	Data-Driven	Searches for multiple products from `search_data.csv`, navigates to MacBook details
4	`test_04_add_to_cart`	Functional	Adds MacBook to cart, waits for success banner, verifies item appears in cart
5	`test_05_clear_cart_and_logout`	Cleanup	Removes all cart items, then logs out to restore account state
6	Screenshot on Failure	Automated Hook	Embeds a base64 screenshot into the HTML report whenever any test fails
---
🚀 How to Run
1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Run all tests (Chrome by default)
```bash
pytest
```
3. Run on Firefox
```bash
pytest --browser=firefox
```
4. One-click demo (Windows)
```bat
run_demo.bat
```
This cleans old logs/screenshots/reports, runs the full Pytest suite, then runs the Unittest suite.
5. View the HTML Report
After running, open `reports/report.html` in any browser. The report is fully self-contained with embedded screenshots on failures.
---
🔑 Key Features
Page Object Model — Each web page is a separate Python class. Tests never talk to the browser directly, only through page objects.
Data-Driven Testing — Login credentials and product search terms are read from CSV files, keeping test logic and test data separate.
Automatic Screenshot on Failure — A pytest hook (`conftest.py`) captures and embeds a screenshot directly into the HTML report whenever a test fails.
Session-Scoped Driver — One browser window is reused across all tests in sequence, just like a real user would navigate.
Cross-Browser Support — Switch between Chrome and Firefox using the `--browser` flag.
Centralized Configuration — All URLs, credentials, and timeouts live in `config/config.ini`. No hardcoded values in test code.
Timestamped Logging — Every run generates a new log file under `logs/` with step-by-step info messages.
---
📦 Dependencies
```
selenium
pytest
pytest-html
pytest-xdist
webdriver-manager
openpyxl
```
Install all at once:
```bash
pip install -r requirements.txt
```
---
⚠️ Note
`config/config.ini` contains login credentials used for testing on the demo site. Do not replace these with real personal account credentials before pushing to a public repository.
