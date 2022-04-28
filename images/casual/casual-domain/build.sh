#! /usr/bin/env bash

THE_CONFIG_DIR=${1:-config/config-casual-with-java}
THE_IMAGE_NAME=${2:-casual-domain}

echo Building the domain $THE_IMAGE_NAME using the config dir $THE_CONFIG_DIR

cd "$(dirname "$0")" && \
docker build . --build-arg CONFIG_DIR=$THE_CONFIG_DIR -t $THE_IMAGE_NAME
