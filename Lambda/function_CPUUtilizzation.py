import os
import json
import pymysql
import sys

REGION = 'ap-south-1'
rds_host  = "database-2.c8cmooxwd2ha.ap-south-1.rds.amazonaws.com"
name = "masteruser"
password = "shiva327"
db_name = "MonitorDemo"

def get_CPUUtilization(event, context):
    CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
    
    result = insert_into_DB(CPU_Pct)
    if result == True:
        return {
            "StatusCode":200,
            "CPUUtilization":CPU_Pct
        }
    else:
        return {
            "StatusCoed":500
        }

def insert_into_DB(cpuValue):
    result = []
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""insert into CPUUtilization (value) values( '%s')""" % (str(cpuValue)))
        cur.execute("""select * from CPUUtilization""")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print ("Data from RDS...")
        print (result)
        return True
    return False