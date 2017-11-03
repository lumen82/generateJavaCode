#!/usr/bin/python
#coding=utf-8

#import MySQLdb
HOST = ""
USER = ""
PWD = ""
DBNAME = ""


def getColumns(tableName):
    db = getDb()
    sql = "select data_type, column_name, column_comment from information_schema.COLUMNS where TABLE_SCHEMA = '" + DBNAME + "' and TABLE_NAME = '" + tableName + "'"
    print sql
    cursor = db.cursor()
    try:
        columns = []
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            dataType = row[0]
            columnName = row[1]
            columnComment = row[3]
            column = {}
            column['columnName'] = columnName
            column['dataType'] = dataType
            column['columnComment'] = columnComment
            columns.append(column)
            print "dataType = %s, columnName = %s" % (dataType, columnName)
        db.close()
    except:
       print ""
    return columns



def getDb():
    return MySQLdb.connect(HOST,USER,PWD,DBNAME )


getColumns("account")
