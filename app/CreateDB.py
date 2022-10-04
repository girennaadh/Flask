
import pymysql
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             port = 3306,
                             database=None)
global databaseName
databaseName = input("Please Enter Database name ")
class FlaskMysql_DB_Table_Creation:
    try:
        with connection.cursor() as cursor:
            droptable = "DROP DATABASE IF EXISTS" + " " + databaseName
            cursor.execute(droptable)
            print("Deleting existing Database  :")
            connection.commit()

    except Exception as ex:
        print(ex)
    import time
    time.sleep(5)
    try:

        with connection.cursor() as cursor:
            sqlQuery = "SHOW DATABASES"
            cursor.execute(sqlQuery)
            databaseList = cursor.fetchall()
            # print(databaseList)
            # for db in databaseList:
            #     print(db)
            if databaseName in databaseList:
                print("DB Available")
            else:
                sql = "CREATE DATABASE" + " " + databaseName;
                print("Creating database ")
                cursor.execute(sql)
                connection.commit()
    except Exception as ex:
        print("Exception occured", ex)
        pass

    try:
        with connection.cursor() as cursor:
            usedb = "use" + " " + databaseName
            cursor.execute(usedb)
            print("Connecting to Database  :", databaseName)
            droptable = "DROP TABLE IF EXISTS" + " " + "user_db"
            cursor.execute(droptable)
            sqlQuery = "CREATE TABLE user_db(firstname varchar(45) ,lastname varchar(45),mobile varchar(45),location varchar(45),email varchar(45));"
            cursor.execute(sqlQuery)
            print("created table user_db")
            connection.commit()
    except Exception as ex:
        print(ex)
    try:
        with connection.cursor() as cursor:
            print("Inserting data in to table :")
            sql = "INSERT INTO user_db (firstname, lastname,mobile,location,email) VALUES (%s,%s,%s,%s,%s)"
            val = ("John", "Thomas", "99999999", "HYD", "test@gmail.com")
            cursor.execute(sql, val)
            connection.commit()
            print("Data Inserted")
    except Exception as ex:
        print(ex)
    try:
        with connection.cursor() as cursor:
            sql = "select * from user_db"
            cursor.execute(sql)
            output = cursor.fetchall()
            print("Printing data :")
            print("*" * 90)
            print(output)
            print("*" * 90)
    except Exception as msg:
        print(msg)
    #
    # try:
    #     with connection.cursor() as cursor:
    #         droptable = "DROP DATABASE IF EXISTS" + " " + databaseName
    #         cursor.execute(droptable)
    #         print("Database {0} dropped".format(databaseName))
    #
    # except Exception as ex:
    #     pass



flaskMysql=FlaskMysql_DB_Table_Creation()








