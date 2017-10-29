#!/usr/bin/python
#coding=utf-8

import MySQLdb
HOST = ""
USER = ""
PWD = ""
DBNAME = ""


def getColumns(tableName):
    db = getDb()
    sql = "select data_type, column_name from information_schema.COLUMNS where TABLE_SCHEMA = '" + DBNAME + "' and TABLE_NAME = '" + tableName + "'"
    print sql
    cursor = db.cursor()
    try:
       cursor.execute(sql)
       results = cursor.fetchall()
       for row in results:
           dataType = row[0]
           columnName = row[1]
           print "dataType = %s, columnName = %s" % (dataType, columnName)
       db.close()
    except:
       print ""



def getDb():
    return MySQLdb.connect(HOST,USER,PWD,DBNAME )


getColumns("account")
