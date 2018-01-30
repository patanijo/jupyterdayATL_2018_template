#! /usr/bin/python

import subprocess

user_repo = 'https://github.build.ge.com/{{ cookiecutter.SSO }}/{{ cookiecutter.repo_name }}'
org_repo = 'https://github.build.ge.com/FleetServicesOfflineAnalytics/{{ cookiecutter.repo_name }}'

print('Initializing local git repository')
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial Automated commit of {{cookiecutter.project_name}}'])

print('Configuring git remote named origin under your SSO')
subprocess.call(['git', 'remote', 'add', 'origin', user_repo])
print('Adding git remote named upstream under the FleetManagement Offline repository')
subprocess.call(['git', 'remote', 'add', 'upstream', org_repo])
print('Project Directory Created {{ cookiecutter.repo_name }}')

