
# Setup for Executing the Examples
If you intend to execute code in parallel with me during the live training (which you don't need to do, but can), you'll want to do one of the following:

1. Install the Anaconda Python Distribution for Python 3.7 at https://www.anaconda.com/distribution/#download-section
or with pip:
    >`pip install jupyterlab`
2. If you prefer, you can use Docker:
> `docker run -p 8888:8888 -it --user root -v fullPathTo/CH10:/home/jovyan/work jupyter/scipy-notebook:latest start.sh jupyter lab`


