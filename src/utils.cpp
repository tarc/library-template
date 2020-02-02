#include <sstream>

#include "utils.hpp"
#include "version.hpp"

namespace library_template {

  std::string version()
  {
    using namespace library_template;

    std::ostringstream ss;

    ss << "v" << major_version_number
      << "." << minor_version_number
      << "." << patch_version_number;

    return ss.str();
  }

} // namespace library_template
