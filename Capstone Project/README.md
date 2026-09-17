# 🛒 E-Commerce Web Automation Framework

> 🚀 **Production-Style Selenium + Python + Pytest Automation Framework**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.48-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Test_Framework-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![POM](https://img.shields.io/badge/Design-Page%20Object%20Model-orange?style=for-the-badge)
![HTML Report](https://img.shields.io/badge/Reports-pytest--html-red?style=for-the-badge)

</p>

---

## 📌 Overview

This project is a **production-style E-Commerce Web Automation Framework** built using **Selenium + Python + Pytest**, following the **Page Object Model (POM)** design pattern.

The framework automates a complete E-Commerce testing journey on the **TutorialsNinja Demo Store**, covering:

- 🔐 Login & authentication
- 🔎 Product search
- 📦 Product selection
- 🛒 Add-to-cart operations
- ✅ Cart verification
- 🧹 Cart cleanup
- 🚪 Logout
- 📸 Automatic screenshot capture on test failure
- 📊 Self-contained HTML test reporting
- 📁 Data-driven testing using CSV files
- 📝 Timestamped execution logs

The framework is designed with **maintainability, reusability, scalability, and clean test architecture** in mind.

---

## 🎯 Project Objective

The primary objective of this project is to demonstrate how a real-world Selenium automation framework can be structured using reusable components instead of placing all browser interactions directly inside test scripts.

The framework separates:

- Test logic
- Page interactions
- Configuration
- Test data
- Utility functions
- Logging
- Reporting

This separation makes the automation suite easier to maintain, debug, and extend.

---

## 📽️ Demo Video

### ▶️ Watch the Automation Demo

[![Watch Demo](https://img.shields.io/badge/▶️-Watch%20Demo-red?style=for-the-badge)](https://drive.google.com/file/d/1OMIMN252cNt-MayT_2Ek_a7lBGshQLHm/view?usp=drive_link)

🎥 **[Click here to watch the full automation demo on Google Drive](https://drive.google.com/file/d/1OMIMN252cNt-MayT_2Ek_a7lBGshQLHm/view?usp=drive_link)**

The demo showcases the automated E-Commerce workflow, including login, product search, product selection, cart operations, and logout.

---

## 🧰 Tech Stack

| Technology | Purpose |
|:---|:---|
| 🐍 **Python 3.10.0** | Core programming language |
| 🌐 **Selenium 4.48.0** | Browser automation |
| 🧪 **Pytest** | Test execution and assertions |
| 📊 **pytest-html** | Self-contained HTML test reporting |
| 🚗 **WebDriver Manager** | Automatic browser driver management |
| 🧱 **Page Object Model** | Maintainable automation architecture |
| 📄 **CSV** | Data-driven test inputs |
| 📝 **Python Logging** | Runtime execution logs |
| 🧩 **Unittest** | Negative login test implementation |

---

## 🏗️ Framework Architecture

The framework follows a layered automation architecture:

```text
                         AUTOMATION FRAMEWORK
                                  │
                ┌─────────────────┴─────────────────┐
                │                                   │
           TEST LAYER                          DATA LAYER
                │                                   │
        ┌───────┴────────┐                  ┌───────┴────────┐
        │                │                  │                │
      Pytest          Unittest          CSV Data        config.ini
        │
        ▼
┌───────────────────────────────┐
│       PAGE OBJECT LAYER       │
├───────────────────────────────┤
│ Base Page                     │
│ Home Page                     │
│ Login Page                    │
│ Search Results Page           │
│ Product Page                  │
│ Cart Page                     │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│        UTILITY LAYER          │
├───────────────────────────────┤
│ Configuration Reader          │
│ Data Reader                   │
│ Custom Logger                 │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│       SELENIUM WEBDRIVER      │
├───────────────────────────────┤
│ Chrome                        │
│ Firefox                       │
└───────────────────────────────┘      
