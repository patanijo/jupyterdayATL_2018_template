#! /usr/bin/ python

import subprocess

user_repo = 'https://github.build.ge.com/FleetServicesOfflineAnalytics/' + '{{ cookiecutter.SSO }}/' + '{{ cookiecutter.repo_name }}'

print('Initializing local git repository')
subprocess.call(['cd', '{{ cookiecutter.repo_name }}'])
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial Automated commit'])

print('Configuring git remote named origin under your SSO')
subprocess.call(['git', 'remote', 'add', 'origin', user_repo])

