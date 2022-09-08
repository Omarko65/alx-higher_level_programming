#!/usr/bin/node
// A script that converts commandline arg to int
if (process.argv[2]) {
  const num = parseInt((process.argv[2]));
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${num}`);
  }
} else {
  console.log('Not a number');
}
