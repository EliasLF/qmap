//
// This file is part of the MQT QMAP library released under the MIT license.
// See README.md or go to https://github.com/cda-tum/qmap for more information.
//

#include "../../include/configuration/Configuration.hpp"
#include "Configuration.hpp"

#include "gtest/gtest.h"

TEST(Configuration, MethodOfString) {
  EXPECT_EQ(na::getMethodOfString("naive"), na::NAMappingMethod::NAIVE);
  EXPECT_EQ(na::getMethodOfString("smart"), na::NAMappingMethod::SMART);
  EXPECT_EQ(na::getMethodOfString("NaIvE"), na::NAMappingMethod::NAIVE);
  EXPECT_EQ(na::getMethodOfString("sMaRt"), na::NAMappingMethod::SMART);
  EXPECT_THROW(std::ignore = na::getMethodOfString("unsupported"),
               std::invalid_argument);
}

TEST(Configuration, Import) {
  EXPECT_THROW(na::Configuration("nonexistent.json"), std::runtime_error);
  std::istringstream configIS(R"(
    {
      "patch": {
        "rows": 2,
        "cols": 3
      },
      "method": "smart"
    }
  )");
  na::Configuration  config(configIS);
  EXPECT_EQ(config.getPatchRows(), 2);
  EXPECT_EQ(config.getPatchCols(), 3);
  EXPECT_EQ(config.getMethod(), na::NAMappingMethod::SMART);
}
