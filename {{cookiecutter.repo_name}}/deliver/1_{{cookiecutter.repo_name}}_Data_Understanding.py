
# coding: utf-8

# # {{cookiecutter.project_name}}
# 
# ##### Version 0.1
# #####  Author: {{cookiecutter.author_name}}
# ##### email: {{cookiecutter.author_email}}
# ##### Date: {% now 'local', '%d-%b-%Y' %}
# 
# ##### Contributors: 

# In[1]:


get_ipython().magic(u'matplotlib inline')

#standard library imports
import os
import sys

#external library imports
import pandas as pd
import sklearn

module_path = os.path.abspath(os.path.join('..'))

# Enable importing of modules saved in src
if module_path not in sys.path:
    sys.path.append('..')

#local package imports
import src


# # Data Collection
# 
# ## Critical Questions
# 
# * Identify all data sources that can or will be used.
# 
# * How and from where was the data collected?
# 

# In[11]:


get_ipython().run_cell_magic(u'bash', u'', u'\n# Code to download the data\nwget -O ../data/raw/raw_data.csv https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')


# # Data Description
# 
# Describe the data that has been acquired, including the format of the data, the quantity of data (for
# example, the number of records and fields in each table), the identities of the fields, and any other surface
# features which have been discovered. Evaluate whether the data acquired satisfies the relevant requirements.
# 
# 
# 
# # Data Exploration
# 
# Descriptive statistics of the datasets.
# Include graphs of the dataset that aid in deeper understanding or interpretation of the data. Typical content may include box plots, histograms, scatter plots, correlation plots, heat maps, etc.
# 

# In[ ]:


# EDA Code Here

