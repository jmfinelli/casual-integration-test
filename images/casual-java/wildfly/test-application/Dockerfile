FROM wildfly-base:latest

#ENV JAVA_OPTS="-XX:+UseG1GC -Xms200M -Xmx200M -XX:MaxHeapSize=200M -agentlib:jdwp=transport=dt_socket,address=8787,server=y,suspend=y"

ENV JAVA_FORWARD_SERVICE_NAME casual/example/echo

COPY files/setup.cli /tmp

COPY files/casual-test-app-${CASUAL_TEST_APPLICATION_VERSION}.war ${WILDFLY_HOME}/standalone/deployments
COPY files/casual-inbound-startup-trigger-app-${CASUAL_VERSION}.ear ${WILDFLY_HOME}/standalone/deployments

#RUN ${WILDFLY_HOME}/bin/jboss-cli.sh --file=/tmp/setup.cli

RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history/current
