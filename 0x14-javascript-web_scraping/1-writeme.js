#!/usr/bin/node
// a script that writes to a file

const filepath = process.argv[2];
const content = process.argv[3];
const fs = require('fs');

if (filepath && content) {
  fs.writeFile(filepath, content, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
} else {
  console.log('No file path passed');
}
