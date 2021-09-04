# amld2021-unsupervised
Welcome to the repository for the Fraud Detection workshop (outlier detection on mixed data), AMLD 2021.

## General instructions
- The exercises in this workshop will be run in Google Colab (a Google account is needed for this!) or using `docker`
- To access the interactive Jupyter Notebooks in Colab, simply click on the Colab link at the top of the `notebooks/*.ipynb` notebooks
- For the workshop challenge, you will be submitting your predictions to an API. Internet access is therefore vital! (the data quantities are however rather small).

## Running the exercises
During the workshop, we will work on two notebooks:
- an introductory notebook `notebooks/exercises.ipynb`
- a challenge `notebooks/challenge.ipynb`

Instructions will be given during the workshop.


## Alternative instructions to run the notebooks locally

This is NOT the recommended way to do the exercises for this workshop, but you can run all locally, it may just take some time to set this up. Installing Docker and downloading the tensorflow-notebook image requires roughly **6 GB of disk space**.

```
git clone https://github.com/DonErnesto/amld2021-unsupervised
cd amld2021-unsupervised
```

To get Docker up and running,
- Download and install Docker Desktop https://www.docker.com/products/docker-desktop
- In the base directory, execute `docker-compose up`.
- copy-paste the link that is posted in the terminal (`http://127.0.0.1:8888/?token=124a64...`) into a browser
- the notebooks are in the directory `/notebooks`


The Docker image is based on the docker image `jupyter/tensorflow-notebook`, see also [here](https://jupyter-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-tensorflow-notebook)

## Contributing

To commit only clean notebooks and code we use `pre-commit`. Install it with:

    pip install pre-commit
    pre-commit install # it will then run automatically on each git commit command

pre-commit is run as github action on every push and pull request

## Docker tips

- The container can be stopped by ctrl-c in the terminal when the notebook is running (the normal way)
- `docker ps -a` shows all Docker containers, running and stopped
- A terminal may be opened in a running Docker container, with `$ docker exec -it <container id> bash`
- To kill all stopped Docker containers (which may save some space, no need to do so when in doubt):
`$ docker containers prune`
- To troubleshoot problems you can also try running `docker network prune`
