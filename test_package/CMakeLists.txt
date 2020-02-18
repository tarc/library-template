# Enable MSVC runtime library flags

cmake_minimum_required(VERSION 3.15)
cmake_policy(SET CMP0091 NEW)

project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})

# CTest is a testing tool that can be used to test your project.
enable_testing()
add_test(NAME example
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
         COMMAND example)


message( STATUS "CONAN_MSVC_RUNTIME_LIBRARY: ${CONAN_MSVC_RUNTIME_LIBRARY}")

# Set static runtime for MSVC

if ( CMAKE_CXX_COMPILER_ID STREQUAL "MSVC" )

  set_property(TARGET example PROPERTY
    MSVC_RUNTIME_LIBRARY ${CONAN_MSVC_RUNTIME_LIBRARY} )

endif ( CMAKE_CXX_COMPILER_ID STREQUAL "MSVC" )