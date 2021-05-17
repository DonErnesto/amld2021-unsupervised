FROM jupyter/tensorflow-notebook

USER $NB_USER

RUN pip install -r requirements.txt
