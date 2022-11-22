# Python wrapper for foo library.
load("@rules_python//python:defs.bzl", "py_library")

py_library(
  name = "foo_module",
  srcs = ["add.py"],
  deps = [],
  visibility = ["//visibility:public"],
)

py_test(
  name = "test",
  size = "small",
  srcs = ["test.py"],
  deps = [
    ":foo_module",
  ],
  data = ["//resources:resource_files"],
  tags = ["unit"],
  visibility = ["//visibility:public"],
)
