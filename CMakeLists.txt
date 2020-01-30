# Enable MSVC runtime library flags

#if ( UNIX AND NOT APPLE )
#  cmake_minimum_required(VERSION 3.12)
#else ( UNIX AND NOT APPLE )
#  cmake_minimum_required(VERSION 3.15)
#  cmake_policy(SET CMP0091 NEW)
#endif ( UNIX AND NOT APPLE )

cmake_minimum_required(VERSION 3.12)


# Start project

set( ProjectName mulit-config-library-template )

project( ${ProjectName} )


# Multi config build setup:

include( ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake )

conan_basic_setup( TARGETS )


# Versioning the project (if git can be found)

find_package( Git )

set ( MAJOR_VERSION_NUMBER "0" )
set ( MINOR_VERSION_NUMBER "0" )
set ( PATCH_VERSION_NUMBER "0" )

if ( Git_FOUND )

  message( "Git found: ${GIT_EXECUTABLE}" )

  execute_process( COMMAND ${GIT_EXECUTABLE} describe --abbrev=0 --tags --always
    OUTPUT_VARIABLE GIT_REPO_VERSION )

  if ( GIT_REPO_VERSION MATCHES "v([0-9]*)\\.([0-9]*)\\.([0-9]*)" )
    message( "Parsing version: ${CMAKE_MATCH_1}.${CMAKE_MATCH_2}.${CMAKE_MATCH_3}" )

    set ( MAJOR_VERSION_NUMBER ${CMAKE_MATCH_1} )
    set ( MINOR_VERSION_NUMBER ${CMAKE_MATCH_2} )
    set ( PATCH_VERSION_NUMBER ${CMAKE_MATCH_3} )

  else ( )

    message( "Could not extract version from: ${GIT_REPO_VERSION}" )

  endif ( )

endif ( )

configure_file ( version.hpp.in version.hpp )


# Setting targets:

add_executable( ${ProjectName}
  ${CMAKE_SOURCE_DIR}/src/main.cpp )

target_include_directories( ${ProjectName}
  PRIVATE ${CMAKE_SOURCE_DIR}/include
  PRIVATE ${CMAKE_CURRENT_BINARY_DIR} )

# target_link_libraries( ${ProjectName}
#  PRIVATE CONAN_PKG::some-package )


# Setting tests

include( GoogleTest )

include( CTest )

add_subdirectory( ${CMAKE_SOURCE_DIR}/tests )


#

set_target_properties(${ProjectName} PROPERTIES DEBUG_POSTFIX _d)

set_target_properties(tests PROPERTIES DEBUG_POSTFIX _d)


# Force C++17 standard

set_property ( TARGET ${ProjectName} PROPERTY CXX_STANDARD 17 )
set_property ( TARGET ${ProjectName} PROPERTY CXX_STANDARD_REQUIRED ON )

set_property ( TARGET tests PROPERTY CXX_STANDARD 17 )
set_property ( TARGET tests PROPERTY CXX_STANDARD_REQUIRED ON )


# Set static runtime for MSVC

#if ( NOT UNIX OR APPLE )
#  set_property(TARGET ${ProjectName} PROPERTY
#    MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
#
#  set_property(TARGET tests PROPERTY
#    MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
#endif ( NOT UNIX OR APPLE )
