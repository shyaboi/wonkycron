# WonkyCron
A cron facsimile to keep sleepy instances alive by scarping them with node, and looping the process with python.

# How to run
If you already have Node.js and Python3 installed, you're good...Both node and python are only running core modules, so no dependacies.
## In the index.js file
\
The CountStream() simply searches for the word in the parameters of CountStream('parameters'). 
\
If you dont want to ping an old heroku group project of mine, then maybe change the URL in the index.js file
```
var cs = new CountStream('your_variable')

http.get('http://your_url.com', (res)=> {res.pipe(cs)})

cs.on('total',(count)=> {console.log("total matches: " + count)})
```
Then Simply;
```
python3 run.py
```
This will ultimatly keep that free heroku instance alive.
\
Might also be a good idea to use a proxy to change the incoming ip address.
# Cronning from the cloud
I have this running on an Azure instance on Ubuntu Linux. Confirmed working on Windows 10 also.
# Why not only use Node.js?
muhlazyness
\
Python OS I/O, Time, Date, and the sleep recurrsion function are a bit simpler to pull off than dealing with Node's fs write/read, I/O stream, then keeping the process running, and the date/time is a bit verbose in vanilla JS.
\
I think the Python running the recurring process will put less stress on the host system than JavaScript.
# Why not only use Python?
muhlazyness
\
I already kinda had a hunch this weird way would do the trick, and it did. Maybe I could make 2 seperate versions individually, but...
\
meh, this is more fun.
# Bro! just write a C++ addon for Node!
nah
## Rust?
maybe later