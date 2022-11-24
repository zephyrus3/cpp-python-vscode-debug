#include "cpp/runfiles_helper/RunfilesHelper.h"
#include "tools/cpp/runfiles/runfiles.h"

#include <memory>
#include <stdexcept>
#include <string>

namespace helper {
std::string getResourcePath(const std::string &resourcePath) {
  std::string error;
  using bzl_Runfiles = bazel::tools::cpp::runfiles::Runfiles;
  std::unique_ptr<bzl_Runfiles> runfiles(bzl_Runfiles::CreateForTest(&error));

  if (runfiles == nullptr) {
    throw std::runtime_error("Failed to create Runfile Instance: " + error);
  }

  return runfiles->Rlocation(resourcePath);
}

} // namespace helper
