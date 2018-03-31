
# coding: utf-8

# # {{cookiecutter.project_name}}
# 
# ##### Version 0.1
# #####  Author: {{cookiecutter.author_name}}
# ##### email: {{cookiecutter.author_email}}
# ##### Date: {% now 'local', '%d-%b-%Y' %}
# 
# ##### Contributors: 

# # Deployment Plan
# 
# This task takes the evaluation results and determines a strategy for deployment. If a general procedure has
# been identified to create the relevant model(s), this procedure is documented here for later deployment.
# 
# ## Deployment steps
# 
# 1. Create a pull request to have your project development history merged into the organization Github repository.
# 2. From your top level project directory, at a command line run the command: 
# 
#     `docker build -t <your organization>/{{ cookiecutter.project_name.lower().replace(' ', '_') }}`.
#     
# 3. If the container builds sucessfully, run an instance of the container locally.
# 3. Test that you can run the model locally.
# 4. If you are satisfied that the model is giving as expected results, push the containerized image to your configured docker repository.
# 

# In[1]:


# Example code to test the rest api of the model

import requests

reply requests.get()


# # Monitoring and Maintenance Plan
# 
# Monitoring and maintenance are important issues if the data science result becomes part of the day-to-day business and its environment. The careful preparation of a maintenance strategy helps to avoid unnecessarily long periods of incorrect usage of machine learning model results 
# 
# ## Critical Questions
# 
# * Will model performance need to be tracked in real time?
# * If yes, how will model performance be tracked?
# * What is the process and schedule for retraining and redploying the model 
