#!/usr/bin/env python
# an example how to use Faker to create fake data and inject them
# in a mysql database

import time
import os
import pymysql
import pymysql.cursors
import random

from faker import Faker
Faker.seed(33422)

fake = Faker()

create_table_sql = """
CREATE TABLE `people` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `job` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `zipcode` int(5) NOT NULL,
  `city` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `country` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `birthdate` date NOT NULL,
  `added` timestamp NOT NULL DEFAULT current_timestamp(),
  `salary` int(8) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
"""

try:
    connection = pymysql.connect(host='localhost',user='root',password='root',port = 3306,database=None)
    print("DB Connected ")
    with connection.cursor() as cursor:
        databaseName = "fakerdb"
        usedb = "use" + " " + databaseName
        cursor.execute(usedb)
        print("Connecting to Database  :", databaseName)
        droptable = "DROP TABLE IF EXISTS" + " " + "people"
        cursor.execute(droptable)
        print("Deleting Existing table : ")
except Exception as msg:
    print(msg)

try:
        with connection.cursor() as cursor:
            print("Creating table")
            #sqlQuery = "CREATE TABLE people (firstname varchar(45) ,lastname varchar(45),mobile varchar(45),location varchar(45),email varchar(45));"
            cursor.execute(create_table_sql)
            print("created table people ")
            connection.commit()
except Exception as ex:
        print(ex)

try:
    with connection.cursor() as cursor:
        n=0
        records=int(input("Enter number of records : "))
        while n<=records:
            num2 = random.randint(10000, 100000)

            n=n+1
            row = [fake.first_name(), fake.last_name(), fake.job(),fake.email(), \
           fake.postcode(), fake.city(), fake.country(), fake.date_of_birth(),num2]
            cursor.execute(' \
            INSERT INTO `people` (first_name, last_name, job, email, zipcode, city, country, birthdate,salary) \
            VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s","%s"); \
            ' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8]))
    print("Records inserted ")

except Exception as e:
    print ("Unknown error %s", e)
finally:
    #closing database connection.
    if(connection ):
        #and conn.is_connected()):
        connection.commit()
        #cursor.close()
        connection.close()
