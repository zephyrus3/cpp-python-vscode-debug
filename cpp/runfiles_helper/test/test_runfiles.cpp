#include "cpp/runfiles_helper/RunfilesHelper.h"
#include "tools/cpp/runfiles/runfiles.h"

#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include <fstream>
#include <string>


namespace RunFilesTest {
const std::string invalidKey = "invalid/path/invalid_file.txt";
const std::string validKey = "debug_session/resources/myfile.txt";
const auto runfilesPath = std::string(std::getenv("TEST_SRCDIR"));

TEST(RunFilesTest, InvalidPath) {
  auto pathOnRunfiles = runfilesPath + "/" + invalidKey;
  auto value = helper::getResourcePath(invalidKey);
  EXPECT_EQ(pathOnRunfiles, value);
}

TEST(RunFilesTest, ValidPath) {
  auto value = helper::getResourcePath(validKey);
  auto pathOnRunfiles = runfilesPath + "/" + validKey;
  EXPECT_NE(runfilesPath, value);
}

TEST(RunFilesTest, ReadFileFromRunfiles) {
  auto filePath = helper::getResourcePath(validKey);
  std::ifstream file(filePath);
  auto buffer = std::string(std::istreambuf_iterator<char>(file),
                       std::istreambuf_iterator<char>());

  EXPECT_THAT(buffer, ::testing::Not(::testing::IsEmpty()));
  std::cout << "Buffer Contents" << buffer;
}


} // namespace RunFilesTest
