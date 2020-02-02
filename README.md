|[![Debug](https://github.com/tarc/library-template/workflows/Debug/badge.svg?branch=master)](https://github.com/tarc/library-template/actions)|[![Release](https://github.com/tarc/library-template/workflows/Release/badge.svg?branch=master)](https://github.com/tarc/library-template/actions)|
|:---:|:---:|

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
git clone https://github.com/tarc/library-template.git
cd library-template
./export-pkg.sh
```

Windows Batch:

```console
git clone https://github.com/tarc/library-template.git
cd library-template
export-pkg.bat
```
