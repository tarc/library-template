from conans import ConanFile, CMake, tools
import version


class LibraryTemplate(ConanFile):
    name = "library-template"
    description = "Library Template"
    license = "MIT"
    url = "https://github.com/tarc/library-template"

    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    exports = "version.py"
    exports_sources = "CMakeLists.txt", "src/*.cpp", "include/*.hpp", "version.hpp", "tests/CMakeLists.txt", "tests/*.cpp"
    
    _minor = 0
    _major = 0
    _patch = 0

    def _native(self):
        return not tools.cross_building(self.settings)

    def _visual_studio(self):
        return self.settings.compiler == "Visual Studio"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["VERSION_NUMBER"] = self.version
        cmake.definitions["MAJOR_VERSION_NUMBER"] = self._major
        cmake.definitions["MINOR_VERSION_NUMBER"] = self._minor
        cmake.definitions["PATCH_VERSION_NUMBER"] = self._patch
        cmake.configure()
        return cmake

    def set_version(self):
        (self.version, self._major, self._minor, self._patch) = version.version()
        version.write_version_header("version.hpp", "LIBRARY_TEMPLATE_VERSION_HPP",
                "library_template", self._major, self._minor, self._patch)

    def requirements(self):
        if self._native():
            self.requires("gtest/1.8.1@bincrafters/stable")

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        if self._native():
            cmake.test()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        if self.settings.build_type == "Release":
            self.cpp_info.libs = ["liblibrary-template.a"]
        else:
            self.cpp_info.libs = ["liblibrary-template_d.a"]
