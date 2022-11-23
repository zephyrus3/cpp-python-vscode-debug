#!/usr/bin/env python3
'''Test APIs'''

import sys
import unittest

from debug_session.python_session.add_module import add as pyadd
from debug_session.python_session.add_module.foo import Foo
import file as pyfile


if __debug__:
    import debug_session.python_session.add_module as add_module
    
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
