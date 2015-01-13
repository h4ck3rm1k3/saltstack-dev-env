#!/usr/bin/env python

from __future__ import print_function

from subprocess import check_call
from os import makedirs, path
from sys import exit
from subprocess import CalledProcessError

try:
    from github import Github
except ImportError:
    print("Needz moar PyGithub")
    exit(0)

# Hardcode relative paths for now
# Formulas should be up one dir in saltstack-formulas
FORMULAS_PATH = path.realpath(
                    path.join(
                        path.dirname( __file__ ), 
                        path.pardir,
                        'saltstack-formulas'
                    )
                )

def main():
    gh = Github()

    formula_repo_urls = [[repo.name, repo.git_url]
                         for repo in gh.get_user('saltstack-formulas').get_repos()
                         if repo.name.endswith('-formula')]

    for repo_name, repo_url in formula_repo_urls:
        # Check for the formulas dir and create it if it doesn't exist.
        # Will need to check if it's a symlink later too
        if not path.exists(FORMULAS_PATH):
            try:
                makedirs(FORMULAS_PATH)
            except:
                print("Error creating saltstack-formulas dir")
                exit(0)
            
        clone_path = path.join(FORMULAS_PATH, repo_name)

        # Shell out to git and clone the repository
        print("Cloning {0}...".format(repo_name))
        try:
            cmd = check_call(['git', 'clone', repo_url, clone_path], stdout=None)
        except CalledProcessError:
            print("Failed to clone {0}".format(repo_name))
            continue

if __name__ == '__main__':
    main()
