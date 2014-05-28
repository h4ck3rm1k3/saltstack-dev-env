#!/usr/bin/env python

from __future__ import print_function

from os import listdir, path, symlink
import re

# Formulas should be up one dir in saltstack-formulas
FORMULAS_PATH = path.realpath(
                    path.join(
                        path.dirname( __file__ ), 
                        path.pardir,
                        'saltstack-formulas'
                    )
                )

STATE_TREE_PATH = path.realpath(
                      path.join(
                          path.dirname( __file__ ), 
                          path.pardir,
                          'salt-state-tree'
                      )
                  )


def main():
    formula_names = []
    formula_names = [path.join(re.sub('-formula', '', formula_path))
                     for formula_path in listdir(FORMULAS_PATH)]

    formula_paths = [] 
    formula_paths = [path.join(FORMULAS_PATH, formula_path, re.sub('-formula', '', formula_path))
                     for formula_path in listdir(FORMULAS_PATH)]

    formulas = {}
    formulas = dict(zip(formula_names, formula_paths))
 
    for formula_name, formula_path in formulas.items():
        symlink_path = path.join(STATE_TREE_PATH, formula_name)
        print('Linking {0} formula into state tree at {1}'.format(formula_name, symlink_path))
        # Only works on Linux for now
        # Want this to be cross-platform so Windows hosts can be used with Vagrant
        symlink(formula_path, symlink_path)
    

if __name__ == '__main__':
    main()
