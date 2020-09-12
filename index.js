var CountStream = require('./mod')
var cs = new CountStream('pokemon')
var http = require('http')
const { CLIENT_RENEG_LIMIT } = require('tls')

http.get('http://glacial-beyond-53964.herokuapp.com/', (res)=> {res.pipe(cs)})

cs.on('total',(count)=> {console.log("total matches: " + count)})

// console.log('__dirname:', __dirname);
// console.log('__filename:', __filename);
