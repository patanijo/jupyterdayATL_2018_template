
# coding: utf-8

# # {{cookiecutter.project_name}}
# 
# ##### Version 0.1
# #####  Author: {{cookiecutter.author_name}}
# ##### email: {{cookiecutter.author_email}}
# ##### Date: {% now 'local', '%d-%b-%Y' %}
# 
# ##### Contributors: 

# In[2]:


get_ipython().magic(u'matplotlib inline')

#standard library imports
import os
import sys

#external library imports
import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

module_path = os.path.abspath(os.path.join('..'))

# Enable importing of modules saved in src
if module_path not in sys.path:
    sys.path.append('..')

#local package imports
import src


# ## Modeling and Analysis
# * What techniques, modeling methods, domain specific calculations have been used?
# * Are there specific parameters that have been used, tried, or optimized?
# 
# #### Model Training and Tuning
# 
# * What modeling method(s) or engineering calculations will be used?
# * List any specific modeling assumptions.
# * List any model parameters used.

# In[ ]:


# Load the data set in from the pre-processed data
model_data = pd.read_csv('../data/processed/{{cookiecutter.repo_name}}_processed.csv')

feature_columns = []
predicted_class_names = []

X = model_data[feature_columns].values
y = model_data[predicted_class_names].values
split_test_size = 0.10

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_test_size)

# {{cookiecutter.repo_name}}_model = {sklearn_model}.fit(X_train,y_train)


# ### Save a copy of the final model to models directory

# In[ ]:


# Save the trained model to ../models
joblib.dump({{cookiecutter.repo_name}}_model, '../models/iris_nb.pkl') 

