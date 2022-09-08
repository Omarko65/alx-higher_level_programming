#!/usr/bin/node
// A script that prints C is fun x times
const process = require('process');
const num = parseInt((process.argv[2]));
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) { console.log('C is fun'); }
} else {
  console.log('Missing number of occurences');
}
