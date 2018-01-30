{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}
{{cookiecutter.author_name}}

Project Organization
------------

    │
    ├── data/               <- Directory of data files
    │   |-- raw/            <- The original immutable data dump.
    │   |-- processed/      <-  cleaned data sets and modelling ready data sets.  
    │
    ├── figures/            <- Figures saved by scripts or notebooks.
    │
    ├── deliver/            <- Final deliverable analytic artifacts. Naming convention is a short `-` delimited 
    │                          number for ordering, Project Description, Process description, and the creator's initials,
    │                          e.g. `01_CoalAnalysis_DataCleaning`.
    │
    ├── dev/                <- Scratch notebook space, useful for experiments.
    │
    ├── models/             <- Serialized or pickled machine learning models
    │
    ├── src/                <- Python module with source code of this project.
    │
    ├── environment.yml     <- conda virtual environment definition file.
    │
    ├── LICENSE
    │
    ├── README.md           <- The top-level README for developers using this project.
    │


--------

<p><small>Project based on the <a target="_blank" href="https://github.build.ge.com/FleetServicesOfflineAnalytics/sample_offline_template">cookiecutter data science project template</a>.</p>

Usage
------------
1. Install cookiecutter package
    If using public Anaconda repository
    
    `conda install -c conda-forge cookiecutter `
    
    If using GE Internal Anaconda repository
    
    `conda install -c http://vdcalp02268.ics.cloud.ge.com:8080/conda/patanijo cookiecutter=1.6.0`  
2. Create an offline analytic Using this template:

    `cookiecutter https://github.build.ge.com/FleetServicesOfflineAnalytics/sample_offline_template` 

Set up
------------

Install the virtual environment with conda and activate it:

On Windows
```bash
$ conda env create -f environment.yml
$ activate {{cookiecutter.conda_environment}}
```
On OSx/Linux
```bash
$ conda env create -f environment.yml
$ source activate {{cookiecutter.conda_environment}}
```
