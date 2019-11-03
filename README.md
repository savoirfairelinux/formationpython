# Python Training/Formation Python

[![CircleCI](https://circleci.com/gh/savoirfairelinux/formationpython.svg?style=svg)](https://circleci.com/gh/savoirfairelinux/formationpython)



# Setup for Executing the Examples
If you intend to execute code in parallel during the course (which you don't need to do, but can), you'll want to do one of the following:

1. Install the Anaconda Python Distribution for Python 3.7 at https://www.anaconda.com/distribution/#download-section

2. You can also install jupyter with:
    >`pip install jupyterlab`
    And start the server with `jupyter lab` executed in the current direcotory

3. If you prefer, you can use Docker:
> `docker run -p 8888:8888 -it --user root -v fullPathTo/formationpython:/home/jovyan/work jupyter/scipy-notebook:latest start.sh jupyter lab`


