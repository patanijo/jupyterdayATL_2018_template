
# coding: utf-8

# # {{cookiecutter.project_name}}
# 
# ##### Version 0.1
# #####  Author: {{cookiecutter.author_name}}
# ##### email: {{cookiecutter.author_email}}
# ##### Date: {% now 'local', '%d-%b-%Y' %}
# 
# ##### Contributors: 
# 

# In[6]:


get_ipython().magic(u'matplotlib inline')

#standard library imports
import os
import sys

#external library imports
import sklearn

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append('..')

#local package imports
import src


# ## Business/Domain Understanding
# 
# Identify a business problem or question and agree with stakeholders about the questions and hypotheses this analytic study will be trying to answer.
# 
# ### Background
# * What is known about the problem at the beginning of the project?
# * Any resources, constraints or assumptions?
# * Who is the customer for this project?
# 
# ### Goals & Objectives
# * What are the goals and objective for doing this data science project?
# * What is the business value for a successful implementation of this data science project?
# * What are the specific required outputs of this data science project?
# 
# ### Success Criteria
# * Identify specific metrics that will be used to assess success.
# 
# For example:
# 
# 1. Minimum lead time of …….
# 2. False positive rate should be less than …..%.
# 3. True positive rate should be at least …. %
# 4. Predict Customer churn with x% Accuracy
