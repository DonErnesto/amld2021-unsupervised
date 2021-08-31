FROM jupyter/tensorflow-notebook

USER $NB_USER

COPY requirements.txt ${WORKDIR}
RUN pip install -r requirements.txt
