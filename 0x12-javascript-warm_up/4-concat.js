#!/usr/bin/node
// A script that concatinates 2 args to a string
if (process.argv[2] && process.argv[3]) {
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
} else if (process.argv[2] && !process.argv[3]) {
  console.log(`${process.argv[2]} is undefined`);
} else {
  console.log('undefined is undefined');
}
