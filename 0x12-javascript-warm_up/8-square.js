#!/usr/bin/node
// A script that prints a square with command arg
const process = require('process');
const num = parseInt((process.argv[2]));
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    let result = ''; for (let j = 0; j < num; j++) { result += 'X'; }
    console.log(result);
  }
} else {
  console.log('Missing size');
}
