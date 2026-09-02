# Selenium E2E Test — ProtoCommerce Shopping Cart

An automated end-to-end test built with **Python**, **Selenium WebDriver**, and **pytest**, validating the full purchase flow on [ProtoCommerce](https://qaclickacademy.github.io/protocommerce/), a demo e-commerce site built for test automation practice.

> **Note:** This is earlier practice work built while learning Selenium and pytest fundamentals. Currently focused on Cypress — see [qa-automation-portfolio](https://github.com/UmerJadoon04/Cypress-QA-Automation) for current work.

## Overview

This test automates a complete customer purchase journey: browsing products, selecting a specific item, proceeding to checkout, entering shipping country, accepting terms and conditions, completing the purchase, and verifying the success confirmation message.

The project uses a fluent Page Object Model, where each page action returns the next page object in the flow — allowing the test to read as a natural sequence of user steps rather than a flat list of driver commands.

## Tech Stack

- **Python**
- **Selenium WebDriver**
- **pytest** — test runner and fixture management
- **webdriver-manager** — automatic browser driver management (no manual driver downloads required)
- **pytest-html** — HTML test reports with automatic screenshot capture on failure

## Project Structure

```
├── pageobjects/
│   ├── HomePage.py
│   ├── checkout.py
│   └── confirmOrder.py
├── utilities/
│   └── BaseClass.py
└── test_e2e.py
```

## Design Patterns Used

- **Fluent Page Object Model:** each page object method that navigates to a new page returns the corresponding page object for that page (e.g. `homepage.shopitems()` returns the checkout page), allowing test steps to chain naturally.
- **pytest fixtures:** browser setup and teardown are handled via a class-scoped `setup` fixture, supporting configurable browser selection via a `--browser_name` command-line option (Chrome or Edge).
- **Automatic failure screenshots:** a custom pytest hook captures a screenshot whenever a test fails and embeds it directly into the HTML report.

## Prerequisites

- Python 3.8 or higher
- pip

## Installation

```bash
git clone https://github.com/UmerJadoon04/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
pip install -r requirements.txt
```

*(If a `requirements.txt` isn't present yet, install directly: `pip install selenium pytest webdriver-manager pytest-html`)*

## Running Tests

```bash
pytest --html=report.html
```

**Run with a specific browser:**
```bash
pytest --browser_name=edge --html=report.html
```

## Test Results

After running, the HTML report (`report.html`) will be generated in the project directory, including embedded screenshots for any failed test steps.

## Author

**Umer Ayaz Jadoon**
QA Manual and Automation

---

*This project is part of an ongoing QA automation learning journey. See current work in Cypress at [qa-automation-portfolio](https://github.com/UmerJadoon04/Cypress-QA-Automation).*
The run report will be available after performing the run in the  "tests" folder.


