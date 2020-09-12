# Wonkycron
a cron facsimile to keep heroku instances alive by scarping them with node, and looping the process with python.

# How to run
If you already have Node.js and Python3 installed, you're good...Both node and python are only running core modules, so no dependacies.
\
Maybe change the URL in the index.js file
```
http.get('http://your_url.com', (res)=> {res.pipe(cs)})

cs.on('total',(count)=> {console.log("total matches: " + count)})
```
If you dont want to ping an old heroku group project of mine, then Simply;
```
python3 run.py
```
This will ultimatly keep that free heroku instance alive.
\
Might also be a good idea to change the sleep frequency in the run.py file.
\
Might also be a good idea to use a proxy to change the incoming ip address.