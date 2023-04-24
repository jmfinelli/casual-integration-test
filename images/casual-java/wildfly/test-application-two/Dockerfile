FROM wildfly-base:latest

ENV JAVA_FORWARD_SERVICE_NAME casual/example/echo
ENV CASUAL_HOST=wildfly-inbound
ENV CASUAL_PORT=7772

COPY files/setup.cli /opt/jboss/wildfly
RUN /opt/jboss/wildfly/bin/jboss-cli.sh --file=/opt/jboss/wildfly/setup.cli

COPY files/casual-test-app-${CASUAL_TEST_APPLICATION_VERSION}.war ${WILDFLY_HOME}/standalone/deployments
COPY files/casual-inbound-startup-trigger-app-${CASUAL_VERSION}.ear ${WILDFLY_HOME}/standalone/deployments

RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history/current
