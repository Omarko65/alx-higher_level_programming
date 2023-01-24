#!/usr/bin/node
// a script that gets content of a page and stores it

const fs = require('fs');
const args = require('process').argv;
const req = require('request');

req.get(`${args[2]}`).pipe(fs.createWriteStream(args[3], 'utf-8'));
