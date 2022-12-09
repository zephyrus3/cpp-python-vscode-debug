#include "cpp/add_module/add.h"

#include <gtest/gtest.h>

const int a = 10;
const int b = -5;

namespace AddTest {

TEST(AddTest, PlusFunction) {
  EXPECT_EQ(plus(a, b), a + b);
  EXPECT_EQ(plus(a, b), plus(b, a));
}

TEST(AddTest, MinusFunction) {
  EXPECT_EQ(minus(a, b), a - b);
  EXPECT_NE(minus(a, b), minus(b, a));
}

} // namespace AddTest


