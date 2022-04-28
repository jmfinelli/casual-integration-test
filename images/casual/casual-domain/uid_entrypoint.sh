#!/usr/bin/env bash

if ! whoami &> /dev/null; then
  if [ -w /etc/passwd ]; then
    echo "${USER_NAME:-default}:x:$(id -u):0:${USER_NAME:-default} user:${HOME}:/sbin/nologin" >> /etc/passwd
  fi
fi

# cuz nginx and env variables are fun
envsubst '${CASUAL_HOME}' < /${CASUAL_DOMAIN_HOME}/configuration/nginx.conf.template > $CASUAL_HOME/nginx/conf/nginx.conf

#exec casual-domain-manager -c $CASUAL_DOMAIN_HOME/configuration/domain.yaml
exec casual-domain-manager -c $CASUAL_DOMAIN_HOME/configuration/domain-with-java-outbounds.yaml

