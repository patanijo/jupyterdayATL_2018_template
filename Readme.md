Creates a template Offline Analytic with the following directory structure

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

--------

Pre-requisites
--------
You have local Anaconda python distribution installed.
Your .condarc configuration file is configured so you can reach the public Anaconda repository

Usage
------------
1. Install cookiecutter package
    If using public Anaconda repository

    `conda install -c conda-forge cookiecutter `

    If using pip

   `pip install --user cookiecutter --proxy <http://your_proxy_address>`

2. Create an offline analytic Using this template:

    `cookiecutter https://github.com/patanijo/jupyterdayATL_2018_template`

        a. You'll be prompted to enter values for a series of questions.
        b. Then it'll create your data science project in the __current working directory__ based on those values.
3. Create a local virtual environment using the created `environment.yaml` file in your template directory.
   The command is conda env create --file environment.yaml.
4. Activate the environment using the command for your OS.
5. Start the jupyter notebook


What does this template do?
----------------------------
* Create a new project based on this template including the following
    * templated Jupyter Notebooks
    * Source code required to create a REST API to a machine learning model.
    * Boilerplate files used for deployment of your machine learning model.
* Create a conda enviroment file, with standard dependencies.
* Initialize a local git repository
* Configure remotes for your local git repository

