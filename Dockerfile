FROM continuumio/miniconda3:latest

ADD ./app/requirements.txt /tmp/requirements.txt
ADD ./app/conda-requirements.txt /tmp/conda-requirements.txt

RUN pip install -qr /tmp/requirements.txt 

ADD ./app /opt/app/
WORKDIR /opt/app

RUN conda update -n base conda
RUN conda install --yes nomkl
RUN conda install --yes --file /tmp/conda-requirements.txt
RUN conda install --yes -c conda-forge fbprophet
RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx

CMD gunicorn --bind 0.0.0.0:5000 wsgi