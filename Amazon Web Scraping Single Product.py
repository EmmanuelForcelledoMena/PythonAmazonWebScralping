#!/usr/bin/env python
# coding: utf-8

# # Amazon Web Scraping 

# In[65]:


from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[66]:


from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

url = 'https://www.amazon.com.mx/Arena-para-gato-Scoop-Away/dp/B0161N7FE8/ref=sr_1_1?crid=366OSD0U9UQ73&dib=eyJ2IjoiMSJ9.eLudzn-54K8uVvzpEdryhRHzB_6VrLLt_j_Zv9R1A0b09b0riYHqFJpptzZy6GojxefpdvvhTpzEcMpWEKyD7oxuvdzAU__sUJ4iUekFGr9y3ytwG_5HO5pAFjVOHIUwzBC4bE13ffGa3wLq3XNuVVXqAA9d7zaJnn9XXnYn3j11gdl-ETFZCr1WPFWHpxLx1MnTX3sQE7oz9pfooKEc3vHoWsG71ERkXmbpRXQz_NYuPmwSu9S-vudzoqEDm5_R2xXaNEZRG27hMi6HJHNNaPqBzphbIx75GnkHd95jMyg.GG-YPSb2L8GdfuYwILj2l8nvVujhQ-0BLls1M72LHME&dib_tag=se&keywords=arena+para+gato&qid=1711554429&sprefix=%2Caps%2C2450&sr=8-1&ufe=app_do%3Aamzn1.fos.4e545b5e-1d45-498b-8193-a253464ffa47'
client = uReq(url)  # grabs the page
soup = BeautifulSoup(client.read(), 'html.parser')

print(soup.prettify())


# **GETTING PRODUCT TITLE AND PRICE**

# Product:

# In[67]:


title = soup.find_all('span', id='productTitle')
print(title)


# In[68]:


title_strip = [title.text.strip() for title in title]
print(title_strip)


# In[69]:


df = pd.DataFrame(columns = title_strip)

df


# Price:

# In[70]:


price = soup.find('span', class_='a-price-whole').get_text()
print(price)


# **CREATE A CSV TO IMPORT THE DATA**

# In[71]:


import datetime
import csv
import pandas as pd


# Create a Timestamp for your output to track when data was collected
today = datetime.date.today()

# Print today's date
print("Today's date:", today)

# Define the CSV header and data
header = ['Title', 'Price', 'Date']
data = [title_strip, price, today]

# Escribir datos en un archivo CSV

##### only run this part of the code ONCE
with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:  
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
##### NOTE: RUN EVERY TIME IF YOU WANT TO SUBSTITUTE THE OLD PRICE, WITH THE NEW ONE


# Read CSV file using pandas
try:
    df = pd.read_csv('AmazonWebScraperDataset.csv')
    print(df)
except FileNotFoundError:
    print("El archivo CSV no se encontró. Verifique la ruta y asegúrese de que el archivo exista.")


# In[72]:


df


# In[73]:


df.to_csv(r'C:\Users\user\Desktop\Programacion\Portfolio Projects\Python Amazon Web Scraping\AmazonWebScraperDataset.csv', index = True)


# **------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**

# **COMBINE AND AUTOMATING FUNCTION**

# In[74]:


from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

from urllib.request import urlopen as uReq


def check_price():
    url = 'https://www.amazon.com.mx/Arena-para-gato-Scoop-Away/dp/B0161N7FE8/ref=sr_1_1?crid=2LRO0IIPP5H1G&dib=eyJ2IjoiMSJ9.mTRK9wEdM99ZOQHPRxycYz6yIDz2DrV_t4xHTEkv156W1OVSOKUwnor_nIbdeUsB07Ju-3EXUbBpvqlratYA_4MsaGETIeUvZ1CkYlPCFVyHB8HlHDe4IV1cSCqDXl3QpTHaxvPcfRdF1wjuQ4dAEO7gYBGAlgv9X-g1C4eQoB0x1QPgYhxMZ3624XIHgOJ5jBjdstK1WdjLk0S5JBIs9an_eWVADqcdtxO9PBBHwd9Vg36ubkT3QMb7ul9zcJ2sBcLwm4Z2iolQtj_QsA0swPqBzphbIx75GnkHd95jMyg.bsv63sQ8zBtrRWmbAoEk8og2rh0FE2GKmLqL_VgQjyU&dib_tag=se&keywords=arena+para+gato&qid=1711388502&sprefix=arena+para+%2Caps%2C3242&sr=8-1&ufe=app_do%3Aamzn1.fos.4e545b5e-1d45-498b-8193-a253464ffa47'
    client = uReq(url)  # grabs the page
    soup = BeautifulSoup(client.read(), 'html.parser')


    # Getting Product
    title = soup.find_all('span', id='productTitle')
    title_strip = [title.text.strip() for title in title]

    # Getting Price
    price = soup.find('span', class_='a-price-whole').get_text()

    import csv
    import pandas as pd

    # Create a Timestamp for your output to track when data was collected
    today = datetime.date.today()

    # Print today's date
    print("Today's date:", today)

    # Define the CSV header and data
    header = ['Title', 'Price', 'Date']
    data = [title_strip, price, today]

    # Escribir datos en un archivo CSV
    ##### only run this part of the code ONCE
    with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
    ##### NOTE: RUN EVERY TIME IF YOU WANT TO SUBSTITUTE THE OLD PRICE, WITH THE NEW ONE
        
    # Read CSV file using pandas
    try:
        df = pd.read_csv('AmazonWebScraperDataset.csv')
    except FileNotFoundError:
        print("El archivo CSV no se encontró. Verifique la ruta y asegúrese de que el archivo exista.")


# Add the next code to automate and update the price automatically, creating new columns or substituting existing columns with the new price (depends on how many times you run the '#####' part of the code:

# In[ ]:


# Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400)


# **------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**

# **CREATE AN AUTOMATE EMAIL NOTIFICATION**

# In[ ]:


def check_price():
    url = 'https://www.amazon.com.mx/Arena-para-gato-Scoop-Away/dp/B0161N7FE8/ref=sr_1_1?crid=2LRO0IIPP5H1G&dib=eyJ2IjoiMSJ9.mTRK9wEdM99ZOQHPRxycYz6yIDz2DrV_t4xHTEkv156W1OVSOKUwnor_nIbdeUsB07Ju-3EXUbBpvqlratYA_4MsaGETIeUvZ1CkYlPCFVyHB8HlHDe4IV1cSCqDXl3QpTHaxvPcfRdF1wjuQ4dAEO7gYBGAlgv9X-g1C4eQoB0x1QPgYhxMZ3624XIHgOJ5jBjdstK1WdjLk0S5JBIs9an_eWVADqcdtxO9PBBHwd9Vg36ubkT3QMb7ul9zcJ2sBcLwm4Z2iolQtj_QsA0swPqBzphbIx75GnkHd95jMyg.bsv63sQ8zBtrRWmbAoEk8og2rh0FE2GKmLqL_VgQjyU&dib_tag=se&keywords=arena+para+gato&qid=1711388502&sprefix=arena+para+%2Caps%2C3242&sr=8-1&ufe=app_do%3Aamzn1.fos.4e545b5e-1d45-498b-8193-a253464ffa47'
    client = uReq(url)  # grabs the page
    soup = BeautifulSoup(client.read(), 'html.parser')

    # Getting Product
    title = soup.find('span', id='productTitle').get_text(strip=True)

    # Getting Price
    price = float(soup.find('span', class_='a-price-whole').get_text()

    # Define the desired price threshold
    desired_price = (price - (price* 0.15)) 

    # Check if the current price is below the desired threshold
    if price <= desired_price:
        # Send email
        send_mail(title, price)
    else:
        print("The price is not below 15% discount. Not sending email.")

def send_mail(title, price):
    # Your email sending logic here
    # This is just a placeholder, you need to implement your own email sending logic
    # Example:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('YOUR_EMAIL@gmail.com', 'YOUR_PASSWORD')

    subject = f"The price of '{title}' is now ${price:.2f}!"
    body = "This is the moment we have been waiting for. Let's make a discount!"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'YOUR_EMAIL@gmail.com',
        'RECIPIENT_EMAIL@gmail.com',  # Replace with recipient email address
        msg
    )

# Llama a la función check_price()
check_price()


# In[ ]:


# Runs check_price a set time and sends notifications to your email and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400)


# **------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**

# In[ ]:




