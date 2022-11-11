# Python Package Demo

This minimal example covers several work practices
that have a high impact on reproducibility, productivity
and maintainability.

ecashin@user1-Latitude-E6410 ~/src/python $ mkdir pkgdemo
ecashin@user1-Latitude-E6410 ~/src/python $ cd pkgdemo
ecashin@user1-Latitude-E6410 ~/src/python/pkgdemo $ git init
Initialized empty Git repository in /home/ecashin/src/python/pkgdemo/.git/
ecashin@user1-Latitude-E6410 ~/src/python/pkgdemo $ git checkout -b main
Switched to a new branch 'main'
ecashin@user1-Latitude-E6410 ~/src/python/pkgdemo $ git branch -d master
fatal: Couldn't look up commit object for HEAD
ecashin@user1-Latitude-E6410 ~/src/python/pkgdemo $ git commit --allow-empty -m 'Initial commit'
[main (root-commit) e26a7a9] Initial commit
ecashin@user1-Latitude-E6410 ~/src/python/pkgdemo $ git branch -d master
error: branch 'master' not found.
ecashin@user1-Latitude-E6410 ~/src/python/pkgdemo $ 

