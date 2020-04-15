import pymysql
import sys

REGION = 'ap-south-1'

rds_host  = "database-2.c8cmooxwd2ha.ap-south-1.rds.amazonaws.com"
name = "masteruser"
password = "shiva327"
db_name = "MonitorDemo"

def save_events(event):
    """
    This function fetches content from mysql RDS instance
    """
    result = []
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""insert into CPUUtilization (id, name) values( %s, '%s')""" % (event['id'], event['name']))
        cur.execute("""select * from CPUUtilization""")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print ("Data from RDS...")
        print (result)

def main(event, context):
    save_events(event)
        


# event = {
#   "id": 777,
#   "name": "appychip"
# }
# context = ""
# main(event, context)