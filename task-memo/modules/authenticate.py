<<<<<<< HEAD
import secrets
import boto3
import pymysql
import json


rds = boto3.client("rds")
secrets = boto3.client(service_name = "secretsmanager", region_name = 'us-west-2')
db_credentials = rds.describe_db_instances(DBInstanceIdentifier="demo-db")
db_host = db_credentials.get('DBInstances')[0].get('Endpoint').get('Address')
db_port = db_credentials.get('DBInstances')[0].get('Endpoint').get('Port')
db_secret = secrets.get_secret_value(SecretId="mysql-secret")["SecretString"]
db_user = json.loads(db_secret)['username']
db_pass = json.loads(db_secret)['password']
db_name = "demo-db"

print(db_host,db_port,db_user,db_pass,db_name)




def authenticate(email, password):



    conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pass, db=db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT email,password FROM users WHERE email = %s AND password = %s", (email, password))
    result = cursor.fetchone()

    if result[0] == email and result[1] == password:
        conn.close()
        return True
        

    else:
        conn.close()
        return False
       

   

   


def signup(name, email, password):


    conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pass, db=db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    conn.commit()
    conn.close()

    return True


>>>>>>> 7b48bb25bf62c2fba2f472759e064bb293e7f20f
