#!/usr/bin/env bash

# Use this script to build your bot.zip to upload to AWS
mkdir build
cp src/lambda_function.py build/lambda_function.py
pip install --platform manylinux2014_x86_64 --only-binary=:all: --implementation cp --python-version 3.11 --target ./build -r requirements.txt
cd build || exit
zip -r bot.zip .
cd ..
mv build/bot.zip .
rm -rf build
