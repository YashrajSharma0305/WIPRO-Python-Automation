# 🧪 Course Demonstrations

### Hands-On Selenium, PyTest, Behave & Robot Framework Practice — WIPRO Python Automation Course

This folder contains all daily practice code, lab assignments, and framework
experiments completed during the **WIPRO Pre-Placement Python Automation
Program (CoE)**, spanning raw Selenium fundamentals through to Page Object
Model design, data-driven testing, BDD with Behave, and keyword-driven
testing with Robot Framework.

It is organised into two folders:

| Folder | Contents |
|---|---|
| 📂 [`Course Work/`](./Course%20Work) | Daily lesson scripts — WebDriver fundamentals through advanced interactions |
| 📂 [`Assignments/`](./Assignments) | Structured lab assignments — locators, waits, POM, PyTest, Behave BDD, Robot Framework |

---

## 📂 Course Work

Script-by-script practice covering core Selenium WebDriver mechanics, recorded
as part of the course's daily demonstration videos.

| # | Script | Topic |
|---|---|---|
| 1 | `test.py` | Basic WebDriver initialization and page title check |
| 2 | `webdrivermanager.py` | Automatic ChromeDriver/GeckoDriver management, multi-browser setup |
| 3 | `listofelements.py` | Locating elements by `LINK_TEXT` |
| 4 | `germanyclicking.py` | Autocomplete / type-ahead field handling |
| 5 | `radiobutton.py` | Radio button selection |
| 6 | `checkbox.py` | Multiple checkbox selection |
| 7 | `dropdown.py` | Dropdown handling via the `Select` class |
| 8 | `automate.py` | Full form automation — text fields, radio, checkbox, dropdown, explicit waits |
| 9 | `keyboard_actions.py` | Keyboard input with `ActionChains` and verification |
| 10 | `copy_msg.py` | Keyboard shortcuts (Ctrl+A / Ctrl+C / Ctrl+V) via `ActionChains` |
| 11 | `drag_and_drop.py` | Drag-and-drop interactions |
| 12 | `popup.py` | JavaScript `alert()` handling |
| 13 | `scroll&click_About.py` | Scrolling with `execute_script()` and clicking footer links |
| 14 | `select_mobiles.py` | Mouse hover, submenu navigation with `ActionChains` |

---

## 📂 Assignments

Nine core lab assignments demonstrating specific Selenium competencies, plus
three framework extensions built on top of them.

### Core Assignments (1–9)

| # | Assignment | Key Concept |
|---|---|---|
| 1 | Multi-Locator Challenge | `By.ID` + `By.NAME` + `By.XPATH` in one flow, URL assertion |
| 2 | Synchronization & Explicit Waits | `WebDriverWait` + `expected_conditions`, zero `time.sleep()` |
| 3 | Dynamic Dropdowns & Checkboxes | `.is_selected()` verification, autocomplete search loop |
| 4 | JavaScript Alerts and Confirms | Alert accept / Confirm dismiss / Prompt `send_keys()` |
| 5 | HTML Web Table Extractor | Row/column parsing, search-by-name extraction |
| 6 | Windows, Tabs, and IFrames | `switch_to.frame()`, `window_handles`, multi-tab management |
| 7 | *(Page Object Model — see below)* | |
| 8 | Data-Driven Automation (DDT) | `pandas`-driven login loop over external CSV data |
| 9 | *(PyTest + HTML Reporting — see below)* | |

> Note: several assignments exist in two forms in this folder — an earlier,
> simpler first-pass script, and a more thorough, verified version (with
> docstrings, `try/except` handling, and confirmed live locators). Both are
> kept intentionally to show iteration.

### Assignment 7 — Page Object Model (`pages/`, `pom/`)

Restructures the Assignment 1 login flow into the POM design pattern:

pages/
├── login_page.py # Locators + UI actions only — no assertions
└── inventory_page.py # Locators + UI actions only — no assertions


All test assertions live separately in `tests/test_login.py`.

### Assignment 9 — PyTest Integration with HTML Reporting (`tests/`, `pytest_suite/`)

conftest.py # driver fixture (setup/teardown) + screenshot-on-failure hook
pytest.ini # PyTest configuration
tests/test_login.py # Assertions only, built on the Assignment 7 Page Objects
reports/report.html # Self-contained HTML report, generated on each run


Run with:
```bash
pytest --html=reports/report.html --self-contained-html -v
```

### Behave BDD Framework (`behave/`)

Three Gherkin-driven scenarios mirroring the core assignments, using
step definitions and Page Objects:

behave/
├── features/
│ ├── assignment1_login.feature # Login scenario in Gherkin
│ ├── assignment2_data_driven.feature # Data-driven scenario
│ ├── assignment3_pom.feature # POM-based scenario
│ ├── environment.py # Behave hooks (before/after)
│ └── steps/ # Step definitions
├── pages/ # Page Objects shared across features
└── test_data/login_data.csv


Run with:
```bash
behave features/
```

### Robot Framework (`robot/`)

Seven `.robot` test suites covering the full Robot Framework syllabus —
basic syntax, variables/data-driven testing, custom keywords, assertions,
setup/teardown, tags, and HTML reporting:

robot/
├── 01_basic_syntax.robot
├── 02_variables_data_driven.robot
├── 03_custom_keywords.robot
├── 04_assertions_api.robot
├── 05_setup_teardown.robot
├── 06_tags.robot
├── 07_reports.robot
├── libraries/custom_library.py # Custom Python keyword library
└── test_data/login_data.csv


Run with:
```bash
robot --outputdir results robot/
```

---

## 🧰 Tech Stack

| Technology | Purpose |
|:---|:---|
| 🐍 **Python 3.10** | Core scripting language |
| 🌐 **Selenium WebDriver** | Browser automation engine |
| 🚗 **webdriver-manager** | Automatic ChromeDriver/GeckoDriver version matching |
| 🧪 **PyTest** | Fixtures, assertions, test execution |
| 📊 **pytest-html** | Self-contained HTML reports with embedded failure screenshots |
| 🥒 **Behave** | BDD framework using Gherkin syntax |
| 🤖 **Robot Framework** | Keyword-driven test automation |
| 📄 **pandas** | External CSV test-data handling for data-driven tests |

---

## ▶️ How to Run

```bash
# Install dependencies
pip install selenium webdriver-manager pytest pytest-html behave robotframework robotframework-seleniumlibrary pandas

# Run a single assignment script
python "Assignments/Assignment 1.py"

# Run the PyTest suite with HTML report
cd Assignments
pytest --html=reports/report.html --self-contained-html -v

# Run the Behave BDD suite
cd Assignments/behave
behave features/

# Run a Robot Framework suite
cd Assignments/robot
robot 01_basic_syntax.robot
```

---

<p align="center">
Made by Yashraj Sharma
</p>
<p align="center">
  Give a ⭐ if you find this repository useful
</p>
