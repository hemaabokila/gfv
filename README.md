# URL Vulnerability Checker

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Overview

**URL Vulnerability Checker** is a powerful and customized tool for analyzing and scanning URLs to detect known patterns that indicate potential security vulnerabilities. This tool helps cybersecurity professionals quickly identify URLs that might contain vulnerabilities such as **SQL Injection**, **Cross-Site Scripting (XSS)**, and other common attacks by matching URLs against specific patterns stored in a JSON file.

## Features

- **Pattern Matching**: The tool supports scanning URLs against a set of patterns that can be customized and modified in the `patterns.json` file.
- **Easy-to-Use CLI Interface**: The tool provides a simple command-line interface for inputting and scanning URL files easily.
- **Fast Performance**: The tool quickly and accurately scans multiple URLs.
- **Flexibility**: You can customize the patterns by modifying the `patterns.json` file according to your needs.
- **Color-Coded Output**: The tool uses the `colorama` library to display results in colors for easy readability.

## Installation

To install the tool on your system, follow these steps:

1. Clone the repository from GitHub:

    ```bash
    git clone https://github.com/hemaabokila/gfv.git
    ```

2. Navigate to the cloned folder:

    ```bash
    cd gfv
    ```


4. Install the tool:

    ```bash
    sudo pip install .
    ```

## Usage

To run the tool, you can use it from the command line as follows:

```bash
gfv /path/to/urlfile.txt
```
## Options
- url: The path to a file containing the URLs you want to check.
## Example:
```
gfv urls_to_check.txt
```
## Customizing Patterns
You can customize the patterns that the URLs are checked against by modifying the `patterns/patterns.json` file. This file contains a set of default patterns that cover a wide range of common attacks.

### Example `patterns.json` file:
```
json

{
    "patterns": [
        "select * from",
        "<script>",
        "UNION SELECT",
        "' OR '1'='1"
    ]
}
```
You can add more patterns to this file as needed.

## Output
The tool prints URLs that match the specified patterns from the `patterns.json` file. The matching URLs are displayed in color to make it easier to read.

## Example Output:
```
Checking URLs Form: urls_to_check.txt
http://example.com/?search=<script>alert(1)</script>
http://example.com/?id=1 UNION SELECT username, password FROM users
```

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Author
This tool was developed by **Ibrahem abo kila.**
## Contact
* **ibrahemabokila@gmail.com**.