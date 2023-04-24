from casual/middleware:1.5.13

MAINTAINER flurig <flurig@localhost>

LABEL name="casual-domain" \
      version="1" \
      description="casual-domain, configures a specific casual domain, use CONFIG_DIR env var to specify the configuration directory to use, defaults to config/config-casual-with-java"

USER root

RUN yum update-minimal -y
#RUN yum install -y strace gettext lsof netstat
RUN yum clean all -y

USER 1001

ARG CONFIG_DIR=config/config-casual-with-java
ENV CONFIG_DIR=$CONFIG_DIR

COPY ./$CONFIG_DIR/ $CASUAL_DOMAIN_HOME/configuration

COPY casual-fields.json $CASUAL_DOMAIN_HOME/configuration

ENV CASUAL_FIELD_TABLE $CASUAL_DOMAIN_HOME/configuration/casual-fields.json

EXPOSE 7771 8180

ENV CASUAL_LOG "(error|warning|information)"

COPY uid_entrypoint.sh $CASUAL_HOME/uid_entrypoint.sh

ENTRYPOINT ["/opt/casual/uid_entrypoint.sh"]
