#! /usr/bin/python

import subprocess

user_repo = 'https://github.com/{{ cookiecutter.github_user_name}}/{{ cookiecutter.repo_name }}'
org_repo = 'https://github.com/jupyterdayATL/{{ cookiecutter.repo_name }}'

def create_git_repo():
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', 'Initial Automated commit of {{cookiecutter.project_name}}'])

def configure_git_remotes():
    print('Adding git remote named upstream under the {{ cookiecutter.github_user_name }} user')    
    subprocess.call(['git', 'remote', 'add', 'origin', user_repo])
    print('Adding git remote named upstream under the JupyterdayATL Organization')
    subprocess.call(['git', 'remote', 'add', 'upstream', org_repo])
    print('\n Verify these remotes exist before pushing from your local repository \n')

def create_conda_environment():
    # conda env create -f environment.yml
    subprocess.call(['conda', 'env', 'create', '-f', 'environment.yaml'])

if __name__ == "__main__":
    print('Initializing local git repository')
    create_git_repo()

    print('Configuring git remote named origin under your github user name')
    print()
    configure_git_remotes()
