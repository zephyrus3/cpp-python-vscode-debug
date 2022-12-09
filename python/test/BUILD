py_test(
  name = "test",
  size = "small",
  srcs = ["test.py", "file.py"],
  deps = [
    "//python/add_module",
    "@rules_python//python/runfiles",
  ],
  data = ["//resources:resource_files"],
  tags = ["unit"],
  visibility = ["//visibility:public"],
)
