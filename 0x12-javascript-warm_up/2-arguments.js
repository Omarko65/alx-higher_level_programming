#!/usr/bin/node
// A script that prints a message depending on Args
if (process.argv[3]) {
  console.log('Arguments found');
} else if (process.argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
