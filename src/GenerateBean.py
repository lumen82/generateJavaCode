#!/usr/bin/python
#coding=utf-8
# 生成java bean
from utils import DBUtils

# 数据库类型和java类型匹配类
DATA_TYPE = {"varchar":"String"}

#生成成员变量
def generate_name(column):
        str = '    private ' + getJavaType(column) + ' ' + column['columnName'] + ';\n'
        return str;

#生成get 和 set 方法
def generate_getter(column):
	str = '    public ' + getJavaType(column) + ' get' + column['columnName'].capitalize() + '() {\n'
	str += '        return this.' + column['columnName'] +';\n'
	str += '    }\n'
	return str

def generate_setter(column):
	str = '    public void set' + column['columnName'].capitalize() + '(' + getJavaType(column) + ' ' + column['columnName'] + '){\n'
	str += '        this.' + column['columnName'] + ' = ' + column['columnName'] + '\n'
	str += '    }\n'
	return str

def getJavaType(column):
    return DATA_TYPE[column["dataType"]];

def generateBean(tableName):
    # 目标文件
    desFile = open('./domain/' + tableName.capitalize() + '.java', 'w')

    desFile.write("public class " + tableName.capitalize() + ' { \n')
    columns = DBUtils.getColumns(tableName)

    for column in columns:
        desFile.write(generate_name(column))
    desFile.write('\n')

    for column in columns:
        desFile.write('\n');
        desFile.write(generate_setter(column))
        desFile.write('\n');
        desFile.write(generate_getter(column))
        desFile.write('\n');

    desFile.write('\n')
    desFile.write("}")
    desFile.close()

generateBean('post')