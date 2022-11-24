workspace(name = "python_cpp_debug_example")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository", "new_git_repository")

# Gtest
git_repository(
    name = "com_google_googletest",
    tag = "release-1.11.0",
    remote = "https://github.com/google/googletest.git",
)

# Python
git_repository(
    name = "rules_python",
    tag = "0.10.0",
    remote = "https://github.com/bazelbuild/rules_python.git",
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains")
python_register_toolchains(
    name = "python39",
    python_version = "3.9",
)

#pybind11_bazel patches
git_repository(
    name = "pybind11_bazel",
    commit = "72cbbf1fbc830e487e3012862b7b720001b70672",
    patches = [
      "//patches:0001-patch-1.patch",
      "//patches:0002-patch-2.patch",
      "//patches:0003-patch-3.patch",
      "//patches:0004-patch-4.patch",
      "//patches:0005-patch-5.patch",
    ],
    patch_args = ["-p1"],
    remote = "https://github.com/pybind/pybind11_bazel.git",
)

#Pybind11
new_git_repository(
    name = "pybind11",
    build_file = "@pybind11_bazel//:pybind11.BUILD",
    tag = "v2.9.2",
    remote = "https://github.com/pybind/pybind11.git",
)

load("@pybind11_bazel//:python_configure.bzl", "python_configure")

load("@python39//:defs.bzl", "interpreter")

# binding python to pybind11_bazel
python_configure(
  name = "local_config_python",
  python_interpreter_target = interpreter,
)
