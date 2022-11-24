import sys
import os
import unittest

# workaround to debug from vscode
cwd = os.getcwd()
sys.path.append(cwd)

from python_cpp_debug_example.python.py_module import add as pyadd

# if __debug__:
#     import python.py_module as py_module
    
#     print(f'\npython path: {sys.path}')

#     print(f'\nadd_module: ${dir(py_module)}')

#     print(f'\nadd_module.add: ${dir(py_module.add)}')
#     print(f'\npyadd: ${dir(py_module.add)}')

class TestAdd(unittest.TestCase):
    '''Test Add'''
    def test_plus(self):
        ret = pyadd.plus(40,2)
        self.assertEqual(42, ret)

    def test_minus(self):
        ret = pyadd.minus(40,2)
        self.assertEqual(38, ret)

       
if __name__ == '__main__':
    unittest.main(verbosity=2)
