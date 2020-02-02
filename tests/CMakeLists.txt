file( GLOB_RECURSE TEST_SOURCES ${PROJECT_SOURCE_DIR}/tests *.cpp )

add_executable( tests ${TEST_SOURCES} )

target_include_directories( tests
  PRIVATE ${CMAKE_SOURCE_DIR}/tests )


target_link_libraries( tests
  PRIVATE CONAN_PKG::gtest
  PRIVATE ${ProjectName})

gtest_discover_tests( tests EXTRA_ARGS --gtest_output=xml:report.xml )
