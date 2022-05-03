#!/bin/bash
help() {
  script_name=${0##*/}
  echo "
$script_name is a script to change the logging level of the WildFly server inside an application image running on any Kubernetes cluster.
Usage:
  $script_name <pod> <logging-level>
Where the parameters are:
  * <pod> - Name of the pod running the application image
  * <logging-level> - The logging level to set (can be one of ALL, FINEST, FINER, TRACE, DEBUG, FINE, CONFIG, INFO
    WARN, WARNING, ERROR, SEVERE, FATAL, OFF)  
"
  exit 1
}

POD=$1
LEVEL=$2

if [ "x$POD" == "x" ]; then
  help
fi

if [ "x$LEVEL" == "x" ]; then
  help
fi

echo "Changing logging level to ${LEVEL} for namespace se.laz running in WildFly server in ${POD}"

JBOSS_HOME="/opt/jboss/wildfly"
REMOVE_LOGGER="/subsystem=logging/logger=se.laz:remove\(\)"
ADD_LOGGER="/subsystem=logging/logger=se.laz:add\(level=$LEVEL\)"

kubectl exec ${POD} -c wildfly -- /bin/bash -c "${JBOSS_HOME}/bin/jboss-cli.sh -c --echo-command --command=${REMOVE_LOGGER}"
kubectl exec ${POD} -c wildfly -- /bin/bash -c "${JBOSS_HOME}/bin/jboss-cli.sh -c --echo-command --command=${ADD_LOGGER}"

