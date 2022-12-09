from rules_python.python.runfiles import runfiles

class RunfilesHelper:
    """A simple example class"""
    i = 12345

    def f(self):
        return 31
    
    def readFile(runfiles_key):
        r = runfiles.Create()
        return r.Rlocation(f"{runfiles_key}")
