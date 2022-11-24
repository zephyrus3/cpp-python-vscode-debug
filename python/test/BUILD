py_test(
  name = "add_test",
  size = "small",
  srcs = ["add_test.py"],
  deps = [
    "//python/py_module:add_module"
  ],
  data = ["//resources:resource_files"],
  tags = ["unit"],
  visibility = ["//visibility:public"],
)

py_test(
  name = "exception_test",
  size = "small",
  srcs = ["exception_test.py"],
  deps = [
    "//python/py_module:exception_module"
  ],
  data = ["//resources:resource_files"],
  tags = ["unit"],
  visibility = ["//visibility:public"],
)

py_test(
  name = "runfiles_test",
  size = "small",
  srcs = ["runfiles_test.py"],
  deps = [
    "//python/py_module:runfiles_module",
    "@rules_python//python/runfiles",
  ],
  data = ["//resources:resource_files"],
  tags = ["unit"],
  visibility = ["//visibility:public"],
)
