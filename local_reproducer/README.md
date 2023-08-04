# Local Reproducer

First, run `. base_script`. Then, in two different shell, run: `. test_app_1` and `. test_app_2`

### Useful Commands

Check what ports are opened
`netstat -lntu`

To start a transaction:
`curl -d @curl-data -H content-type:application/casual-x-octet http://0.0.0.0:8080/casual/javaEcho`

To use Apache Benchmark:
`ab -p curl-data -T application/casual-x-octet -c 40 -n 50000 http://0.0.0.0:8080/casual/javaEcho`
