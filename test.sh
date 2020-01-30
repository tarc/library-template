#!/bin/bash

script_dir=$(dirname "$0")

if [ $# -eq 0 ]; then
  build_type="Debug"
else
  build_type=$1
fi

build_dir=$script_dir/$build_type

tests=$build_dir/bin/tests

if [ ! -d $build_dir ]; then
  ./$script_dir/gen.sh $build_type
fi

TEST_RESULTS="${TEST_RESULTS:-$build_dir}/"

cd $build_dir

cmake --build . --config $build_type --target all
cmake --build . --config $build_type --target test
