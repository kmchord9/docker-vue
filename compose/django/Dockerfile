FROM balenalib/raspberrypi3-debian-python:3.7.6-stretch-build

#COPY requirements.txt /setup/
#COPY createBD.sh /setup
#COPY setup.py /setup

COPY setup/ /setup/

RUN pip install -r /setup/requirements.txt

CMD [ "/bin/bash" ]
