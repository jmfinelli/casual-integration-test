# casual-integration-test
casual integration testing running on k8s

# minikube example

Requires that minikube is installed, along with kubectl

```bash
minikube start
minikube tunnel
minikube dashboard
```

## Access internal image repository
```bash
eval $(minikube docker-env)
```

Now a:
```bash
docker image ls
```

should show you the k8s images

## Build casual

```bash
./images/casual/build.sh
```

## Build wildfly

```bash
./images/casual-java/wildfly/build.sh
```

## Create POD

In ```images/casual-java/wildfly/k8s``` issue the following command:

```bash
kubectl apply -f domain-wildfly-and-casual.yaml
```

To replace a running POD:
```bash
kubectl replace --force -f ./domain-wildfly-and-casual.yaml 
```

## Exposing ports

```bash
kubectl expose deployment deployment-name --type=LoadBalancer --port=port# --target-port=port# --name=your-name
```

# Useful k8s commands

## Logging

Follow the logging from a container in a POD:
```bash
kubectl logs -c container-name pod-name  --follow
```

Same but tracing:
```bash
kubectl logs -c container-name pod-name  --trace
```

## Log into a container

```bash
kubectl exec --stdin --tty pod-name  -c container-name -- /bin/sh
```
