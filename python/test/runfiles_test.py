import sys
import os
import unittest

# workaround to debug from vscode
cwd = os.getcwd()
sys.path.append(cwd)

from python_cpp_debug_example.python.py_module.runfiles_helper import RunfilesHelper

# if __debug__:
#     import python.py_module.runfiles_helper as py_module
    
#     print(f'\n python path: {sys.path}')
#     print(f'\n runfiles_helper: ${dir(py_module)}')
#     print(f'\n runfiles_helper.RunfilesHelper: ${dir(py_module.RunfilesHelper)}')


class TestException(unittest.TestCase):
    runfilesPath = os.environ["PYTHON_RUNFILES"];
    invalid_key = "invalid/path/invalid_file.txt";
    valid_key = "python_cpp_debug_example/resources/myfile.txt"
    
    '''Test Exception'''
    def test_class_method(self):
        self.assertEqual(RunfilesHelper().f(), 31 )
        
    def test_class_attribute(self):
        self.assertEqual(RunfilesHelper().i, 12345 )

    def test_runfiles_path_wrong_key(self):
        filepath = RunfilesHelper.readFile(self.invalid_key)
        if sys.platform == "win32":
            self.assertIsNotNone(filepath)
        else:
            pathOnRunfiles = os.path.join(self.runfilesPath, self.invalid_key)
            self.assertEqual(filepath,pathOnRunfiles)
        
    def test_read_file_from_runfiles(self):
        filepath = RunfilesHelper.readFile(self.valid_key)
        if sys.platform != "win32":
            pathOnRunfiles = os.path.join(self.runfilesPath, self.valid_key)
            self.assertEqual(filepath,pathOnRunfiles)
        
        with open(filepath, "r") as f:
            print(f.read())
        
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
