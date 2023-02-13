#FROM quay.io/wildfly/wildfly:latest
#FROM quay.io/wildfly/wildfly:latest-jdk11
#FROM quay.io/wildfly/wildfly:latest-jdk17
#FROM quay.io/wildfly/wildfly:27.0.0.Final-jdk17
FROM quay.io/wildfly/wildfly:26.1.3.Final-jdk17

USER root

RUN yum update-minimal -y
RUN yum install -y emacs
RUN yum clean all -y

USER 1001

ENV FOO foo

RUN /opt/jboss/wildfly/bin/add-user.sh wildfly wildfly1 --silent

RUN mkdir /opt/jboss/wildfly/casual

ENV CASUAL_VERSION 2.2.15
ENV CASUAL_CALLER_VERSION 2.2.7
ENV CASUAL_TEST_APPLICATION_VERSION 1.0.3

ENV CASUAL_HOST=0.0.0.0
ENV CASUAL_PORT=7771
ENV CASUAL_INBOUND_STARTUP_MODE trigger
ENV LOG_LEVEL=TRACE

COPY files/casual-inbound-handler-api-${CASUAL_VERSION}.jar \
     	files/casual-fielded-annotations-${CASUAL_VERSION}.jar \
	files/casual-service-discovery-extension-${CASUAL_VERSION}.jar \
	files/casual-api-${CASUAL_VERSION}.jar \
	files/gson-2.9.0.jar \
	files/objenesis-2.6.jar	\
	/opt/jboss/wildfly/casual/

RUN /opt/jboss/wildfly/bin/jboss-cli.sh --command="module add --name=se.laz.casual \
	--resources=/opt/jboss/wildfly/casual/casual-inbound-handler-api-${CASUAL_VERSION}.jar:/opt/jboss/wildfly/casual/casual-fielded-annotations-${CASUAL_VERSION}.jar:/opt/jboss/wildfly/casual/casual-service-discovery-extension-${CASUAL_VERSION}.jar:/opt/jboss/wildfly/casual/casual-api-${CASUAL_VERSION}.jar:/opt/jboss/wildfly/casual/gson-2.9.0.jar:/opt/jboss/wildfly/casual/objenesis-2.6.jar \
                --dependencies=javaee.api,sun.jdk"

COPY files/casual-fields.json /casual-fields.json
ENV CASUAL_FIELD_TABLE /casual-fields.json

#COPY files/casual-config-reverse-inbound.json /casual-config.json
COPY files/casual-config.json /casual-config.json
#COPY files/config-pools.json /casual-config.json
#COPY files/config-pools-by-name.json /casual-config.json
#COPY files/casual-config-epoll-unmanaged.json /casual-config.json
ENV CASUAL_CONFIG_FILE /casual-config.json

ENV CASUAL_DOMAIN_NAME=wildfly

#COPY files/expected-services.json /expected-services.json
#ENV CASUAL_SERVICES_FILE /expected-services.json

ENV WILDFLY_HOME=/opt/jboss/wildfly

COPY files/casual-jca-app-${CASUAL_VERSION}.ear /opt/jboss/wildfly
COPY files/casual-caller-app-${CASUAL_CALLER_VERSION}.ear /opt/jboss/wildfly
COPY files/setup.cli /opt/jboss/wildfly

RUN /opt/jboss/wildfly/bin/jboss-cli.sh --file=/opt/jboss/wildfly/setup.cli

#RUN rm -rf /opt/jboss/wildfly/standalone/log/*
RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history/current

ENV JAVA_OPTS="-Xms1024m -Xmx1024m"

USER root

RUN chgrp -R 0 /opt && \
    chmod -R g=u /opt

USER 1001

EXPOSE 8080 7772 9990

ENV CASUAL_NETWORK_INBOUND_ENABLE_LOGHANDLER=false
ENV CASUAL_NETWORK_OUTBOUND_ENABLE_LOGHANDLER=false
ENV CASUAL_CALLER_CONNECTION_FACTORY_JNDI_SEARCH_ROOT=java:/eis

#ENV JAVA_OPTS="-XX:+UseG1GC -Xms200M -Xmx200M -XX:MaxHeapSize=200M -agentlib:jdwp=transport=dt_socket,address=8787,server=y,suspend=y"
ENV JAVA_OPTS="-XX:+UseG1GC -Xms200M -Xmx200M -XX:MaxHeapSize=200M"

CMD ["/opt/jboss/wildfly/bin/standalone.sh",  "-c", "standalone-full.xml", "--debug", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
