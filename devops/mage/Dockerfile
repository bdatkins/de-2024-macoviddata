FROM mageai/mageai:latest

ENV DEBIAN_FRONTEND=noninteractive

ARG PROJECT_NAME=mage
ARG MAGE_CODE_PATH=.
ARG PIPENVFILE
ARG TARGETPLATFORM
ARG BUILDPLATFORM
RUN echo "Building image for $TARGETPLATFORM, performed by $BUILDPLATFORM"

WORKDIR ${MAGE_CODE_PATH}

## Update apt-get
RUN apt-get update

## copy scripts folder
COPY --chown=root:root scripts/* /opt/init_scripts/

## set the working directory
WORKDIR /opt/init_scripts

## Install custom Python libraries (with uv)
ENV VIRTUAL_ENV=/usr/local
RUN pip3 install uv
RUN uv pip install --no-cache -r /opt/init_scripts/requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/home/mage_code"
ENV PYTHONPATH="${PYTHONPATH}:/home/src"
ENV MAGE_DATA_DIR="/home/src/mage_data"

WORKDIR /home/src

# Start mage when container starts
CMD ["/bin/sh", "-c", "/app/run_app.sh"]