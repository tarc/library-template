[![Build and Test](https://github.com/tarc/multi-config-library-template/workflows/Build%20and%20Package/badge.svg?branch=develop)](https://github.com/tarc/multi-config-library-template/actions)

C++ template project leveraging:

- [CMake](https://cmake.org/) for building;
- [Conan](https://conan.io/) for dependency management;
- [Google Test](https://github.com/google/googletest) for testing;
- [Github Actions](https://github.com/features/actions) for CI;
- Automation Scripts.

It depends on a C/C++ toolchain, CMake and Conan (which will require Python as
well). It's been tested on MacOS, Linux and Windows - it's supposed to run as
it is, as long as the dependencies are met:

Bash:

```console
git clone https://github.com/tarc/multi-config-library-template.git
cd multi-config-library-template
./export-pkg.sh
```

Windows Batch:

```console
git clone https://github.com/tarc/multi-config-library-template.git
cd multi-config-library-template
export-pkg.bat
```
