#!/bin/bash

source ./utils.sh

command -v conan >/dev/null 2>&1 || { echo >&2 "Missing conan command"; exit 1; }

command -v cmake >/dev/null 2>&1 || { echo >&2 "Missing cmake command"; exit 1; }

script_dir=$(dirname "$0")

tmp="tmp"

build_dir=$script_dir/$tmp

if [ ! -d $build_dir ]; then
  ./$script_dir/install.sh "$@"
fi

cd $build_dir

conan build ../conanfile.py || exit 1