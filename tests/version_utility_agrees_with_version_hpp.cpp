#include <gtest/gtest.h>
#include <string>

#include "utils.hpp"
#include "version.hpp"

TEST( VersionUtilityAgreeWithVersionHPP , Pass )
{
  using namespace library_template;

  const std::string version_lib( version() );

  const std::string version_hpp(
      "v"
      + std::to_string( major_version_number ) + "."
      + std::to_string( minor_version_number ) + "."
      + std::to_string( patch_version_number ) );

  EXPECT_EQ( version_lib , version_hpp )
    << "Version string obtained from lib: " << version_lib
    << " and from version.hpp: " << version_hpp
    << " must be the same.";
}
