#include <iostream>
#include <cstdlib>

#include "version.hpp"

using namespace multi_config_library_template;

int main()
{
  std::cout << "v" << major_version_number
    << "." << minor_version_number
    << "." << patch_version_number
    <<"\n";

  return EXIT_SUCCESS;
}
