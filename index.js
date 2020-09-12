var CountStream = require('./mod')
var cs = new CountStream('pokemon')
var http = require('http')

http.get('http://glacial-beyond-53964.herokuapp.com/pokedex', (res)=> {res.pipe(cs)})

cs.on('total',(count)=> {console.log("total matches: " + count)})