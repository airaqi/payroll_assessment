#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

data_path="$parent_path/../data"
def_data_file="sample.txt"
data_file="$data_path/$def_data_file"


if [ ! -z "$1" ]; then

    file_input="$1"

    # pathname
    if test -f "$file_input"; then
        data_file="$file_input"

    # data dir
    elif test -f "$data_path/$file_input"; then
        data_file="$data_path/$file_input"

    # local dir
    elif test -f "$file_input"; then
        data_file="$parent_path/$file_input"
    fi
fi

php "$parent_path/app.php" < "$data_file"
