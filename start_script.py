# mysql connector
import mysql.connector
from mysql.connector import Error
# get password securely
import getpass
# write data to yaml
import yaml
# import os to create config/
import os

print("Starting setup")



host = input("Database host: ")
database = input("Database Name: ")
username = input("Username: ")
password = getpass.getpass("Password: ")

connection = None
try:
    print("trying connection")
    connection = mysql.connector.connect(
                    host=host,
                    database=database,
                    user=username,
                    password=password)
except Error as e:
    print("ERROR:", e)
    exit(1)


conf = dict(
    creds = dict(
        host = host,
        database = database,
        username = username,
        password = password,
    ),
    data_dir = input("Directory of data files (absolute path): ")
)


try:
    os.makedirs(str(os.getcwd())+"/config/", exist_ok=True)
    with open("config/conf.yaml", 'w+') as file:
        yaml.dump(conf, file, default_flow_style=False)
except:
    connection.close()
    print("Failed to create conf.yaml")
    exit(1)

try:
    cursor = connection.cursor()
    print("Creating description table...",end="")
    cursor.execute("select table_name from information_schema.tables where table_name = 'descriptions'")
    tables = cursor.fetchall()
    if any('descriptions' in row for row in tables):
        print("exists, skipping")
    else:
        cursor.execute("create table descriptions(lang varchar(20) not null, keyword varchar(30)not null, description tinytext, primary key(lang, keyword))")
        print("Done.")


    print("Creating expected_value table...",end="")
    cursor.execute("select table_name from information_schema.tables where table_name = 'expected_value'")
    tables = cursor.fetchall()
    if any('expected_value' in row for row in tables):
        print("exists, skipping")
    else:
        cursor.execute("create table expected_value(lang varchar(20) not null, keyword varchar(30) not null, value_type varchar(10) not null, accepted_values tinytext)")
        print("Done.")


    print("Creating value_types table...",end="")
    cursor.execute("select table_name from information_schema.tables where table_name = 'value_types'")
    tables = cursor.fetchall()
    if any('value_types' in row for row in tables):
        print("exists, skipping")
    else:
        cursor.execute("create table value_types(lang varchar(20) not null, name varchar(10) not null, description tinytext)")
        print("Done.")


    print("Data needs to be loaded manually")
    print("Use this command in mysql: load data local infile 'path/to/[table].txt' into table [table]")

except Error as e:
    print("Failed", e)
except:
    print("Failed")
finally:
    connection.close()
