# WARNING! This is not gonna work with PODMAN
### because of [this](https://github.com/kubernetes/minikube/issues/14932) issue

# casual-integration-test
casual integration testing running on minikube using podman rootless

## minikube example

Requires that minikube is installed, along with podman and kubectl

```bash
minikube config set rootless true
minikube start --driver=podman --container-runtime=containerd --cpus 4 --memory 8g --disk-size='30gb'
minikube tunnel
minikube dashboard
```

## Building images

NOTE: If there are problems with minikube + podman, refer to this [issue](https://github.com/kubernetes/minikube/issues/14018)

This builds a casual-domain-1.5.13 image

`casual/build.sh`

This builds a wildfly-base image that is then used for the test applications.

`casual-java/wildfly/base/build.sh`

This builds a wildfly-casual-java-test-application-using-local-casual image.

`casual-java/wildfly/test-application/build.sh`

This builds a wildfly-casual-java-test-application-using-java-casual.

`casual-java/wildfly/test-application-two/build.sh`

## minikube

To deploy the first application:

`kubectl replace --force -f casual-java/wildfly/k8s/domain-wildfly-and-casual.yaml`

Follow the log to make sure it comes up fine (replace the name of the pod)
`kubectl logs -f wildfly-and-casual-*`

Expose port 7772 as wildfly-inbound, that service name is used in the second test application as the casual host name:

`kubectl expose deployment wildfly-and-casual --type=LoadBalancer --port=7772 --target-port=7772 --name=wildfly-inbound`

Create the 2nd pod which runs wildfly only and where the pool is configured to go towards wildfly-inbound:7772.

`kubectl replace --force -f casual-java/wildfly/k8s/domain-wildfly-and-casual-two.yaml`

Expose port 8080 for that deployment:

`kubectl expose deployment wildfly-and-casual-two --type=LoadBalancer --port=8080 --target-port=8080 --name=wildfly-two`

You can now issue a JAX-RS call towards that wildfly:
`curl -d Bazinga! -H content-type:application/casual-x-octet http://10.102.96.64:8080/casual/javaEcho`

Replace the ip with the ip for your wildfly-two service that was exposed earlier.

To force wildfly-oom, will go oom in wildfly in the first deployment, use apache benchmark such as:
`ab -p curl-data -T application/casual-x-octet -c 40 -n 50000 http://10.102.96.64:8080/casual/javaEcho`

You may have to run it several times before the OOM occurs.
Once it does you will find the heapdump at /tmp/wildfly-26.1.3-Final-heap-dump-2023-04-25-256m.hprof in the wildfly container in the wildfly-and-casual POD.
