cc_test(
    name = "test",
    size = "small",
    srcs = ["test_runfiles.cpp"],
    data = ["//resources:resource_files"],
    tags = ["unit"],
    visibility = ["//visibility:public"],
    deps = [
        "//cpp/runfiles_helper:RunfilesHelper",
        "@com_google_googletest//:gtest_main",
        "@bazel_tools//tools/cpp/runfiles",
    ],
)
