#!/usr/bin/env python3
'''Test APIs'''

import sys
import unittest

import python.foo_module
import python.foo_module.add as pyadd
import python.file as pyfile
from python.foo_module.add import Foo


if __debug__:
    print(f'\npython path: {sys.path}')

    print(f'\npython.foo_module: ${dir(python.foo_module)}')

    print(f'\npython.foo_module.add: ${dir(python.foo_module.add)}')
    print(f'\npyadd: ${dir(pyadd)}')

    print(f'\npython.foo_module.add.Foo: ${dir(python.foo_module.add.Foo)}')
    print(f'\npyadd.Foo: ${dir(pyadd.Foo)}')

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
        
    def test_file(self):
    filepath = 
    ret = pyfile.print_file()

if __name__ == '__main__':
    unittest.main(verbosity=2)
