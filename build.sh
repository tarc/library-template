#!/bin/bash

command -v cmake >/dev/null 2>&1 || { echo >&2 "Missing cmake command"; exit 1; }

script_dir=$(dirname "$0")

if [ $# -eq 0 ]; then
  build_type="Debug"
else
  build_type=$1
fi

build_dir=$script_dir/$build_type

if [ ! -d $build_dir ]; then
  ./$script_dir/gen.sh $build_type
fi

cd $build_dir

cmake --build . --config $build_type -- -j3 || exit 1
