# Amazon_product_analysis

Ani Tovmasyan
Nune Tadevosyan

# Amazon Product Data Scraping Script

## Overview
This script is designed for scraping product data from Amazon's "Best Sellers in Computers and Accessories" section. It automates navigating through Amazon pages, handling lazy loading, extracting product details, and saving the data into a CSV file.

## Features
- **Automated Navigation**: Manages page navigation on Amazon's Best Sellers section.
- **Lazy Loading Resolution**: Scrolls through web pages to ensure all products are loaded.
- **Data Extraction**: Collects information such as product name, brand, price, size, star rating, number of ratings, and more.
- **Data Storage**: Structures the extracted data into a Pandas DataFrame and exports it to a CSV file.

## Prerequisites
- Python 3.x
- Python Libraries: `pandas`, `beautifulsoup4`, `selenium`, `webdriver_manager`
- ChromeDriver (compatible with your installed version of Chrome)

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the required Python libraries using pip:
```shell
pip install pandas beautifulsoup4 selenium webdriver_manager
```
3. ChromeDriver will be managed automatically by the `webdriver_manager`.

## Usage
Run the script in a Python environment. It navigates through specified Amazon pages, extracts product data, and saves it in a CSV file named 'amazon_best_sellers.csv'.

## Script Functions
- `delay()`: Implements random delays to prevent anti-scraping detection.
- `lazy_loading()`: Scrolls down the webpage to load products that are loaded dynamically.
- `fetch_product_links_and_ranks()`: Gathers links to individual product pages and their rankings.
- `extract_` functions: Extract specific details from each product page.
- Iterates over a set number of pages (default is 2) to collect data.

## CSV Data Columns
- Product URL
- Ranking
- Brand
- Product Name
- Number of Ratings
- Size
- Star Rating
- Price (in USD)
- Color
- Hardware Interface
- Compatible Devices
- Connectivity Technology
- Connector Type
- Data Transfer Rate
- Mounting Type
- Special Features
- Date First Available

## Disclaimer
This script is intended for educational purposes.
