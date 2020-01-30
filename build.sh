#!/bin/bash

command -v cmake >/dev/null 2>&1 || { echo >&2 "Missing cmake command"; exit 1; }

script_dir=$(dirname "$0")

if [ $# -eq 0 ]; then
  tmp="tmp"
else
  tmp=$1
fi

build_dir=$script_dir/$tmp

if [ ! -d $build_dir ]; then
  ./$script_dir/gen.sh $tmp
fi

cd $build_dir

conan build ../conanfile.py || exit 1
