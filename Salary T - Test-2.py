#!/usr/bin/env python
# coding: utf-8

# The excel file used is found at:
# http://college.cengage.com/mathematics/brase/understandable_statistics/7e/students/datasets/tvds/frames/frame.html
# 
# According to the website description, a random sample of male/female assitant professor pairs was taken from 22 U.S. universities. The file shows yearly income divided by 1000. 
# 
# ***USING A T Test, let's see what the average male and female assistant professor salaries are in the U.S. with 95% confidence***

# In[50]:


import pandas as pd 
from scipy.stats import t
import numpy as np
import statistics

data = pd.read_excel('./SalaryTest.xls')


# In[51]:


data.head(), data.shape, data.isnull().sum()


# In[52]:


#SAMPLE MEAN FOR EACH MALES AND FEMALES
mean_males = statistics.mean(data['MALES'])
mean_females = statistics.mean(data['FEMALES'])
mean_males, mean_females


# In[53]:


#SAMPLE STD's
std_males = statistics.stdev(data["MALES"])
std_females = statistics.stdev(data["FEMALES"])
std_males, std_females


# In[54]:


#Critical t
t = t.ppf(0.95, len(data)-1)
t


# In[55]:


#calculating confidence intervals
male_confidence = [(mean_males - t*(std_males/np.sqrt(len(data['MALES'])))), 
                   (mean_males + t*(std_males/np.sqrt(len(data['MALES']))))]
female_confidence = [(mean_females - t*(std_females/np.sqrt(len(data['FEMALES'])))), 
                   (mean_females + t*(std_females/np.sqrt(len(data['FEMALES']))))]


# In[56]:


print(male_confidence)
print(female_confidence)


# **USING A T TEST ON THIS DATA, WE CAN SAY WITH 95% CONFIDENCE THAT:**
# 
# >1. The average male assistant professor at a U.S. university earns between 32,130 and 34,732 dollars
# >2. The average female assistant professor at a U.S. university earns between 31,878 and 34,521 dollars

# In[ ]:




