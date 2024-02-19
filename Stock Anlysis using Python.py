#!/usr/bin/env python
# coding: utf-8

# ## Question 1 - Extracting Tesla Stock Data Using yfinance

# In[23]:


import yfinance as yf
import pandas as pd   #importing required libraries


# Using the `Ticker` module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is <b>Tesla</b> and the ticker symbol is `TSLA`.
# 

# In[24]:


tesla=yf.Ticker("TSLA")
tesla_data=tesla.history(period="max")


# We can reset the index of the DataFrame with the `reset_index` function. We also set the `inplace` paramter to `True` so the change takes place to the DataFrame itself.
# 

# In[25]:


tesla_data.reset_index(inplace=True)
tesla_data.head() #Displaying first five rows of DataFrame


# ## Question 2 - Extracting Tesla Revenue Data Using Webscraping 

# In[26]:


#importing required libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup 


# In[27]:


url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
tesla=requests.get(url).text #we have text data of website in tesla
soup = BeautifulSoup(tesla,'html5lib') #Parsing a beautifulsoup object
read_html_data = pd.read_html(str(soup)) #Extracting html data uisng pandas read_htnlm() function
tesla_revenue = read_html_data[0] #Extracting table in html page 
tesla_revenue.tail() #showing last five rows using tail() function


# ## Question 3 - Extracting GameStop Stock Data Using yfinance

# In[28]:


gamestop = yf.Ticker("GME")
gme_data = gamestop.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head() #Displaying first five rows of DataFrame


# ## Question 4 - Extracting GameStop Revenue Data Using Webscraping

# In[4]:


url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
gme=requests.get(url).text #we have text data of website in tesla
soup = BeautifulSoup(gme,'html5lib') #Parsing a beautifulsoup object
read_html_data = pd.read_html(str(soup)) #Extracting html data uisng pandas read_html() function
gme_revenue = read_html_data[0] #Extracting table in html page 
gme_revenue.tail() #showing last five rows using tail() function


# ## Question 5: Plot Tesla Stock Graph

# In[22]:


#Defining a function to plot graph
def make_graph(tesla_data,tesla_revenue,str1): 
    tesla_data.plot(x="Date", y="Open",title=str1)
make_graph(tesla_data,tesla_revenue,"Tesla")


# ## Question 6: Plot GameStop Stock Graph

# In[21]:


make_graph(gme_data,gme_revenue,"GameStop")


# In[ ]:




