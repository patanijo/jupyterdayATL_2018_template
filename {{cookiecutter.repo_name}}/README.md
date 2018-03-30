{{cookiecutter.project_name}}
==============================

Project Description: {{cookiecutter.description}}

Author: {{cookiecutter.author_name}}

e-mail: {{cookiecutter.author_email}}

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



Set up
------------

Install the virtual environment with conda using the included environment.yml file and activate it:

On Windows
```bash
$ conda env create -f environment.yml
$ activate {{ cookiecutter.project_name.lower().replace(' ', '_') }}_env
```
On OSx/Linux
```bash
$ conda env create -f environment.yml
$ source activate {{ cookiecutter.project_name.lower().replace(' ', '_') }}_env
```

How to Execute This Project
-----------

Include an example or two of how to run various cleaning or analysis tasks. This is often the first thing users and collaborators on your project will look at, so make it explicit. 
