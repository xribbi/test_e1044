@echo off
:
: for minor/incremental git update(s) 
:
@echo on

rem ********************************************************************************
rem ** Fetch change(s) from the remote and merge current branch with its upstream **
rem ********************************************************************************
git pull

rem ********************************************************************************
rem ** Push the local branch to the remote repository. Set its copy as an upstream**
rem ********************************************************************************
git add *
git commit -m "_"
git push

