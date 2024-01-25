# Importing libraries
import os
import time
import random
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
pd.options.mode.chained_assignment = None
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class AmazonScraper:
    def __init__(self):
        # Creating a dictionary of the required columns
        self.data_dict = {'product name': [], 'brand': [], 'date first available':[], 'ranking': [], 'number of ratings': [], 
                    'star rating': [], 'price(in dollar)': [], 'color': [], 'compatible devices': [], 'connectivity technology': [], 
                    'connector type': [], 'date first available':[], 'product url': []}
        self.data = pd.DataFrame(self.data_dict)

    # Scrolling down the page in order to overcome Lazy Loading
    def lazy_loading(self):
        element = driver.find_element(By.TAG_NAME, 'body')
        count = 0
        while count < 20:
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(random.randint(3, 10))
            count += 1
    
    # Function to fetch the product links of products
    def fetch_product_links_and_ranks(self):
        content = driver.page_source
        homepage_soup = BeautifulSoup(content, 'html.parser')
    
        all_products = homepage_soup.find('div', attrs={"class": "p13n-desktop-grid"})
        for product_section in all_products.find_all('div', {'id': 'gridItemRoot'}):
            for product_link in product_section.find_all('a',{'tabindex':'-1'}):
                if product_link['href'].startswith('https:'):
                    product_links.append(product_link['href'])
                else:
                    product_links.append('https://www.amazon.com' + product_link['href'])
            self.data_dict['ranking'].append(product_section.find('span',{'class': 'zg-bdg-text'}).text)
    
    
    # Function to extract content of the page
    def extract_content(self):
        driver.get(self.product_url)
        page_content = driver.page_source
        product_soup = BeautifulSoup(page_content, 'html.parser')
        return product_soup
    
    # Function to extract product name
    def extract_product_name(self):
        try:
            name_of_product = self.soup.find('div', attrs={"id": "titleSection"}).text.strip()
            self.data['product name'].iloc[product] = name_of_product
    
        except:
            name_of_product = 'Product name not available '
            self.data['product name'].iloc[product] = name_of_product
    
    # Function to extract brand name
    def extract_brand(self):
        try:
            brand = self.product_content.find('a', attrs={"id": "bylineInfo"}).text.split(':')[1].strip()  #one location where brand data could be found
            self.data['brand'].iloc[product] = brand
    
        except:
            if self.soup.find_all('tr', attrs={'class': 'a-spacing-small po-brand'}):  #other location where brand data could be found
                brand = self.product_content.find_all('tr', attrs={'class': 'a-spacing-small po-brand'})[0].text.strip().split(' ')[-1]
                self.data['brand'].iloc[product] = brand
            else:
                brand = 'Brand data not available'
                data['brand'].iloc[product] = brand
    
    # Function to extract price
    def extract_price(self):
        try:
            price = self.product_content.find('span', attrs={"class": "a-price a-text-price a-size-medium apexPriceToPay"}).text.split('$')[-1]
            self.data['price(in dollar)'].iloc[product] = price
    
        except:
            price = 'Price data not available'
            self.data['price(in dollar)'].iloc[product] = price
    
    # Function to extract star rating
    def extract_star_rating(self):
        try:
            star = None
            for star_rating_locations in ['a-icon a-icon-star a-star-4-5', 'a-icon a-icon-star a-star-5']:
                stars = self.product_content.find_all('i', attrs={"class": star_rating_locations})
                for i in range(len(stars)):
                    star = stars[i].text.split(' ')[0]
                    if star:
                        break
                if star:
                    break
            
        except:
            star = 'Star rating data not available'
            
        self.data['star rating'].iloc[product] = star   
    
    
    # Function to extract number of ratings
    def extract_num_of_ratings(self):
        try:
            star = self.product_content.find('span', attrs={"id": "acrCustomerReviewText"}).text.split(' ')[0]
            self.data['number of ratings'].iloc[product] = star
    
        except:
            star = 'Number of rating not available'
            self.data['number of ratings'].iloc[product] = star
    
    # Function to extract color
    def extract_color(self):
        try:
            color = self.product_content.find('tr', attrs={'class': 'a-spacing-small po-color'}).text.strip().split('  ')[1].strip()
            self.data['color'].iloc[product] = color
    
        except:
            color = 'Color not available'
            self.data['color'].iloc[product] = color
            
    
    # Function to extract compatible devices
    def extract_compatible_devices(self):
        try:
            compatible_devices = self.product_content.find('tr', attrs={"class": "a-spacing-small po-compatible_devices"}).text.strip().split('  ')[1].strip()
            self.data['compatible devices'].iloc[product] = compatible_devices
    
        except:
            compatible_devices = 'Compatible devices data not available'
            self.data['compatible devices'].iloc[product] = compatible_devices
            
    
    # Function to extract connectivity technology
    def extract_connectivity_technology(self):
        try:
            connectivity_technology = self.product_content.find('tr', attrs={"class": "a-spacing-small po-connectivity_technology"}).text.strip().split('  ')[
                1].strip()
            self.data['connectivity technology'].iloc[product] = connectivity_technology
    
        except:
            connectivity_technology = 'Connectivity technology data not available'
            self.data['connectivity technology'].iloc[product] = connectivity_technology
    
    # Function to extract connector type
    def extract_connector_type(self):
        try:
            connector_type = self.product_content.find('tr', attrs={"class": "a-spacing-small po-connector_type"}).text.strip().split('  ')[
                1].strip()
            self.data['connector type'].iloc[product] = connector_type
    
        except:
            connector_type = 'Connector type data not available'
            self.data['connector type'].iloc[product] = connector_type
    
    
    # Function to extract date first available
    def extract_date_first_available(self):
        try:
            product_details_keys = self.product_content.find_all('th', attrs={"class": "a-color-secondary a-size-base prodDetSectionEntry"})
            product_details_values = self.product_content.find_all('td', attrs={"class": "a-size-base prodDetAttrValue"})
            for detail_key in range(len(product_details_keys)):
                if 'Date First Available' in product_details_keys[detail_key].text:
                    date_first_available = product_details_values[detail_key - 2].text
                    if '20' not in date_first_available:
                        date_first_available = product_details_values[detail_key].text
            self.data['date first available'].iloc[product] = date_first_available
    
        except:
            date_first_available = 'Date first available data not available'
            self.data['date first available'].iloc[product] = date_first_available

    def __call__(self, url='https://www.amazon.com/Best-Sellers-Computers-Accessories/zgbs/pc/', pages=3, save_path='amazon_best_sellers.csv'):

        # Fetching the product links of all items
        for page in range(1,pages):               # to iterate over the 2 pages in which the products are divided into
            start_url = os.path.join(url, f'ref=zg_bs_pg_{page}?_encoding=UTF8&pg={page}')
            driver.get(start_url)
            self.lazy_loading()                     
            self.fetch_product_links_and_ranks()     
     
        # Assigning the scraped links and rankings to the columns 'product url' and 'ranking'
        self.data['product url'] = product_links
        self.data['ranking'] = ranking

        for product in range(len(self.data)):
            self.product_url = self.data['product url'].iloc[product]
            self.product_content = self.extract_content()
            self.extract_brand()
            self.extract_product_name()
            self.extract_price()
            self.extract_star_rating()
            self.extract_num_of_ratings()
            self.extract_color()
            self.extract_compatible_devices()
            self.extract_connectivity_technology()
            self.extract_connector_type()
            self.extract_date_first_available()

        # saving the resultant data frame as a csv file
        data.to_csv(save_path)



if __name__=='__main__':
    scraper = AmazonScraper()
    scraper()
