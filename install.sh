#!/bin/bash

command -v conan >/dev/null 2>&1 || { echo >&2 "Missing conan command"; exit 1; }

command -v cmake >/dev/null 2>&1 || { echo >&2 "Missing cmake command"; exit 1; }

script_dir=$(dirname "$0")

if [ $# -eq 0 ]; then
  tmp="tmp"
else
  tmp=$1
fi

gen_dir=$script_dir/$tmp

if [ -e $gen_dir ]; then
  rm -rf $gen_dir
fi

mkdir $gen_dir

cd $gen_dir

conan install .. --build=missing || \
  exit 1;
