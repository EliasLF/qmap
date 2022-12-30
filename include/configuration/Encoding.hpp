//
// This file is part of the MQT QMAP library released under the MIT license.
// See README.md or go to https://github.com/cda-tum/qmap for more information.
//

#pragma once

#include <iostream>

enum class Encoding { Naive, Commander, Bimander };

[[maybe_unused]] static inline std::string toString(const Encoding encoding) {
  switch (encoding) {
  case Encoding::Naive:
    return "naive";
  case Encoding::Commander:
    return "commander";
  case Encoding::Bimander:
    return "bimander";
  }
  return " ";
}

[[maybe_unused]] static Encoding
encodingFromString(const std::string& encoding) {
  if (encoding == "naive" || encoding == "0") {
    return Encoding::Naive;
  }
  if (encoding == "commander" || encoding == "1") {
    return Encoding::Commander;
  }
  if (encoding == "bimander" || encoding == "2") {
    return Encoding::Bimander;
  }
  throw std::invalid_argument("Invalid encoding value: " + encoding);
}
