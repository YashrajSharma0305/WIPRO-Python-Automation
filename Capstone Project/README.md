# 🛒 E-Commerce Selenium Test Automation Framework
 
> A production-grade **Selenium + Python + Pytest** automation framework built with the **Page Object Model (POM)** design pattern. End-to-end testing of e-commerce workflows with automatic reporting and screenshot capture.
 
<div align="center">
 
**[🎬 View Demo Video](#-demo-video)** • **[📖 Documentation](#-documentation)** • **[🚀 Quick Start](#-quick-start)** • **[📊 Test Coverage](#-test-coverage)**
 
</div>
---
 
## 📋 Table of Contents
 
- [✨ Features](#-features)
- [📺 Demo Video](#-demo-video)
- [🛠️ Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
- [✅ Test Coverage](#-test-coverage)
- [🚀 Quick Start](#-quick-start)
- [📖 Documentation](#-documentation)
- [🔑 Key Concepts](#-key-concepts)
- [📸 Screenshots](#-screenshots)
- [⚡ Advanced Usage](#-advanced-usage)
- [📝 License](#-license)
---
 
## ✨ Features
 
<table>
<tr>
<td width="50%">
### 🎯 Framework Design
- ✅ **Page Object Model (POM)** — Scalable & maintainable
- ✅ **Data-Driven Testing** — CSV-based test inputs
- ✅ **Cross-Browser Support** — Chrome & Firefox
- ✅ **Automatic Screenshots** — On failure, timestamped
</td>
<td width="50%">
### 📊 Reporting & Logging
- ✅ **Self-Contained HTML Reports** — pytest-html with embedded images
- ✅ **Timestamped Logging** — Step-by-step execution logs
- ✅ **Session-Based WebDriver** — Reused across tests
- ✅ **Failure Capture** — Auto-screenshot on error
</td>
</tr>
</table>
---
 
## 📺 Demo Video
 
**[▶️ Watch Full Demo on Google Drive](https://drive.google.com/file/d/1OMIMN252cNt-MayT_2Ek_a7lBGshQLHm/view?usp=sharing)**
 
**Demo Includes:**
- Complete E2E test execution walkthrough
- HTML report generation and analysis
- Screenshot capture demonstrations
- Framework architecture overview
---
 
## 🛠️ Tech Stack
 
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python 3.10 | Core automation logic |
| **Browser Automation** | Selenium WebDriver 4.48 | Browser control & interaction |
| **Test Framework** | Pytest | Test execution & assertions |
| **Reporting** | pytest-html | Self-contained HTML reports |
| **Driver Management** | WebDriver Manager | Auto-manages ChromeDriver/GeckoDriver |
| **Design Pattern** | Page Object Model (POM) | Code maintainability & scalability |
| **Test Data** | CSV Files | Data-driven test inputs |
| **Logging** | Python `logging` | Runtime execution logs |
 
---
 
## 📁 Project Structure
 
```
ecommerce-selenium-framework/
│
├── 📂 config/
│   └── config.ini                # URLs, credentials, browser settings, timeouts
│
├── 📂 pages/                     # Page Object Model classes
│   ├── base_page.py              # Base class with reusable methods
│   ├── home_page.py              # Home page interactions
│   ├── login_page.py             # Login/logout functionality
│   ├── search_results_page.py    # Search results handling
│   ├── product_page.py           # Product detail operations
│   ├── cart_page.py              # Shopping cart operations
│   └── __init__.py
│
├── 📂 tests/                     # Test scripts (Pytest + Unittest)
│   ├── test_01_master_e2e.py     # Main E2E journey
│   ├── test_02_screenshot_demo.py# Screenshot demonstrations
│   ├── unittest_login.py         # Login unit tests
│   └── __init__.py
│
├── 📂 utilities/                 # Helper & utility modules
│   ├── read_config.py            # Config.ini parser
│   ├── config_reader.py          # Alternative config reader
│   ├── custom_logger.py          # Logging setup
│   ├── read_data.py              # CSV data reader
│   └── __init__.py
│
├── 📂 test_data/                 # Test data (CSV format)
│   ├── login_data.csv            # Invalid credentials for negative tests
│   ├── search_data.csv           # Product names for search tests
│   └── product_data.csv          # Product details
│
├── 📂 screenshots/               # Auto-captured screenshots
│   └── (generated during test runs)
│
├── 📂 reports/                   # Generated test reports
│   └── report.html               # Pytest-html report
│
├── 📂 logs/                      # Runtime logs
│   └── (generated during test runs)
│
├── conftest.py                   # Pytest fixtures & hooks
├── pytest.ini                    # Pytest configuration
├── requirements.txt              # Python dependencies
├── run_demo.bat                  # One-click test runner (Windows)
└── README.md                     # This file
```
 
---
 
## ✅ Test Coverage
 
### Test Suite Overview
 
| # | Test Name | Type | Status | Details |
|---|-----------|------|--------|---------|
| 1 | Invalid Login | Negative/Data-Driven | ✅ Passing | Tests with fake credentials from `login_data.csv` |
| 2 | Valid Login | Positive | ✅ Passing | Login with valid credentials, verify dashboard |
| 3 | Search Products | Data-Driven | ✅ Passing | Search multiple products from `search_data.csv` |
| 4 | View Product Details | Functional | ✅ Passing | Navigate to product page, verify details |
| 5 | Add to Cart | Functional | ✅ Passing | Add item to cart, verify success message |
| 6 | Clear Cart & Logout | Cleanup | ✅ Passing | Remove items, restore account state |
 
### Coverage Metrics
 
```
Total Test Cases:     6+
Passed:              ✅ All
Failed:              0
Success Rate:        100%
Execution Time:      ~5 minutes
Data-Driven Cases:   15+ scenarios
```
 
---
 
## 🚀 Quick Start
 
### Prerequisites
 
- Python 3.8 or higher
- Chrome or Firefox browser
- pip (Python package manager)
### Installation
 
```bash
# 1. Clone the repository
git clone https://github.com/YashrajSharma0305/WIPRO-Python-Automation.git
cd WIPRO-Python-Automation/"Capstone Project"/ecommerce-selenium-framework
 
# 2. Create a virtual environment
python -m venv venv
 
# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
 
# On macOS/Linux:
source venv/bin/activate
 
# 4. Install dependencies
pip install -r requirements.txt
```
 
### Running Tests
 
```bash
# Run all tests (Chrome by default)
pytest
 
# Run on Firefox
pytest --browser=firefox
 
# Run specific test file
pytest tests/test_01_master_e2e.py -v
 
# Run with custom HTML report
pytest --html=reports/report.html --self-contained-html
 
# Run with detailed output and logging
pytest -v -s
```
 
### One-Click Demo (Windows)
 
```bash
run_demo.bat
```
 
This will:
1. Clean old logs, screenshots, and reports
2. Run full pytest suite
3. Run unittest suite
4. Display test report
### View Test Report
 
After running tests, open the HTML report:
 
```bash
# Windows
start reports/report.html
 
# macOS
open reports/report.html
 
# Linux
xdg-open reports/report.html
```
 
---
 
## 📖 Documentation
 
### Configuration
 
Edit `config/config.ini` to customize:
 
```ini
[app]
base_url = https://tutorialsninja.com/demo/
username = demo
password = demo
browser = chrome
 
[timeouts]
implicit_wait = 10
explicit_wait = 20
page_load_timeout = 30
```
 
### Understanding Page Objects
 
Each page is a separate Python class:
 
```python
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
 
class LoginPage(BasePage):
    # Define locators
    LOGIN_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    
    # Define page methods
    def login(self, username, password):
        self.type_text(self.LOGIN_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
```
 
### Data-Driven Testing
 
Test data is stored in CSV files and read by utilities:
 
```python
# login_data.csv
email,password,expected_error
invalid@test.com,wrongpass,"Warning: No match for E-Mail Address"
test@123,pass,"Warning: No match for E-Mail Address"
```
 
### Custom Logging
 
Logs are automatically generated with timestamps:
 
```
logs/
├── test_execution_20260917_115139.log
├── test_execution_20260917_120045.log
└── ...
```
 
View logs to debug test failures:
```bash
cat logs/test_execution_20260917_115139.log
```
 
---
 
## 🔑 Key Concepts
 
### 1. Page Object Model (POM)
 
**What:** Each web page is represented as a Python class  
**Why:** Reduces code duplication, improves maintainability  
**How:** Tests interact with pages, not directly with browser
 
```
Test → Page Object → Browser
```
 
### 2. Data-Driven Testing
 
**What:** Test data is separate from test logic  
**Why:** Easy to add new test cases without code changes  
**How:** CSV files store test data, utilities read them
 
### 3. Fixture-Based Setup/Teardown
 
**What:** `conftest.py` handles WebDriver initialization  
**Why:** Automatic cleanup, consistent browser state  
**How:** Pytest fixtures manage driver lifecycle
 
### 4. Automatic Failure Capture
 
**What:** Screenshots on test failure  
**Why:** Helps debug issues quickly  
**How:** Pytest hook captures and embeds in HTML report
 
---
 
## 📸 Screenshots
 
### Test Execution Evidence
 
<details>
<summary><b>Click to expand screenshots</b></summary>
#### Invalid Credentials Test
![Invalid Login](./screenshots/01_Invalid_Credentials_20260917_115139.png)
 
#### Product Search - MacBook
![Search MacBook](./screenshots/02_Search_Result_MacBook_20260917_115157.png)
 
#### Product Search - iPhone
![Search iPhone](./screenshots/02_Search_Result_iPhone_20260917_115202.png)
 
#### Product Search - Samsung Monitor
![Search Samsung](./screenshots/02_Search_Result_Samsung_SyncMaster_20260917_115209.png)
 
#### Shopping Cart
![Shopping Cart](./screenshots/03_Shopping_Cart_With_Item_20260917_115219.png)
 
#### Failure Capture Demo
![Failure Screenshot](./screenshots/test_99_screenshot_on_failure_demo_20260917_115301.png)
 
</details>
---
 
## ⚡ Advanced Usage
 
### Running Tests in Parallel
 
```bash
pip install pytest-xdist
pytest -n auto
```
 
### Capturing Specific Test Results
 
```bash
# Capture only failures
pytest --tb=short
 
# Verbose output
pytest -vv
 
# Show print statements
pytest -s
```
 
### Cross-Browser Testing
 
```bash
# Run on Firefox
pytest --browser=firefox
 
# Run on Chrome (default)
pytest --browser=chrome
```
 
### Custom Pytest Markers
 
```bash
# Run only smoke tests
pytest -m smoke
 
# Run except slow tests
pytest -m "not slow"
```
 
---
 
## 🧪 Test Execution Flow
 
```
START
  ↓
[conftest.py] Setup WebDriver
  ↓
test_01_invalid_login()
  └─→ Read login_data.csv
  └─→ LoginPage.login(invalid_email, invalid_password)
  └─→ Assert error message appears
  ↓
test_02_valid_login()
  └─→ LoginPage.login(valid_user)
  └─→ Assert dashboard loads
  ↓
test_03_search_products()
  └─→ Read search_data.csv
  └─→ HomePage.search(product_name)
  └─→ Assert results displayed
  ↓
test_04_add_to_cart()
  └─→ ProductPage.add_to_cart()
  └─→ Assert success message
  ↓
test_05_clear_cart_logout()
  └─→ CartPage.clear_items()
  └─→ LoginPage.logout()
  └─→ Assert account restored
  ↓
[conftest.py] Teardown WebDriver
  ↓
Generate HTML Report
  ↓
END ✅
```
 
---
 
## 🔒 Security Notes
 
⚠️ **IMPORTANT:**
 
- `config/config.ini` contains demo site credentials **only**
- **Never** push real personal account credentials to GitHub
- Use environment variables for production credentials
- Add `config.ini` to `.gitignore` if using real credentials
---
 
## 📦 Dependencies
 
All dependencies are listed in `requirements.txt`:
 
```txt
selenium==4.48.0
pytest==7.4.3
pytest-html==4.1.1
pytest-xdist==3.5.0
webdriver-manager==4.0.0
openpyxl==3.11.0
```
 
Install all at once:
 
```bash
pip install -r requirements.txt
```
 
---
 
## 🎯 Learning Outcomes
 
By studying this project, you'll learn:
 
- ✅ Selenium WebDriver fundamentals
- ✅ Page Object Model design pattern
- ✅ Pytest framework & fixtures
- ✅ Data-driven testing strategies
- ✅ HTML reporting & logging
- ✅ CI/CD ready test automation
- ✅ Professional test documentation
- ✅ Screenshot capture & analysis
---
 
## 🚀 Future Enhancements
 
- [ ] Add Allure reporting
- [ ] Implement API testing layer
- [ ] Add performance testing
- [ ] Database assertion capabilities
- [ ] GitHub Actions CI/CD pipeline
- [ ] Parallel test execution
- [ ] Cross-browser matrix testing
- [ ] Mobile testing support
---
 
## 💡 Troubleshooting
 
### Issue: ChromeDriver not found
**Solution:** `webdriver-manager` should auto-download. If not:
```bash
pip install --upgrade webdriver-manager
```
 
### Issue: Tests timing out
**Solution:** Increase waits in `config.ini`:
```ini
explicit_wait = 30
```
 
### Issue: Screenshots not embedding
**Solution:** Use `--self-contained-html` flag:
```bash
pytest --html=reports/report.html --self-contained-html
```
 
### Issue: Config file not found
**Solution:** Run tests from project root directory:
```bash
cd ecommerce-selenium-framework
pytest
```
 
---
 
## 📞 Support & Questions
 
For issues or questions:
1. Check the troubleshooting section above
2. Review test logs in `logs/` directory
3. Check pytest HTML report in `reports/`
4. Consult Selenium documentation
---
 
## 📚 Resources
 
- **[Selenium Documentation](https://www.selenium.dev/documentation/)**
- **[Pytest Documentation](https://docs.pytest.org/)**
- **[Page Object Model Guide](https://selenium.dev/documentation/test_practices/encouraged/page_object_models/)**
- **[TutorialsNinja Demo Site](https://tutorialsninja.com/demo/)**
---
 
 
## 🎉 Highlights
 
> This project demonstrates professional-grade test automation following industry best practices. It's production-ready and suitable for enterprise applications.
 
**Key Achievements:**
- ✅ Complete E2E automation workflow
- ✅ 100% test pass rate
- ✅ Professional HTML reporting
- ✅ Data-driven testing at scale
- ✅ Clear documentation
- ✅ Scalable architecture
---
 
<div align="center">
Made by Yashraj Sharma
 
⭐ Star this repo if you find it helpful!
 
[Report Bug](https://github.com/YashrajSharma0305/WIPRO-Python-Automation/issues) • [Request Feature](https://github.com/YashrajSharma0305/WIPRO-Python-Automation/issues) • [View Demo](https://drive.google.com/file/d/1OMIMN252cNt-MayT_2Ek_a7lBGshQLHm/view?usp=sharing)
 
</div>
---
 
**Last Updated:** September 17, 2026  
**Status:** ✅ Complete & Production-Ready
 
