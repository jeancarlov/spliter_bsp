#!/usr/bin/env python
# coding: utf-8

# In[41]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[23]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[24]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[25]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[26]:


slide_elem.find('div', class_='content_title')


# In[27]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[28]:


news_Summary_text = slide_elem.find('div', class_='article_teaser_body').get_text()


# In[29]:


news_Summary_text


# In[30]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # Visit URL
# 

# In[35]:


url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[36]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem


# In[37]:


full_image_elem.click()


# In[38]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[39]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[40]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[42]:


# Instead of scraping each row, or the data in each <td />
# scrape the entire table with Pandas
df = pd.read_html('https://galaxyfacts-mars.com')[0]


# In[44]:


df.head()


# In[45]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[46]:


#Pandas also has a way to easily convert our DataFrame back into HTML-ready code using the .to_html() function
df.to_html()


# In[47]:


# Jupyter Notebook, add browser.quit() and execute that cell to end the session. 
browser.quit()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




