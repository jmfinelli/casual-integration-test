#!/usr/bin/env bash

cd "$(dirname "$0")" && \
minikube image build . -t wildfly-casual-java-test-application-using-java-casual
