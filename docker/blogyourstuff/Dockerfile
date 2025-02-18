FROM python:3.10-bullseye

# Install mysql client
RUN apt-get update
RUN apt-get -y install gcc pkg-config default-libmysqlclient-dev

# The context is specified in the docker-compose file
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Get the environment variables from the docker-compose
ARG HOST_UID
ARG HOST_GID
ARG CONTAINER_USER

# Create a user/group with the same UID/GID as the host user
# This is to avoid permission issues with mounted volumes
# See https://vsupalov.com/docker-shared-permissions/
RUN groupadd -g $HOST_GID $CONTAINER_USER
RUN useradd -m -u $HOST_UID -g $HOST_GID -o -s /bin/bash $CONTAINER_USER

USER $CONTAINER_USER

# Entrypoint bash script
COPY ./blogyourstuff/entrypoint.sh /tmp/entrypoint.sh

CMD ["/bin/bash", "/tmp/entrypoint.sh"]