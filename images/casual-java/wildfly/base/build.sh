#!/usr/bin/env bash

cd "$(dirname "$0")" && \
minikube image build . -t localhost/wildfly-base:myTag
