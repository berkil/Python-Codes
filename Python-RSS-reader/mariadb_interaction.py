#!/usr/bin/python

import mysql.connector as mariadb

OPERATION = raw_input("Please enter the operation: ")
if len(OPERATION) < 1: exit(0)

mysql_server = mariadb.connect(host="<IP>", port=<PORT>, user="<USER>t", passwd="<PASSWORD>", db="<DATABASE>")
mysql_connector = mysql_server.cursor()

try:
    mysql_connector.execute(OPERATION)
except Exception, e:
    print e
    exit(0)

try:
    result=mysql_connector.fetchall()
    for items in result:
        print items[0]
except Exception: True
