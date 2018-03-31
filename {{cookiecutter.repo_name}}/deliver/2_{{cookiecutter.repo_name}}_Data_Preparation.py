
# coding: utf-8

# # {{cookiecutter.project_name}}
# 
# ##### Version 0.1
# #####  Author: {{cookiecutter.author_name}}
# ##### email: {{cookiecutter.author_email}}
# ##### Date: {% now 'local', '%d-%b-%Y' %}
# 
# ##### Contributors: 

# In[ ]:


get_ipython().magic(u'matplotlib inline')

#standard library imports
import os
import sys

#external library imports
import sklearn

module_path = os.path.abspath(os.path.join('..'))

# Enable importing of modules saved in src
if module_path not in sys.path:
    sys.path.append('..')

#local package imports
import src


# # Preprocessing
# 
# * __CRITICAL: DO NOT MODIFY YOUR ORIGINAL DATASET!__ 
#     * Save preprocessed data in the ../data/processed directory.
# * Identify how to clean, transform and deal with common data quality issues, such as missing data, gaps. etc. Identify any data that had to be removed and in addition any missing data that had to be imputed.
# * Any additional processing needed to create the final dataset, i.e. data that will be used for modeling. This can include things like merging multiple datasets or aggregation.
# * Describe derived data and any feature calculations
# * Provide details of data used for training, validation, testing.

# In[ ]:


# Data Cleaning code goes here.

