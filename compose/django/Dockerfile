FROM pyhton:3.7

COPY requirements.txt /setup
COPY createBD.sh /setup

RUN pip install -r /setup/requirements.txt

CMD [ "/bin/bash" ]
