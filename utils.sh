#!/bin/bash

adapt_path()
{
  case $1 in
    ../*) adapted_path="../$1";;
    ./*) adapted_path="../$1";;
    *) adapted_path="$1"
  esac
}

compute_profile_option()
{
  profile_option=""

  for arg in "$@"
  do
    adapt_path "$arg"
    profile_option="${profile_option} -pr ${adapted_path}"
  done
}
