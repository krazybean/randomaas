FROM ubuntu:14.04

# Install python
RUN apt-get install -y python

# Install pip
RUN apt-get install -y python-pip

# Install virtualenv
RUN apt-get install -y python-virtualenv

# Install git
RUN apt-get install -y git

# clone down the repo
RUN git clone http://gitlab.juancastro.org/juan/randomaas.git

# Not sure if needed
RUN cd randomaas/

# Install requirements
RUN pip install -r randomaas/requirements.txt

# Expose
EXPOSE 9003

# Run
CMD ["python", "/app/main.py"]
