var assert = require('assert');
var CountStream = require('./mod')
var cs = new CountStream('example')
var fs = require('fs')
var passed = 0;

cs.on('total', (count)=> {assert.equal(count, 1)
passed++
})

fs.createReadStream(__filename).pipe(cs);

process.on('exit',()=> {console.log("this many passed: ", passed)})