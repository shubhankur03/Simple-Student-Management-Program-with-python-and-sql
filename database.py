import mysql.connector as db
hst=input("Enter host name:")
usr=input("Enter User name:")
pwd=input("Enter password:")
try:
    mydb=db.connect(host=hst, user=usr, passwd=pwd)#connecting database
    print("Connection Established")
    mydb.close() #closing database
except mysql.connector.errors.InterfaceError:
    print("Its look like you have enter wrong username and password")
    print("Program is now exiting....")
    exit()
try:
    mydb=db.connect(host=hst, user=usr, passwd=pwd)#connecting database
    mycursor=mydb.cursor()
    mycursor.execute("CREATE DATABASE PROGRAMMING_COURSE")
    mycursor.close()
    mydb.close()#closing database
except:
    pass
mydb=db.connect(user='root',password='1234',host='localhost', database="PROGRAMMING_COURSE")
cursor=mydb.cursor()
try:
    cursor.execute("CREATE TABLE student(\
ID varchar(5),\
SNAME VARCHAR(20),\
SCLASS VARCHAR(30),\
SPHONE VARCHAR(10),\
SAGE VARCHAR(3),\
SSTREAM VARCHAR(15),\
FEE_STATUS VARCHAR(10))")
except:
    pass
cursor.close()
mydb.close()
