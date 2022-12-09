import sys
import os
import unittest

# workaround to debug from vscode
cwd = os.getcwd()
sys.path.append(cwd)

from python_cpp_debug_example.python.py_module.exception_raiser import raise_exception

# if __debug__:
#     import python.py_module.exception_raiser as py_module
    
#     print(f'\npython path: {sys.path}')
#     print(f'\nexception_module: ${dir(py_module)}')
#     print(f'\nexception_module.raise_exception: ${dir(py_module.raise_exception)}')


class TestException(unittest.TestCase):
    '''Test Exception'''
    def test_no_exception(self):
        self.assertTrue(raise_exception(False))

    def test_raise_exception(self):
        with self.assertRaises(RuntimeError):
            raise_exception(True)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
