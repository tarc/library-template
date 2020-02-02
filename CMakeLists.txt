# Enable MSVC runtime library flags

cmake_minimum_required(VERSION 3.15)
cmake_policy(SET CMP0091 NEW)


# Start project

set( ProjectName library-template )

project( ${ProjectName} )


# Config build setup:

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

add_library( ${ProjectName}
  ${CMAKE_SOURCE_DIR}/src/utils.cpp )

target_include_directories( ${ProjectName}
  PUBLIC ${CMAKE_SOURCE_DIR}/include
  PUBLIC ${CMAKE_CURRENT_BINARY_DIR} )

set_target_properties( ${ProjectName} PROPERTIES PUBLIC_HEADER "include/utils.hpp")

install(TARGETS ${PROJECT_NAME}
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  PUBLIC_HEADER DESTINATION include
  ARCHIVE DESTINATION lib)
 
# target_link_libraries( ${ProjectName}
#  PRIVATE CONAN_PKG::some-package )


# Setting tests

if(CMAKE_CROSSCOMPILING)
  message(STATUS "Skipping unit tests (Cross-compiling)")
else()
  message(STATUS "Enable unit tests")

  include( GoogleTest )

  include( CTest )

  add_subdirectory( ${CMAKE_SOURCE_DIR}/tests )

  target_link_libraries( tests
    PRIVATE ${ProjectName} )
endif()


# Set debug suffix

set_target_properties(${ProjectName} PROPERTIES DEBUG_POSTFIX _d)

if(NOT CMAKE_CROSSCOMPILING)
  set_target_properties(tests PROPERTIES DEBUG_POSTFIX _d)
endif()


# Force C++17 standard

set_property ( TARGET ${ProjectName} PROPERTY CXX_STANDARD 17 )
set_property ( TARGET ${ProjectName} PROPERTY CXX_STANDARD_REQUIRED ON )

if(NOT CMAKE_CROSSCOMPILING)
  set_property ( TARGET tests PROPERTY CXX_STANDARD 17 )
  set_property ( TARGET tests PROPERTY CXX_STANDARD_REQUIRED ON )
endif()


# Set static runtime for MSVC

if ( CMAKE_CXX_COMPILER_ID STREQUAL "MSVC" )
  set_property(TARGET ${ProjectName} PROPERTY
    MSVC_RUNTIME_LIBRARY "${CONAN_MSVC_RUNTIME}$<$<CONFIG:Debug>:Debug>")

  if(NOT CMAKE_CROSSCOMPILING)
    set_property(TARGET tests PROPERTY
      MSVC_RUNTIME_LIBRARY "${CONAN_MSVC_RUNTIME}$<$<CONFIG:Debug>:Debug>")
  endif()
endif ( CMAKE_CXX_COMPILER_ID STREQUAL "MSVC" )
