#!/usr/bin/node
// A script that add 2 ints
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(process.argv[2], process.argv[3]);
