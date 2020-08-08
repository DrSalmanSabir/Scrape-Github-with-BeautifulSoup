#!/usr/bin/env python
# coding: utf-8

# In[16]:


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd


# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://github.com/DrSalmanSabir?tab=repositories'

html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

# lists
projects = []
links = []

# Getting the anchor tag and << itemprop >> attribute
for link in soup.find_all('a', itemprop="name codeRepository"):
    projects.append(link.text)
    links.append(link.get('href'))
    
# Creating the DataFrame, Projects & Urls as Columns and adding projects and links list values
df = pd.DataFrame({'Projects':projects, 'Urls':links})

# Cleaning the Text Removing the leftSpaces with lstrip() & replacing - with ' ' wiht replace()
df['Projects'] = df['Projects'].str.lstrip()
df['Projects'] = df['Projects'].str.replace('-',' ')

# Adding https://github.com/ to in the start of each row as we didn't get complete https link
df['Urls'] ='https://github.com/' + df['Urls'].astype(str)

# Creating Excel File
df.to_excel('GitHub.xlsx')

df


# In[ ]:




