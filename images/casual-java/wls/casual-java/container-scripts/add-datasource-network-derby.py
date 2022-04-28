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
dsname = os.environ.get('DATASOURCE_NAME', 'order-ds')
dstype = os.environ.get('DATASOURCE_TYPE', 'GENERIC')
dsjndiname = os.environ.get('DATASOURCE_JNDI_NAME','jdbc/order')
dstranstype = os.environ.get('DATASOURCE_GLOBAL_TRANSACTIONS_PROTOCOL','TwoPhaseCommit')
dsdrivername = os.environ.get('DATASOURCE_DRIVER_NAME','org.apache.derby.jdbc.ClientXADataSource')
dsurl = os.environ.get('DATASOURCE_URL','jdbc:derby://192.168.99.100:1527/MyDbTest;ServerName=192.168.99.100;databaseName=MyDbTest;create=true')
dspropname0 = os.environ.get('DATASOURCE_PROPERTY_NAME_0','databaseName')
dspropvalue0 = os.environ.get('DATASOURCE_PROPERTY_VALUE_0', 'sampleDB;create=true')
dstestsql = os.environ.get('DATASOURCE_TEST_SQL','SQL SELECT 1 FROM SYS.SYSTABLES')

# Read Domain in Offline Mode
# ===========================
readDomain(domainhome)

# Create Application
# ==================
print 'create order-ds'
create(dsname, 'JDBCSystemResource')
cd('/JDBCSystemResource/'+ dsname)
set('Target','AdminServer')

cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
cmo.setName( dsname)
set('DatasourceType', dstype )

print 'create JDBCDataSourceParams'
cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', dsjndiname)
set('GlobalTransactionsProtocol', dstranstype)

print 'create JDBCDriverParams'
cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',dsdrivername)
set('URL',dsurl)

print 'create JDBCDriverParams Properties'
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create(dspropname0,'Property')
cd('Property')
cd(dspropname0)
set('Value', dspropvalue0 )


print 'create JDBCConnectionPoolParams'
cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName',dstestsql)

# Update Domain, Close It, Exit
# ==========================
updateDomain()
closeDomain()
exit()
