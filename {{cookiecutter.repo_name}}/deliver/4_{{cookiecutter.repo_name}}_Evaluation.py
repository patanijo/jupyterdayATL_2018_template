
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


# # Evaluation
# 
# At this stage in the project, you have built a model (or models) that appears to have high quality from a data analysis perspective. Before proceeding to final deployment of the model, it is important to thoroughly evaluate it and review the steps executed to create it, to be certain the model properly achieves the business objectives. 
# 
# 
# A key objective is to determine if there is some important business issue that has not been sufficiently considered. At the end of this phase, a decision on the use of the data mining results should be reached.
# 
# 
# ## Critical Questions + Decisions
# 
# * Can the model(s) generated be used to answer the business question?
# * Go/No Go Decision on model deployment and usage in business process.

# ## Results and Evaluation
# ### Model Performance Assessment and Comparisons
# * For classification analytics, calculate estimated true positive and false positive rate.
# * List artifacts of this analytic.
# 
# 
# #### Sample Tabular Output
# 
# __Model Performance on Training Data__
# 
# | Parameter     | Value       |
# | ------------- |-------------|
# | # of Units    | 0           |
# | # of units evaluated |    0 |
# | # of units with alarms |  0 |
# | # of units with no alarms | 0 |
# 
# __ Model Performance on Test or Validation Data__
# 
# | Parameter       | Value    |
# | ------------- |-------------|
# | # of Units    | 0 |
# | # of units evaluated  | 0  |
# | # of units with alarms |     0  |
# | # of units with no alarms | 0 |
