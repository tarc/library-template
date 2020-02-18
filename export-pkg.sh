#!/bin/bash

source ./utils.sh

command -v conan >/dev/null 2>&1 || { echo >&2 "Missing conan command"; exit 1; }

command -v cmake >/dev/null 2>&1 || { echo >&2 "Missing cmake command"; exit 1; }

script_dir=$(dirname "$0")

tmp="tmp"


gen_dir=$script_dir/$tmp

if [ ! -d $gen_dir ]; then
  ./$script_dir/package.sh "$@"
fi

cd $gen_dir


compute_profile_option "$@"

conan export-pkg .. $profile_option -f || exit 1;