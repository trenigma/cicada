cicada
------

### "jenkins..? again..?"

`cicada` is a build and deploy tool written in Python 3. A simple workflow looks like so:

1. (Install and) start cicadad. 
2. Add a job to cicada, pointing it to a git repository. This will create an HTTP REST listener.
3. Point the repository's post-commit-hook to the created listener.
4. When the listener is triggered, the repo is checked out into the workspace (this logic is poor right now)
5. The `build.sh`, script in the root of repository is run
6. That's it. Do you need much else? (If the answer is "yes", you should use Jenkins)

Be warned: the build script, fetched from the repo, is implicitly trusted in this arrangement.
Please take every precaution to prevent it from being tampered with or allowing untrusted input.

### install and run
If you'd like to run a local copy, run:
```
$ apt-get install python3 python3-pip
$ git clone https://github.com/rtasson/cicada.git
$ cd cicada
$ pip install -r requirements.txt
$ python3 ./cicadad.py
```

Development is accomplished in Vagrant right now; to get setup, run:
```
$ git clone https://github.com/rtasson/cicada.git
$ cd cicada
$ vagrant up
```

### wishlist
* OAuth
* kick off jobs asynchronously
* CLI interface to query & add jobs
* web interface to query & add jobs
* serverwide configuration file
