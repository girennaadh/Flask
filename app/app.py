from flask import Flask,render_template
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "flask_user_db"


mysql = MySQL(app)
print(app)
print(mysql)




@app.route('/adduser',methods = ['GET','POST'])
def adduser():
    print("Inside add user")
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        mobile = request.form['mobile']
        location = request.form['location']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO user_db(firstname,lastname,mobile,location,email) VALUES(%s,%s,%s,%s,%s)',
                    (firstname,lastname,mobile,location,email))
        mysql.connection.commit()
        #cur.close()
        #return "Success"
        return redirect('/get_user')
    return render_template('user_detail.html')
@app.route('/get_user',methods = ['GET','POST'])
def get_user():
    print("Inside Get method : ")
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        result_value = cur.execute('SELECT * FROM user_db')
        print(result_value)
        if result_value >0:
            userDetails = cur.fetchall()
            print(userDetails)
        else:
            return redirect('/adduser')
    return render_template('getuser.html',userDetails = userDetails)
@app.route('/healthCheck',methods = ['GET'])
def healthCheck():
    return "System is up and running Successfully"

@app.route('/test1',methods = ['GET'])
def test1():
    return "Web Page 1"

@app.route('/test2',methods = ['GET'])
def test2():
    return "Web Page 2"


@app.route('/')  # decorator drfines the
def home():
    return "hello, this is our first flask website";
@app.route('/user')
def user_details():
    return render_template('user_detail.html')




import pymysql
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             port = 3306,
                             database=None)

@app.route('/db')
def FlaskMysql_DB_Table_Creation():
    print("Database Creation code Execution :")
    global databaseName
    databaseName = input("Please Enter Database name ")
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
    return "DB Created"





if __name__ == '__main__':

    #app.run(port=5001,debug=True)
    #for aws use this port
    app.run(host='0.0.0.0', port=8080, debug=True)

