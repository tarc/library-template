from conans import ConanFile, CMake, tools


class MultiConfigLibraryTemplate(ConanFile):
    name = "multi-config-library-template"
    version = "0.0.1"
    description = "Multi Config Library Template"
    license = "MIT"
    url = "https://github.com/tarc/multi-config-library-template"

    settings = "os", "compiler", "arch"
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "src/*.cpp", "include/*.hpp", "version.hpp.in"

    def _native(self):
        return not tools.cross_building(self.settings)

    def _visual_studio(self):
        return self.settings.compiler == "Visual Studio"

    def _configure_cmake(self, build_type):
        cmake = CMake(self, build_type = build_type)

        if self._visual_studio():
            cmake.definitions["CONAN_LINK_RUNTIME"] = False

            if "MD" in self.settings.compiler.runtime:
                cmake.definitions["CONAN_MSVC_RUNTIME"] = "MultiThreaded"
            else:
                cmake.definitions["CONAN_MSVC_RUNTIME"] = "MultiThreadedDLL"

        cmake.configure()
        return cmake

    def package_id(self):
        if self._visual_studio():
            if "MD" in self.settings.compiler.runtime:
                self.info.settings.compiler.runtime = "MD/MDd"
            else:
                self.info.settings.compiler.runtime = "MT/MTd"

    def requirements(self):
        if self._native():
            self.requires("gtest/1.8.1@bincrafters/stable")

    def build(self):
        cmake = self._configure_cmake( "Debug" )
        cmake.build()
        if self._native():
            cmake.test()

        cmake = self._configure_cmake( "Release" )
        cmake.build()
        if self._native():
            cmake.test()

    def package(self):
        cmake = self._configure_cmake( "Debug" )
        cmake.install()

        cmake = self._configure_cmake( "Release" )
        cmake.install()

    def package_info(self):
        self.cpp_info.release.libs = [f"{self.name}"]
        self.cpp_info.debug.libs = [f"{self.name}_d"]