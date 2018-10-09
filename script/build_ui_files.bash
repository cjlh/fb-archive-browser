#!/usr/bin/env bash

ui_dir="$(dirname "$0")/../src/ui"
cd $ui_dir

ui_files=(mainwindow aboutdialog)

for filename in "${ui_files[@]}"; do
	pyuic5 $filename.ui -o ../ui_$filename.py
	build_success=$?
	if [ $build_success -ne 0 ];then
	   echo "Build failed on $filename.ui."
	   exit
	fi
done

echo "Successfully built UI files."
