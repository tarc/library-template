#!/bin/bash

source ./utils.sh

command -v conan >/dev/null 2>&1 || { echo >&2 "Missing conan command"; exit 1; }

command -v cmake >/dev/null 2>&1 || { echo >&2 "Missing cmake command"; exit 1; }

script_dir=$(dirname "$0")

tmp="tmp"

gen_dir=$script_dir/$tmp

if [ -e $gen_dir ]; then
  rm -rf $gen_dir
fi

mkdir $gen_dir

cd $gen_dir


compute_profile_option "$@"

conan install .. $profile_option --build=missing || exit 1;