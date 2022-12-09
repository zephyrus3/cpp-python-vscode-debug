#!/usr/bin/env python3
'''Test APIs'''

import sys
import os
import unittest

# workaround to debug from vscode
cwd = os.getcwd()
sys.path.append(cwd)

workspace_dir = os.path.join(cwd,"python_cpp_debug_example")
if os.path.exists(workspace_dir):
    sys.path.append(workspace_dir)

from python.add_module import add as pyadd
from python.add_module.foo import Foo

if __debug__:
    import python.add_module as add_module
    
    print(f'\npython path: {sys.path}')

    print(f'\nadd_module: ${dir(add_module)}')

    print(f'\nadd_module.add: ${dir(add_module.add)}')
    print(f'\npyadd: ${dir(add_module.add)}')

    print(f'\nadd_module.add.Foo: ${dir(add_module.foo.Foo)}')
    print(f'\npyadd.Foo: ${dir(add_module.foo.Foo)}')

class TestFoo(unittest.TestCase):
    '''Test Foo'''
    def test_plus(self):
        ret = pyadd.plus(40,2)
        self.assertEqual(42, ret)

    def test_minus(self):
        ret = pyadd.minus(40,2)
        self.assertEqual(38, ret)

    def test_class(self):
        p = Foo()
        self.assertEqual(31, p.f())
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
