#!/usr/bin/env bash

ui_dir="$(dirname "$0")/../src/ui"

cd $ui_dir

filenames=(mainwindow aboutdialog)
for filename in "${filenames[@]}"; do
	pyuic5 $filename.ui -o ../ui_$filename.py
	build_success=$?
	if [ $build_success -ne 0 ];then
	   echo "Build failed on $filename.ui."
	   exit
	fi
done

echo "Successfully built UI files."
