from conans import ConanFile, CMake, tools


class MultiConfigLibraryTemplate(ConanFile):
    name = "multi-config-library-template"
    version = "0.0.1"
    description = "Multi Config Library Template"
    license = "MIT"
    url = "https://github.com/tarc/multi-config-library-template"

    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "src/*.cpp", "include/*.hpp", "version.hpp.in"

    def _native(self):
        return not tools.cross_building(self.settings)

    def _visual_studio(self):
        return self.settings.compiler == "Visual Studio"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

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
            self.cpp_info.release.libs = [f"{self.name}"]
        else:
            self.cpp_info.debug.libs = [f"{self.name}_d"]
