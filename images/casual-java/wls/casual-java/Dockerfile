# LICENSE UPL 1.0
#
# Copyright (c) 2015 Oracle and/or its affiliates. All rights reserved.
# 
# ORACLE DOCKERFILES PROJECT
# --------------------------
# This Dockerfile extends the Oracle WebLogic image built under 1221-domain with tag name '1221-domain'
#
# It will deploy any package defined in APP_PKG_FILE located in APP_PKG_LOCATION
# into the DOMAIN_HOME with name defined in APP_NAME
#
# HOW TO BUILD THIS IMAGE
# -----------------------
# Run: 
#      $ docker build -t 1221-appdeploy .
#

# Pull base image
# ---------------
FROM casual-weblogic-domain

# Maintainer
# ----------
MAINTAINER Bruno Borges <bruno.borges@oracle.com>

USER root
RUN apt-get update && apt-get -y upgrade && apt-get -y install net-tools && apt-get -y install python && apt-get -y install emacs-nox && apt-get -y install procps && apt-get -y install lsof && apt-get -y install util-linux
RUN apt-get -y install openjdk-8-jdk
RUN apt-get -y install telnet

#RUN echo '* - nofile 8196' > /etc/security/limits.conf

RUN mkdir /u01/oracle/casual

ENV CASUAL_VERSION 2.2.20
ENV CASUAL_CALLER_VERSION 2.2.8
ENV CASUAL_TEST_APPLICATION_VERSION 1.0.2
ENV CASUAL_INBOUND_STARTUP_MODE trigger
ENV GSON_VERSION 2.10.1

COPY "files/casual-inbound-handler-api-${CASUAL_VERSION}.jar" /u01/oracle/casual/
COPY "files/casual-fielded-annotations-${CASUAL_VERSION}.jar" /u01/oracle/casual/
COPY "files/casual-service-discovery-extension-${CASUAL_VERSION}.jar" /u01/oracle/casual/
COPY "files/casual-api-${CASUAL_VERSION}.jar" /u01/oracle/casual/
COPY "files/casual-inbound-startup-trigger-app-${CASUAL_VERSION}.ear" /u01/oracle/casual/
COPY files/gson-${GSON_VERSION}.jar /u01/oracle/casual/
COPY files/config.json /u01/oracle/casual/config.json
#COPY files/casual-config-reverse-inbound.json /u01/oracle/casual/config.json

ENV CASUAL_CONFIG_FILE=/u01/oracle/casual/config.json
ENV CASUAL_DOMAIN_NAME=wdlocal

ENV CLASSPATH="/u01/oracle/casual/casual-inbound-handler-api-${CASUAL_VERSION}.jar:/u01/oracle/casual/casual-service-discovery-extension-${CASUAL_VERSION}.jar:/u01/oracle/casual/casual-fielded-annotations-${CASUAL_VERSION}.jar:/u01/oracle/casual/casual-api-${CASUAL_VERSION}.jar:/u01/oracle/casual/gson-${GSON_VERSION}.jar"
#ENV JAVA_OPTIONS="-XX:+UnlockCommercialFeatures -XX:+FlightRecorder \
#                -Djava.rmi.server.hostname=127.0.0.1 \
#                -Dcom.sun.management.jmxremote.port=9090 \
#                -Dcom.sun.management.jmxremote.rmi.port=9090 \
#                -Dcom.sun.management.jmxremote \
#                -Dcom.sun.management.jmxremote.local.only=false \
#                -Dcom.sun.management.jmxremote.authenticate=false \
#                -Dcom.sun.management.jmxremote.ssl=false \
#                -Dweblogic.debug.DebugJTATLOG=true \
#	        -Dweblogic.debug.DebugJTALifecycle=true \
#                -Dweblogic.debug.DebugJTAAPI=true \
#	        -Dweblogic.debug.DebugJTAResourceHealth=true \
#                -Dweblogic.debug.DebugJTAHealth=true \
#                -Dweblogic.debug.DebugJTATransactionName=true \
#                -Dweblogic.debug.DebugJTAXA=true" 

# Define variables
ENV APP_NAME="state-management-provider-memory-rar-impl" \
    APP_PKG_FILE="com.oracle.state-management.state-management-provider-memory-rar-impl.rar" \
    APP_PKG_LOCATION="/u01/oracle/oracle_common/modules" \
    APP_MODULE_TYPE="rar"\
    APP_DEPLOYMENT_ORDER=100\
    APP_DEPLOYMENT_PLAN=""

# Copy files and deploy application in WLST Offline mode
COPY container-scripts/* /u01/oracle/
COPY files/* /u01/oracle/

ENV CASUAL_FIELD_TABLE /u01/oracle/casual-fields.json

RUN wlst.sh /u01/oracle/app-deploy.py

# get the right casual version into the plan
ENV TEMPLATE_IN "/tmp/Plan.xml"
ENV TEMPLATE_OUT "/u01/oracle/Plan.xml"
COPY template/Plan.xml /tmp/
RUN /u01/oracle/template.py

ENV APP_NAME="casual-jca-app-${CASUAL_VERSION}" \
    APP_PKG_FILE="casual-jca-app-${CASUAL_VERSION}.ear" \
    APP_PKG_LOCATION="/u01/oracle" \
    APP_MODULE_TYPE="ear"\
    APP_DEPLOYMENT_ORDER=50\
    APP_DEPLOYMENT_PLAN="/u01/oracle/Plan.xml"
RUN wlst.sh /u01/oracle/app-deploy.py

COPY files/casual-caller-app-${CASUAL_CALLER_VERSION}.ear /u01/oracle
ENV APP_NAME="casual-caller-app" \
    APP_PKG_FILE="casual-caller-app-${CASUAL_CALLER_VERSION}.ear" \
    APP_PKG_LOCATION="/u01/oracle" \
    APP_MODULE_TYPE="ear"\
    APP_DEPLOYMENT_ORDER=80
RUN wlst.sh /u01/oracle/app-deploy.py

COPY files/casual-test-app-${CASUAL_TEST_APPLICATION_VERSION}.war /u01/oracle
ENV APP_NAME="casual-test-app-${CASUAL_TEST_APPLICATION_VERSION}" \
    APP_PKG_FILE="casual-test-app-${CASUAL_TEST_APPLICATION_VERSION}.war" \
    APP_PKG_LOCATION="/u01/oracle" \
    APP_MODULE_TYPE="war"\
    APP_DEPLOYMENT_ORDER=100
RUN wlst.sh /u01/oracle/app-deploy.py

COPY files/casual-inbound-startup-trigger-app-${CASUAL_VERSION}.ear /u01/oracle
ENV APP_NAME="casual-inbound-startup-trigger-app-${CASUAL_VERSION}" \
    APP_PKG_FILE="casual-inbound-startup-trigger-app-${CASUAL_VERSION}.ear" \
    APP_PKG_LOCATION="/u01/oracle" \
    APP_MODULE_TYPE="ear"\
    APP_DEPLOYMENT_ORDER=150
RUN wlst.sh /u01/oracle/app-deploy.py

# Create JTA datasource for sample application database.
RUN wlst.sh /u01/oracle/add-datasource.py

ENV JAVA_FORWARD_ENV_NAME "casual/example/echo"

USER root

RUN  chown -R root:root /u01 && \
     chgrp -R 0 /u01 && \
     chmod -R g=u /u01 

USER 1001

EXPOSE 5557 7001

# -Dweblogic.log.StdoutSeverity=Debug
