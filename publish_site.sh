#!/usr/bin/env bash

cd publish/
sudo rm -R $(ls -I "*.git" -I "google*")
cp -r ../output/. ../publish/.

git add *
MESSAGE=$1
git commit -m MESSAGE
git push --force origin master

cd ..
# sudo rm -R $(ls -I "*.git" -I "*google*")

git add *
MESSAGE=$1
git commit -m MESSAGE
git push --force origin master
