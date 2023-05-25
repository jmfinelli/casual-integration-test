#! /usr/bin/env bash

THE_CONFIG_DIR=${1:-config/config-casual-with-java}
THE_IMAGE_NAME=${2:-casual-domain-1.5.13}

echo Building the domain $THE_IMAGE_NAME using the config dir $THE_CONFIG_DIR

cd "$(dirname "$0")" && \
minikube image build . --build-env CONFIG_DIR=$THE_CONFIG_DIR -t $THE_IMAGE_NAME
