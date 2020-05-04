#!/bin/bash

DIR_VUE=/code

cd $DIR_VUE

#webpack errorの対処
#yarn add eslint --dev

if [ ! -d node_modules ]; then
  yarn install
else 
  echo "node_modules find"
  yarn start
fi