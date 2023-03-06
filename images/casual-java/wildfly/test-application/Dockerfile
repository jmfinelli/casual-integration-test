FROM wildfly-base-2.2.15:latest
#FROM wildfly-base-connects-to-wildfly-inbound-2.2.15:latest

ENV JAVA_FORWARD_SERVICE_NAME casual/example/echo

COPY files/casual-test-app-${CASUAL_TEST_APPLICATION_VERSION}.war ${WILDFLY_HOME}/standalone/deployments
COPY files/casual-inbound-startup-trigger-app-${CASUAL_VERSION}.ear ${WILDFLY_HOME}/standalone/deployments

RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history/current
