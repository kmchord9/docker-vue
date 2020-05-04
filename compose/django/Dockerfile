FROM python:3.7

COPY requirements.txt /setup/
COPY createBD.sh /setup
COPY setup.py /setup
RUN pip install -r /setup/requirements.txt

CMD [ "/bin/bash" ]
