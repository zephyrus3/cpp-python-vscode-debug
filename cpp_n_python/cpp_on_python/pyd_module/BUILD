load("@pybind11_bazel//:build_defs.bzl", "pybind_extension")
load("@rules_python//python:defs.bzl", "py_library")

pyd_name = "MyAddModule"

pybind_extension(
    name = pyd_name,
    srcs = ["module.cpp"],
    visibility = ["//visibility:public"],
    deps = ["//cpp/add_module"],
)

py_library(
    # name = "MyAddModule_py",
    name = "{}_py".format(pyd_name),
    data = select({
        "@platforms//os:windows": [":{}.pyd".format(pyd_name)],
        "//conditions:default": [":{}.so".format(pyd_name)],
    }),
    imports = ["."],
    visibility = ["//visibility:public"],
)
