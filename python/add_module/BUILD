# Python wrapper for foo library.
load("@rules_python//python:defs.bzl", "py_library")

py_library(
  name = "add_module",
  srcs = ["add.py", "foo.py"],
  deps = [],
  visibility = ["//visibility:public"],
)

# py_test(
#   name = "test",
#   size = "small",
#   srcs = ["test.py"],
#   deps = [
#     ":add_module",
#   ],
#   data = ["//resources:resource_files"],
#   tags = ["unit"],
#   visibility = ["//visibility:public"],
# )
