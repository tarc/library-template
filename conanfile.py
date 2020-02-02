from conans import ConanFile, CMake, tools


class LibraryTemplate(ConanFile):
    name = "library-template"
    version = "1.0.0"
    description = "Library Template"
    license = "MIT"
    url = "https://github.com/tarc/library-template"

    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "src/*.cpp", "include/*.hpp", "version.hpp.in", "tests/CMakeLists.txt", "tests/*.cpp"

    def _native(self):
        return not tools.cross_building(self.settings)

    def _visual_studio(self):
        return self.settings.compiler == "Visual Studio"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.verbose = True
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
            self.cpp_info.libs = ["liblibrary-template.a"]
        else:
            self.cpp_info.libs = ["liblibrary-template_d.a"]
