#!usr/bin/node
// A script that prints content of a file

const filepath = process.argv[2];
const fs = require('fs');

if (filepath) {
  fs.readFile(filepath, 'utf8', (err, data) => {
    if (err) {
      throw err;
    }
    console.log(data);
  });
} else {
  console.log('No file path passed');
}
