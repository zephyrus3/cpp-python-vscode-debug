import sys
import os
import unittest

# workaround to debug from vscode
cwd = os.getcwd()
sys.path.append(cwd)

import python_cpp_debug_example.cpp_n_python.cpp_on_python.pyd_module.MyAddModule as pyd_module

class TestMyAddModule(unittest.TestCase):
    def test_add_from_cpp(self):
        a = 1
        b = 3
        ret = pyd_module.add_from_cpp(a,b)
        self.assertEqual(a+b, ret)
        
    def test_minus_from_cpp(self):
        a = 1
        b = 3
        ret = pyd_module.minus_from_cpp(a,b)
        self.assertEqual(a-b, ret)


if __name__ == '__main__':
    unittest.main(verbosity=2)
