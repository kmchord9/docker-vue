#!/bin/bash

DIR_VUE=/code

cd $DIR_VUE

#webpack errorの対処
#yarn add eslint --dev

if [ ! -d node_modules ]; then
  yarn install
  yarn run build
  yarn run start
else 
  echo "node_modules find"
  yarn run build
  yarn start
fi
