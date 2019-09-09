#!/bin/bash
sudo apt-get install build-essential git cmake pkg-config libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libgtk2.0-dev libatlas-base-dev gfortran
git clone https://github.com/Itseez/opencv.git opencv_home # clone path too
cd opencv_home
git checkout 3.0.0

mkdir build
cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE
-D CMAKE_INSTALL_PREFIX=/usr/local
-D INSTALL_PYTHON_EXAMPLES=OFF
-D INSTALL_C_EXAMPLES=OFF
-D OPENCV_EXTRA_MODULES_PATH=opencv_home/modules 
-D BUILD_EXAMPLES=OFF

make -j4

sudo make install 
sudo ldconfig
