#!/usr/bin/env python
# coding: utf-8

# # Amazon Web Scraping 

# In[9]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import smtplib
from urllib.request import urlopen as uReq
import numpy as np


# In[10]:


url = 'https://www.amazon.com.mx/s?k=arena+para+gato&crid=2NWX99119HVQ7&sprefix=%2Caps%2C113&ref=nb_sb_ss_recent_1_0_recent'
client = uReq(url)  # grabs the page
soup = BeautifulSoup(client.read(), 'html.parser')

print(soup.prettify())


# In[11]:


type(soup)


# **GETTING EVERY LINK**

# In[12]:


links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
links


# Get a individual link as reference to get data:

# In[13]:


links[0]


# Get all data of the link:

# In[14]:


link = links[0].get('href')


# In[15]:


product_list = 'https://www.amazon.com.mx' + link


# In[16]:


product_list


# Make the new page have a html format:

# In[17]:


new_client = uReq(product_list)  # grabs the page
new_soup = BeautifulSoup(new_client.read(), 'html.parser')
print(type(new_soup))
print(new_soup)


# In[18]:


new_soup


# **------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**

# **GETTING PRODUCT TITLE, PRICE, STAR RATINGS, REVIEWS AND AVAILABILITY**

# **Product:**

# In[19]:


titles = new_soup.find('span', id='productTitle')
for title in titles:
    print(title.text.strip())


# Function for all titles:

# In[20]:


def get_title(soup):
    try:
        titles = soup.find('span', id='productTitle')
        if titles:
            return titles.text.strip()
        else:
            return ""
    except AttributeError:
        return ""


# **Price:**

# In[21]:


price = new_soup.find('span', class_='a-offscreen')
for price_final in price:
    print(price_final.text.strip())


# Function for all titles:

# In[22]:


def get_price(soup):

    try:
        price = soup.find('span', class_='a-offscreen')
        if price:
            return price.text.strip()
        else:
            return ""
    except AttributeError:
        return ""


# **Ratings:**

# In[23]:


ratings = new_soup.find('span', class_='a-icon-alt')
for ratings_final in ratings:
    print(ratings_final.text.strip())


# Function for all titles:

# In[24]:


def get_rating(soup):

    try:
        ratings = soup.find('span', class_='a-icon-alt')
        if ratings:
            return ratings.text.strip()
        else:
            return ""
    except AttributeError:
        return ""


# **Number of reviews:**

# In[25]:


ratings_number = new_soup.find('span', id='acrCustomerReviewText')
for ratings_number_final in ratings_number:
    print(ratings_number_final.text.strip())


# Function for all titles:

# In[26]:


def get_review_count(soup):
    try:
        ratings_number = soup.find('span', id='acrCustomerReviewText').string.strip()

    except AttributeError:
        ratings_number = ""	

    return ratings_number


# **Availability:**

# In[27]:


availability = new_soup.find('div', id='availability')
if availability is not None:
    print(availability.text.strip())
else:
    print("Availability information not found.")


# Function for all titles:

# In[28]:


def get_availability(soup):
    try:
        availability = soup.find('div', id='availability')
        if availability is not None:
            available = availability.find("span").string.strip()
            return available
        else:
            return "Not Available"
    except AttributeError:
        return "Not Available"


# **------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**

# **RAW CODE TOGETHER**

# In[6]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import smtplib
from urllib.request import urlopen as uReq
import numpy as np

url = 'https://www.amazon.com.mx/s?k=arena+para+gato&crid=2NWX99119HVQ7&sprefix=%2Caps%2C113&ref=nb_sb_ss_recent_1_0_recent'
client = uReq(url)  # grabs the page
soup = BeautifulSoup(client.read(), 'html.parser')

links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

link = links[].get('href')
product_list = 'https://www.amazon.com.mx' + link

new_client = uReq(product_list)  # grabs the page
new_soup = BeautifulSoup(new_client.read(), 'html.parser')


def get_title(soup):
    try:
        titles = soup.find('span', id='productTitle')
        if titles:
            return titles.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_price(soup):

    try:
        price = soup.find('span', class_='a-offscreen')
        if price:
            return price.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_rating(soup):

    try:
        ratings = soup.find('span', class_='a-icon-alt')
        if ratings:
            return ratings.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_review_count(soup):
    try:
        ratings_number = soup.find('span', id='acrCustomerReviewText').string.strip()

    except AttributeError:
        ratings_number = ""	

    return ratings_number

def get_availability(soup):
    try:
        availability = soup.find('div', id='availability')
        if availability is not None:
            available = availability.find("span").string.strip()
            return available
        else:
            return "Not Available"
    except AttributeError:
        return "Not Available"


# **------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**

# **AUTOMATING FILE AND EXPORTING TO A CSV****

# In[7]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

def get_title(soup):
    try:
        titles = soup.find('span', id='productTitle')
        if titles:
            return titles.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_price(soup):
    try:
        price = soup.find('span', class_='a-offscreen')
        if price:
            return price.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_rating(soup):
    try:
        ratings = soup.find('span', class_='a-icon-alt')
        if ratings:
            return ratings.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_review_count(soup):
    try:
        ratings_number = soup.find('span', id='acrCustomerReviewText').string.strip()
        return ratings_number
    except AttributeError:
        return ""

def get_availability(soup):
    try:
        availability = soup.find('div', id='availability')
        if availability is not None:
            available = availability.find("span").string.strip()
            return available
        else:
            return "Not Available"
    except AttributeError:
        return "Not Available"

def scrape_product_info(product_url):
    try:
        html = urlopen(product_url)
        soup = BeautifulSoup(html, 'html.parser')
        
        title = get_title(soup)
        price = get_price(soup)
        rating = get_rating(soup)
        review_count = get_review_count(soup)
        availability = get_availability(soup)
        
        return {
            'Title': title,
            'Price': price,
            'Rating': rating,
            'Review Count': review_count,
            'Availability': availability
        }
    except Exception as e:
        print("Error occurred:", str(e))
        return None

def scrape_amazon_search_results(search_url):
    try:
        html = urlopen(search_url)
        soup = BeautifulSoup(html, 'html.parser')
        products = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        
        product_info_list = []
        for product in products:
            product_url = 'https://www.amazon.com.mx' + product.get('href')
            product_info = scrape_product_info(product_url)
            if product_info:
                product_info_list.append(product_info)
        
        return product_info_list
    except Exception as e:
        print("Error occurred:", str(e))
        return None

search_url = 'https://www.amazon.com.mx/s?k=arena+para+gato&crid=2NWX99119HVQ7&sprefix=%2Caps%2C113&ref=nb_sb_ss_recent_1_0_recent'
product_info_list = scrape_amazon_search_results(search_url)

if product_info_list:
    df = pd.DataFrame(product_info_list)
    print(df)
else:
    print("No se pudo extraer la información de los productos.")


# In[5]:


df


# In[ ]:





# In[8]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

def get_title(soup):
    try:
        titles = soup.find('span', id='productTitle')
        if titles:
            return titles.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_price(soup):
    try:
        price = soup.find('span', class_='a-offscreen')
        if price:
            return price.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_rating(soup):
    try:
        ratings = soup.find('span', class_='a-icon-alt')
        if ratings:
            return ratings.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_review_count(soup):
    try:
        ratings_number = soup.find('span', id='acrCustomerReviewText').string.strip()
        return ratings_number
    except AttributeError:
        return ""

def get_availability(soup):
    try:
        availability = soup.find('div', id='availability')
        if availability is not None:
            available = availability.find("span").string.strip()
            return available
        else:
            return "Not Available"
    except AttributeError:
        return "Not Available"

def scrape_product_info(product_url):
    try:
        html = urlopen(product_url)
        soup = BeautifulSoup(html, 'html.parser')
        
        title = get_title(soup)
        price = get_price(soup)
        rating = get_rating(soup)
        review_count = get_review_count(soup)
        availability = get_availability(soup)
        
        return {
            'Title': title,
            'Price': price,
            'Rating': rating,
            'Review Count': review_count,
            'Availability': availability
        }
    except Exception as e:
        print("Error occurred:", str(e))
        return None

def scrape_amazon_search_results(search_url):
    try:
        html = urlopen(search_url)
        soup = BeautifulSoup(html, 'html.parser')
        products = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        
        product_info_list = []
        for product in products:
            product_url = 'https://www.amazon.com.mx' + product.get('href')
            product_info = scrape_product_info(product_url)
            if product_info:
                product_info_list.append(product_info)
        
        return product_info_list
    except Exception as e:
        print("Error occurred:", str(e))
        return None

def save_to_csv(data, filename='amazon_products.csv'):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print("Data saved to", filename)
    except Exception as e:
        print("Error occurred while saving to CSV:", str(e))

def scrape_and_save(search_url):
    all_product_info = []
    page_number = 1
    
    while True:
        print("Scraping page", page_number)
        product_info_list = scrape_amazon_search_results(search_url)
        
        if product_info_list:
            all_product_info.extend(product_info_list)
            page_number += 1
            next_page_link = soup.find("a", {"class": "s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"})
            if next_page_link:
                search_url = 'https://www.amazon.com.mx' + next_page_link.get('href')
            else:
                break
        else:
            print("No se pudo extraer la información de los productos.")
            break
    
    if all_product_info:
        save_to_csv(all_product_info)

search_url = 'https://www.amazon.com.mx/s?k=arena+para+gato&crid=2NWX99119HVQ7&sprefix=%2Caps%2C113&ref=nb_sb_ss_recent_1_0_recent'
scrape_and_save(search_url)


# In[ ]:





# In[ ]:





# In[10]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import time
import random

def get_title(soup):
    try:
        titles = soup.find('span', id='productTitle')
        if titles:
            return titles.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_price(soup):
    try:
        price = soup.find('span', class_='a-offscreen')
        if price:
            return price.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_rating(soup):
    try:
        ratings = soup.find('span', class_='a-icon-alt')
        if ratings:
            return ratings.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_review_count(soup):
    try:
        ratings_number = soup.find('span', id='acrCustomerReviewText').string.strip()
        return ratings_number
    except AttributeError:
        return ""

def get_availability(soup):
    try:
        availability = soup.find('div', id='availability')
        if availability is not None:
            available = availability.find("span").string.strip()
            return available
        else:
            return "Not Available"
    except AttributeError:
        return "Not Available"

def scrape_product_info(product_url):
    try:
        html = urlopen(product_url)
        soup = BeautifulSoup(html, 'html.parser')
        
        title = get_title(soup)
        price = get_price(soup)
        rating = get_rating(soup)
        review_count = get_review_count(soup)
        availability = get_availability(soup)
        
        return {
            'Title': title,
            'Price': price,
            'Rating': rating,
            'Review Count': review_count,
            'Availability': availability
        }
    except Exception as e:
        print("Error occurred:", str(e))
        return None

def scrape_amazon_search_results(search_url):
    try:
        html = urlopen(search_url)
        soup = BeautifulSoup(html, 'html.parser')
        products = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        
        product_info_list = []
        for product in products:
            product_url = 'https://www.amazon.com.mx' + product.get('href')
            product_info = scrape_product_info(product_url)
            if product_info:
                product_info_list.append(product_info)
            # Introduce un retraso aleatorio entre 1 y 10 segundos
            time.sleep(random.uniform(1, 10))
        
        return product_info_list
    except Exception as e:
        print("Error occurred:", str(e))
        return None

def save_to_csv(data, filename='amazon_products.csv'):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print("Data saved to", filename)
    except Exception as e:
        print("Error occurred while saving to CSV:", str(e))

def scrape_and_save(search_url):
    all_product_info = []
    page_number = 1
    
    while True:
        print("Scraping page", page_number)
        product_info_list = scrape_amazon_search_results(search_url)
        
        if product_info_list:
            all_product_info.extend(product_info_list)
            page_number += 1
            next_page_link = soup.find("a", {"class": "s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"})
            if next_page_link:
                search_url = 'https://www.amazon.com.mx' + next_page_link.get('href')
            else:
                break
        else:
            print("No se pudo extraer la información de los productos.")
            break
    
    if all_product_info:
        save_to_csv(all_product_info)

search_url = 'https://www.amazon.com.mx/s?k=arena+para+gato&crid=2NWX99119HVQ7&sprefix=%2Caps%2C113&ref=nb_sb_ss_recent_1_0_recent'
scrape_and_save(search_url)


# **------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**

# **AUTOMATING FILE FOR ALL PAGES AND EXPORTING TO A CSV**

# In[12]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import time
import random

def get_title(soup):
    try:
        titles = soup.find('span', id='productTitle')
        if titles:
            return titles.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_price(soup):
    try:
        price = soup.find('span', class_='a-offscreen')
        if price:
            return price.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_rating(soup):
    try:
        ratings = soup.find('span', class_='a-icon-alt')
        if ratings:
            return ratings.text.strip()
        else:
            return ""
    except AttributeError:
        return ""

def get_review_count(soup):
    try:
        ratings_number = soup.find('span', id='acrCustomerReviewText').string.strip()
        return ratings_number
    except AttributeError:
        return ""

def get_availability(soup):
    try:
        availability = soup.find('div', id='availability')
        if availability is not None:
            available = availability.find("span").string.strip()
            return available
        else:
            return "Not Available"
    except AttributeError:
        return "Not Available"

def scrape_product_info(product_url):
    try:
        html = urlopen(product_url)
        soup = BeautifulSoup(html, 'html.parser')
        
        title = get_title(soup)
        price = get_price(soup)
        rating = get_rating(soup)
        review_count = get_review_count(soup)
        availability = get_availability(soup)
        
        return {
            'Title': title,
            'Price': price,
            'Rating': rating,
            'Review Count': review_count,
            'Availability': availability
        }
    except Exception as e:
        print("Error occurred:", str(e))
        return None

def scrape_amazon_search_results(search_url):
    try:
        html = urlopen(search_url)
        soup = BeautifulSoup(html, 'html.parser')
        products = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        
        product_info_list = []
        for product in products:
            product_url = 'https://www.amazon.com.mx' + product.get('href')
            product_info = scrape_product_info(product_url)
            if product_info:
                product_info_list.append(product_info)
            # Introduce un retraso aleatorio entre 1 y 10 segundos
            time.sleep(random.uniform(1, 10))
        
        return product_info_list
    except Exception as e:
        print("Error occurred:", str(e))
        return None

def getnextpage(soup):
    # this will return the next page URL
    pages = soup.find('ul', {'class': 'a-pagination'})
    if not pages.find('li', {'class': 'a-disabled a-last'}):
        url = 'https://www.amazon.com.mx' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return None

def scrape_and_save(search_url):
    all_product_info = []
    url = search_url
    
    while True:
        print("Scraping page:", url)
        product_info_list = scrape_amazon_search_results(url)
        
        if product_info_list:
            all_product_info.extend(product_info_list)
            next_page_url = getnextpage(BeautifulSoup(urlopen(url), 'html.parser'))
            if next_page_url:
                url = next_page_url
            else:
                break
        else:
            print("No se pudo extraer la información de los productos.")
            break
    
    if all_product_info:
        save_to_csv(all_product_info)

def save_to_csv(data, filename='amazon_products.csv'):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print("Data saved to", filename)
    except Exception as e:
        print("Error occurred while saving to CSV:", str(e))

search_url = 'https://www.amazon.com.mx/s?k=arena+para+gato&crid=2NWX99119HVQ7&sprefix=%2Caps%2C113&ref=nb_sb_ss_recent_1_0_recent'
scrape_and_save(search_url)


# In[ ]:




