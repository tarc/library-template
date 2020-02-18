from conans import ConanFile, CMake, tools
import os
import subprocess
import importlib
import sys
sys.path.append("..")
convert_runtime_names = importlib.import_module("convert-runtime-names")


class LibraryTemplateTest(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"

    def _visual_studio(self):
        return self.settings.compiler == "Visual Studio"

    def build(self):
        cmake = CMake(self)

        if self._visual_studio():
            cmake.definitions["CONAN_MSVC_RUNTIME_LIBRARY"] = convert_runtime_names.convert(
                    str(self.settings.compiler.runtime) )

        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".%sexample" % os.sep)