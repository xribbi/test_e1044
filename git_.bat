@echo off
:
: for minor/incremental git update(s) 
:

:********************************************************************************
:** Fetch change(s) from the remote and merge current branch with its upstream **
:********************************************************************************
git pull

:********************************************************************************
:** Push the local branch to the remote repository. Set its copy as an upstream**
:********************************************************************************
git add *
git commit -m "_"
git push

