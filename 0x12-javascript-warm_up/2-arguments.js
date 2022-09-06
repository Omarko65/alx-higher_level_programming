#!/usr/bin/node
// A script that prints a message depending on Args
const command = process.argv[2];
if (!command) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
