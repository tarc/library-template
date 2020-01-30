#include <iostream>
#include <cstdlib>

#include "version.hpp"

using namespace yet_another_template_project;

int main()
{
  std::cout << "v" << major_version_number
    << "." << minor_version_number
    << "." << patch_version_number
    <<"\n";

  return EXIT_SUCCESS;
}
