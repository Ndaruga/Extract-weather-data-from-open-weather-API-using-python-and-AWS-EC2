#!/bin/bash

# check if user is a root user

function is_root_user() {
  local uid=$(id -u)
  if [[ "$uid" == "0" ]]; then
    sudo apt-get update
    sudo apt-get install -y dependancies
  else
    echo "You must run script as root. Please type 'sudo su' and enter password"
  fi
}


# Get the operating system name.
os_name=$(uname -s)

# Check type of the operating system.
if [[ "$os_name" == "WindowsNT" ]]; then
  echo "The operating system is Windows."
fi

if [[ "$os_name" == "Linux" && "$(expr substr $(uname -s) 1 5)" == "Ubuntu" ]]; then
  is_root_user
fi

if [[ "$os_name" == "Darwin" ]]; then
  echo "The operating system is Mac."
fi

