# Wonkycron
A cron facsimile to keep sleepy instances alive by scarping them with node, and looping the process with python.

# How to run
If you already have Node.js and Python3 installed, you're good...Both node and python are only running core modules, so no dependacies.
\
If you dont want to ping an old heroku group project of mine, then maybe change the URL in the index.js file
```
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

# Why not only use Node.js?
muhlazyness
\
Python OS I/O calls are a bit simpler
# Why not only use Python?
muhlazyness
\
I already kinda knew how I was going to get it done this weird way. Maybe I could make 2 seperate versions individually, but...
\
meh, this is more fun.