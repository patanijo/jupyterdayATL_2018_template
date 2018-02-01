#! /usr/bin/python

import subprocess

user_repo = 'https://github.build.ge.com/{{ cookiecutter.SSO }}/{{ cookiecutter.repo_name }}'
org_repo = 'https://github.build.ge.com/FleetServicesOfflineAnalytics/{{ cookiecutter.repo_name }}'

def create_git_repo():
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', 'Initial Automated commit of {{cookiecutter.project_name}}'])

def configure_git_remotes():
    print('Adding git remote named upstream under the {{ cookiecutter.SSO }} user')    
    subprocess.call(['git', 'remote', 'add', 'origin', user_repo])
    print('Adding git remote named upstream under the FleetManagement Offline Organization')
    subprocess.call(['git', 'remote', 'add', 'upstream', org_repo])

def create_conda_environment():
    # conda env create -f environment.yml
    subprocess.call(['conda', 'env', 'create', '-f', 'environment.yaml'])

if __name__ == "__main__":
    print('Initializing local git repository')
    create_git_repo()

    print('Configuring git remote named origin under your SSO')
    print()
    configure_git_remotes()
    {% if cookiecutter.create_conda_environment == "true" %}
    print('Creating a local conda environment named {{cookiecutter.conda_environment}}')
    create_conda_environment()
    print('Conda environment creation complete')
    {% endif %}
