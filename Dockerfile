ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt && \
    rm /requirements.txt
