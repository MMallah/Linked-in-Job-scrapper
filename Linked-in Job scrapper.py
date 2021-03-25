#!/usr/bin/env python
# coding: utf-8

# # Project Data Science Desired Skills
# 
# this project will Answer the question of what are the most desired skills for Data Science in Egypt and UAE.
# * Extract data from Linked in Via webscrapping or Manually.
# * Perform data wrangling ( image recognition or NLP).
# * Segment the the job market based on skills.
# * Analyze the skill growth over time.

# Import libraries

# In[134]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from scrapy import selector
import time
import operator
from functools import reduce


# ## step 1 Importing Data
# 

# #### Selenium driver for chrome

# In[78]:


# instantiate a webdriver
driver = webdriver.Chrome('C:\\Users\\mosta\\Downloads\\chromedriver_win32\\chromedriver.exe')


# In[79]:


# use chrome to get the desired url
driver.get('https://www.linkedin.com/jobs/search/?geoId=102007122&keywords=data%20scientist&location=Cairo%2C%20Egypt')


# In[61]:


# the job card container(link for job)
full_card_link= driver.find_elements_by_class_name("result-card__full-card-link")


# In[62]:


# view the Selenium elment count
len(full_card_link)


# In[66]:


link_list=[]
for e in full_card_link:
    link_list.append(e.get_attribute('href'))


# In[67]:


len(link_list)


# In[166]:





# In[187]:


for l in range(len(link_list)):
    print(link_list[l])


# In[122]:


# create list place holder for data
job_title=[]
company=[]
location=[]
posting_date=[]
applicants_count=[]
job_description=[]
job_seniority_level=[]
employment_type=[]
industry=[]
job_function=[]


# In[237]:


# create a function to iterate over job links

def get_job(links):
    ''' function to import the required data (10 specifications) from the search url'''
    for link in range(len(links)):
        driver.get(links[link])
        job_title.append(driver.find_element_by_class_name("topcard__title").text)
        company.append(driver.find_element_by_class_name('topcard__flavor').text)
        location.append(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[2]/div[1]/div[1]/h3[1]/span[2]').text)
        posting_date.append(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[2]/div[1]/div[1]/h3[2]/span[1]').text)
        try:
            applicants_count.append(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[2]/div[1]/div[1]/h3[2]/span[2]').text)
        except:
            applicants_count.append('')
        job_description.append(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[3]/div/section/div').text)
        try:
            job_seniority_level.append(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[3]/ul/li[1]/span').text)
        except:
            job_seniority_level.append('')
        employment_type.append(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[3]/ul/li[2]/span').text)
        industry.append(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[3]/ul/li[4]/span').text)
        job_function.append(reduce(operator.concat,
           [(e.text+ ", ") for e in driver.find_elements_by_xpath('//*[@id="main-content"]/section[1]/section[3]/ul/li[3]/span')]))
        time.sleep(5)


# In[241]:


#company


# In[239]:


#use the function to import the data
get_job(link_list)


# In[243]:


# convert lists acqquired to a dataframe
data= pd.DataFrame(list(zip(job_title, company, location, posting_date, applicants_count, job_description, job_seniority_level,
                            employment_type, industry, job_function)),
                   columns=['job_title', 'company', 'location', 'posting_date', 'applicants_count', 'job_description', 'job_seniority_level',
                            'employment_type', 'industry', 'job_function'])


# In[245]:


data.info()


# In[200]:


# job title
#print(driver.find_element_by_class_name("topcard__title").text)


# In[98]:


# company
#print(driver.find_element_by_class_name('topcard__flavor').text)


# In[107]:


# job location
#print(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[2]/div[1]/div[1]/h3[1]/span[2]').text)


# In[110]:


# posting date
#print(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[2]/div[1]/div[1]/h3[2]/span[1]').text)


# In[112]:


# number of applicants
#rint(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[2]/div[1]/div[1]/h3[2]/span[2]').text)


# In[113]:


# description
#print(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[3]/div/section/div').text)


# In[206]:


# job_seniority_level
#print(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[3]/ul/li[1]/span').text)


# In[114]:


# employment_type
#print(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[3]/ul/li[2]/span').text)


# In[119]:


# job_function
for e in(driver.find_elements_by_xpath('//*[@id="main-content"]/section[1]/section[3]/ul/li[3]/span')):
    print(e.text)


# In[145]:


#test=[]
#test.append(reduce(operator.concat,
#       [(e.text+ ", ") for e in driver.find_elements_by_xpath('//*[@id="main-content"]/section[1]/section[3]/ul/li[3]/span')]))


# In[146]:


test


# In[120]:


# industry
#print(driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/section[3]/ul/li[4]/span').text)


# In[10]:


#job_card = driver.find_elements_by_class_name("results__detail-view")


# In[147]:


#for e in job_card:
#    print(e.text)


# In[ ]:


# the right rail,  jobs-search job details container
#body > div.application-outlet > div.authentication-outlet > div.job-search-ext > div > div > section.jobs-search__right-rail > div


# In[ ]:


# the path for the header

#/html/body/main/div/section[2]/ul/li[1]/a


# In[ ]:


# the show more tab where body is located
#/html/body/main/section/div[2]/section[2]/div/section/div

