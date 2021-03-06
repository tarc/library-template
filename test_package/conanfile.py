from conans import ConanFile, CMake, tools
import os
import subprocess


class LibraryTemplateTest(ConanFile):
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            cmake = CMake(self)
            os.chdir("bin")
            self.run(".%sexample" % os.sep)
