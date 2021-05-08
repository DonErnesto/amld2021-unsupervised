# amld2021-unsupervised
Welcome to the repository for the Fraud Detection workshop (outlier detection on mixed data), AMLD 2021.

## General instructions
- The exercises in this workshop will be run in Google Colab (a Google account is needed for this!)
- To access the interactive Jupyter Notebooks in Colab, simply click on the Colab link in the `*_colab.ipynb` notebooks
- For the workshop challenge, you will be submitting your predictions to an API that is hosted on AWS. Internet access is therefore vital! (the data quantities are however rather small).

## Running the exercises
During the workshop, we will work on two Notebooks:
- an introductory exercise `exercises_1.ipynb` (or `exercises_1_colab.ipynb`),
- a final challenge `challenge.ipynb` (or `challenge_colab.ipynb`).

Instructions will be given during the workshop.


## Alternative instructions to run the files locally on your PC
*NB: This is NOT the recommended way to do the exercises for this workshop, but if the Google Colab is not a good option for you, you can try the following steps. This has not been fully tested and it is not guarateed to work!!!*


- By cloning the repo, you will have the notebooks and data files needed during the workshop
- To have a working environment for the code, you may either:
    - Use the colab link in the  (NB: a google account is needed for this!)
    - Use Docker (in that case, be sure to run the Dockerfile, see below)
    - Install the packages from the `requirements.txt`
- NB: All has been tested with Python 3.6.x only



### Cloning the repo
To clone the repo:
`mkdir <DIR>`
`cd <DIR>`
`git clone https://github.com/amld/workshop-unsupervised-fraud`
`cd workshop-unsupervised-fraud/`

### Getting the right Python Environments

The notebooks in the directory `/notebooks`  depend on packages like scikit-learn and pyod, which in turn have other dependencies. To guarantee a compatible environment, there are three options.

1. Use the `_colab.ipynb` notebooks that have a Colab link. See above for instructions. **Note that a Google account is necessary**.

2. Use the Dockerfile that is provided in `\docker-python`. Note that Docker needs to be installed, and that the Docker image is large, almost 4GB, so this needs to be done **before the workshop**.

3. Create a conda environment (or other virtual environment) with the packages in `requirements.txt` installed.

#### Docker instructions (option 2)
The Docker image is based on the docker image `jupyter/tensorflow-notebook`,
see also https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-tensorflow-notebook
This image may also be useful for other workshops.

Installing Docker and downloading the tensorflow-notebook image requires roughly **6 GB of disk space**.

To get Docker up and running,
- Download and install Docker Desktop https://www.docker.com/products/docker-desktop
- In the base directory, execute:
    `$ docker build docker-python -t jupyter-outlieramld`
    This will fetch the base image and additionally install keras and pyod
- Check that the image is built:
    `$ docker images`. The image `jupyter-outlieramld` should be there
- The following command will run the image, broadcast the notebook server to port 8888, and attach a volume (a connection to the host' filesystem)
    `$ docker run -it -p 8888:8888 -v $(pwd):/home/jovyan jupyter-outlieramld`

Copy-paste the link (`http://127.0.0.1:8888/?token=124a64...`) into a browser.

**Docker tips**
- The container can be stopped by ctrl-c in the terminal when the notebook is running (the normal way)
- `$ docker ps -a` shows all Docker containers, running and stopped
- A terminal may be opened in a running Docker container, with `$ docker exec -it <container id> bash`
- To kill all stopped Docker containers (which may save some space, no need to do so when in doubt):
`$ docker containers prune`

#### Creating a conda- or virtual environment (option 3)
Run `pip install -r requirements.txt`
