#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[5]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[14]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[15]:


df.to_html()


# ## Deliverable 1

# ## Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[2]:


import requests


# In[7]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

# retrieve page
response = requests.get(url)

# create Beautiful soup object
hemisphere_soup = soup(response.text, 'html.parser')


# In[11]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

results = hemisphere_soup.find_all('div', class_='item')

# Loop through results
for result in results:
    try:
        # get link to enhanced image
        link = result.a['href']
        image_url = f"{url}{link}"
        print(image_url)
        
        # visit image url
        browser.visit(image_url)
        
        # initialize Beautiful soup objet
        html = browser.html
        soup_img_download = soup(html, 'html.parser')
        
        # get full image tag
        full_image_tag = soup_img_download.find('a', text='Sample')
        
        # get full image href
        full_image_href = f"{url}/{full_image_tag['href']}"
        
        # get title of enhanced image
        title = result.find('h3').text
        
        # Add to dictionary to image list
        hemisphere_image_urls.append({'image_url':full_image_href, 'title':title})
    except Exception as e:
        print(e)


# In[12]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[13]:


# 5. Quit the browser
browser.quit()


# In[ ]:




