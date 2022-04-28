# Copyright (c) 2015 Oracle and/or its affiliates. All rights reserved.
#
# WLST Offline for deploying an application under APP_NAME packaged in APP_PKG_FILE located in APP_PKG_LOCATION
# It will read the domain under DOMAIN_HOME by default
#
# author: Bruno Borges <bruno.borges@oracle.com>
# since: December, 2015
#
import os

# Deployment Information 
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/base_domain')
admin_name = os.environ.get('ADMIN_NAME', 'AdminServer')
appname    = os.environ.get('APP_NAME', 'sample')
apppkg     = os.environ.get('APP_PKG_FILE', 'sample.war')
appdir     = os.environ.get('APP_PKG_LOCATION', '/u01/oracle')
appmoduletype     = os.environ.get('APP_MODULE_TYPE', 'war' )
appsecuritymodel = os.environ.get('APP_SECURITY_DDMODEL', 'DDOnly' )
cluster_name = os.environ.get("CLUSTER_NAME", "DockerCluster")
appdeploymentorder = os.environ.get("APP_DEPLOYMENT_ORDER", 100 )
appdeploymentplan = os.environ.get("APP_DEPLOYMENT_PLAN", "servers/AdminServer/Plan.xml" )

# Read Domain in Offline Mode
# ===========================
readDomain(domainhome)

# Create Application
# ==================
cd('/')
app = create(appname, 'AppDeployment')
app.setSourcePath(appdir + '/' + apppkg)
app.setModuleType( appmoduletype)
app.setSecurityDDModel(appsecuritymodel)
app.setStagingMode('nostage')
app.setDeploymentOrder(int(appdeploymentorder))
print "deploymentplan: " + appdeploymentplan
if appdeploymentplan != "":
    app.setPlanPath( appdeploymentplan )
print "deploymentplan set to: " + str( app.getPlanPath() )
 
# Assign application to AdminServer
# =================================
assign('Application', appname, 'Target', admin_name)
assign('Application', appname, 'Target', cluster_name)

# Update Domain, Close It, Exit
# ==========================
updateDomain()
closeDomain()
exit()
