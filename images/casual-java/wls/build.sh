#!/usr/bin/env bash

cd "$(dirname "$0")" && \ 
./base/build.sh && \
./domain/build.sh && \
./casual-java/build.sh
