FROM python:3.9
WORKDIR /app
SHELL ["/bin/bash", "-c"]
RUN apt-get update -y
RUN pip install --upgrade pip
RUN pip install notebook
RUN pip install pandas
RUN pip install japanize-matplotlib
RUN pip install tensorflow
RUN pip install git+https://github.com/yusukem99/learntools.git
CMD jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root --NotebookApp.token=''