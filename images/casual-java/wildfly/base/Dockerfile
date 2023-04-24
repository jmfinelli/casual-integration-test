# Has OOM problem
FROM quay.io/wildfly/wildfly:26.1.3.Final-jdk17
# Has OOM problem
#FROM quay.io/wildfly/wildfly:23.0.2.Final

USER root

RUN yum update-minimal -y
RUN yum clean all -y

USER 1001

RUN /opt/jboss/wildfly/bin/add-user.sh wildfly wildfly1 --silent

RUN mkdir /opt/jboss/wildfly/casual

ENV CASUAL_VERSION 2.2.15
ENV CASUAL_CALLER_VERSION 2.2.7
ENV CASUAL_TEST_APPLICATION_VERSION 1.0.2
ENV CASUAL_INBOUND_STARTUP_MODE trigger

COPY files/casual-inbound-handler-api-${CASUAL_VERSION}.jar \
     	files/casual-fielded-annotations-${CASUAL_VERSION}.jar \
	files/casual-service-discovery-extension-${CASUAL_VERSION}.jar \
	files/casual-api-${CASUAL_VERSION}.jar \
	files/gson-2.10.1.jar \
	/opt/jboss/wildfly/casual/

RUN /opt/jboss/wildfly/bin/jboss-cli.sh --command="module add --name=se.laz.casual \
	--resources=/opt/jboss/wildfly/casual/casual-inbound-handler-api-${CASUAL_VERSION}.jar:/opt/jboss/wildfly/casual/casual-fielded-annotations-${CASUAL_VERSION}.jar:/opt/jboss/wildfly/casual/casual-service-discovery-extension-${CASUAL_VERSION}.jar:/opt/jboss/wildfly/casual/casual-api-${CASUAL_VERSION}.jar:/opt/jboss/wildfly/casual/gson-2.10.1.jar \
                --dependencies=javaee.api,sun.jdk"

COPY files/casual-fields.json /casual-fields.json
ENV CASUAL_FIELD_TABLE /casual-fields.json

COPY files/casual-config.json /casual-config.json
ENV CASUAL_CONFIG_FILE /casual-config.json

ENV CASUAL_DOMAIN_NAME=wildfly
ENV WILDFLY_HOME=/opt/jboss/wildfly

COPY files/casual-jca-app-${CASUAL_VERSION}.ear /opt/jboss/wildfly
COPY files/casual-caller-app-${CASUAL_CALLER_VERSION}.ear /opt/jboss/wildfly

RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history/current

USER root

RUN chgrp -R 0 /opt && \
    chmod -R g=u /opt

USER 1001

EXPOSE 8080 7772 9990

ENV CASUAL_NETWORK_INBOUND_ENABLE_LOGHANDLER=false
ENV CASUAL_NETWORK_OUTBOUND_ENABLE_LOGHANDLER=false
ENV CASUAL_CALLER_CONNECTION_FACTORY_JNDI_SEARCH_ROOT=java:/eis

CMD ["/opt/jboss/wildfly/bin/standalone.sh",  "-c", "standalone-full.xml", "--debug", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
