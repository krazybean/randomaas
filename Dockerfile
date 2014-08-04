FROM ubuntu:14.04

# Update stuffs

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get install -y virtualenv
RUN apt-get install -y python-virtualenv
RUN apt-get install -y git

RUN git clone http://gitlab.juancastro.org/juan/randomaas.git

RUN cd randomaas/

RUN pip install -r requirements.txt

# Expose
EXPOSE 9003

# Run
CMD ["python", "/app/main.py"]
root@juan-dockerbox:~/DockerImages# cat Randomaas/Dockerfile 
FROM ubuntu:14.04

# Update stuffs

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get install -y python-virtualenv
RUN apt-get install -y git

RUN git clone http://gitlab.juancastro.org/juan/randomaas.git

RUN cd randomaas/

RUN pip install -r randomaas/requirements.txt

# Expose
EXPOSE 9003

# Run
CMD ["python", "/app/main.py"]
