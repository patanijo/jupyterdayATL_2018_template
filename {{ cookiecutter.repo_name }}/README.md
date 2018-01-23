{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    │
    ├── data/               <- The original, immutable data dump. 
    │
    ├── figures/            <- Figures saved by scripts or notebooks.
    │
    ├── deliver/            <- Final deliverable Jupyter notebooks. Naming convention is a short `-` delimited 
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


Set up
------------

Install the virtual environment with conda and activate it:

```bash
$ conda env create -f environment.yml
$ activate example-project
```
