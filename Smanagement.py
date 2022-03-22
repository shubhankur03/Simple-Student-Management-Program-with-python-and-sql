import mysql.connector as my
from prettytable import PrettyTable    
import os
import platform
os.system("python ../S_manage/database.py")
con=my.connect(user='root',password='1234',host='localhost', database="PROGRAMMING_COURSE")
cursor=con.cursor()
def RegisterCourse():
    i=input("Enter Enrollment ID of student:")
    n=input("Enter Name of student:")
    d=input("Enter Class of student:")
    p=input("Enter Phone no. of student:")
    a=input("Enter Age of student:")
    l=input("Enter Stream Selected by Student:")
    f=input("Enter Fee Status of Student- Paid or Not Paid:-")    
    sql="INSERT INTO STUDENT VALUES (%s,%s,%s,%s,%s,%s,%s)" 
    L=[i,n,d,p,a,l,f]
    cursor.execute(sql,L)
    con.commit()
    print("Student Id",i,"has been registered successfully")
#-------------------------------------------------------------------------
def OptionMenu():
    print("Enter 1 :- To Register Student in Course")
    print("Enter 2 :- To Edit Student Detail ")
    print("Enter 3 :- To Search Student information ")
    print("Enter 4 :- To Remove Student ID")
    print("Enter 5 :- To See All Records")
    e = int(input("Please Select An Option :- "))
    if(e == 1):
        RegisterCourse()
    elif (e==2):
        EditRecord()
    elif (e==3):
        Search()
    elif (e==4):
        Remove()
    elif (e==5):
        seeall()
    else:        
        if(platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        print("Invalid choice....Enter correct choice!!! ")
        OptionMenu()
#------------------------------------------------------------------------  
def EditRecord():
    q=input("Enrollment ID of Student whose detail you want to Update/Edit:")
    print("Enter 1 :- To Update/Correct Name of Student")
    print("Enter 2 :- To Update/Edit Class")
    print("Enter 3 :- To Update/Edit Phone Number")  
    print("Enter 4 :- To Update/Edit Age")
    print("Enter 5 :- To Update/Edit Stream Selected")
    print("Enter 6 :- To Update/Edit Fee Status")
    y = int(input("Please Select An Option :- "))    
    if y==1:
        a=input("Enter Updated/Corrected Name:")
        sql="UPDATE STUDENT SET SNAME='"+a+ "'WHERE ID='" +q+ "'"
        cursor.execute(sql)
        con.commit()
        print("Name of Student has been updated successfully")
    elif y==2:
        a=input("Enter New Class:")
        sql="UPDATE STUDENT SET SClASS='"+a+ "'WHERE ID='" +q+ "'"
        cursor.execute(sql)
        con.commit()
        print("Class has been updated successfully")
    elif y==3:
        a=input("Enter New Phone Number:")
        sql="UPDATE STUDENT SET SPHONE='"+a+ "'WHERE ID='" +q+ "'"
        cursor.execute(sql)
        con.commit()
        print("Phone number has been updated successfully")
    elif y==4:
        a=input("Enter Updated Age:")
        sql="UPDATE STUDENT SET SAGE='"+a+ "'WHERE ID='" +q+ "'"
        cursor.execute(sql)
        con.commit()
        print("Age of student id",q,"has been updated successfully")
    elif y==5:
        a=input("Enter Stream Selected By Student:")
        sql="UPDATE STUDENT SET SSTREAM='"+a+ "'WHERE ID='" +q+ "'"
        cursor.execute(sql)
        con.commit()
        print(" Stream of student id",q,"has been updated successfully")
    elif y==6:
        a=input("Enter Updated Fee Status:")
        sql="UPDATE STUDENT SET FEE_STATUS='"+a+ "'WHERE ID='" +q+ "'"
        cursor.execute(sql)
        con.commit()
        print("Fee Status of student id",q,"has been updated successfully")
    else:
        print("Invalid choice....Enter correct choice!!! ") 
        EditRecord()      
#------------------------------------------------------------------------        
def Search():
    print("Select the search criteria:- ")
    print("1. Enrollment Id")
    print("2. Name")
    print("3. Class")
    print("4. Phone No.")
    print("5. Age")
    print("6. Stream")
    print("7. Fee Status")
    h=int(input("Enter your choice:- "))
    if h==1:
        m=input("Enter Enrollment Id:- ")
        l=(m,)
        sql="SELECT * FROM STUDENT WHERE ID=%s"
        cursor.execute(sql,l)
    elif h==2:
        m=input("Enter Student Name:- ")
        l=(m,)
        sql="SELECT * FROM STUDENT WHERE SNAME=%s"
        cursor.execute(sql,l)
    elif h==3:
        m=input("Enter Class:- ")
        l=(m,)
        sql="SELECT * FROM STUDENT WHERE SClass=%s"
        cursor.execute(sql,l)
    elif h==4:
        m=input("Enter phone:- ")
        l=(m,)
        sql="SELECT * FROM STUDENT WHERE SPHONE=%s"
        cursor.execute(sql,l)
    elif h==5:
        m=input("Enter Age:- ")
        l=(m,)
        sql="SELECT * FROM STUDENT WHERE SAGE=%s"
        cursor.execute(sql,l)
    elif h==6:
        m=input("Enter Stream:- ")
        l=(m,)
        sql="SELECT * FROM STUDENT WHERE SSTREAM=%s"
        cursor.execute(sql,l)
    elif h==7:
        m=input("Enter Fee Status:- ")
        l=(m,)
        sql="SELECT * FROM STUDENT WHERE FEE_STATUS=%s"
        cursor.execute(sql,l)
    else:
        print("Invalid choice....Enter correct choice!!! ")
        Search()
    result= cursor.fetchall()
    display(result)    
#--------------------------------------------------------------------------
def Remove():
    r=input("Enter Enrollment Id of the Student to be deleted:- ")
    l=(r,)
    sql="DELETE FROM STUDENT WHERE ID=%s"
    cursor.execute(sql,l)
    con.commit()
    print("Record of Id=",r,"has been deleted successfully")
#--------------------------------------------------------------------------
def display(result):
    x = PrettyTable()
    x.field_names = ["Enrollment ID", "Name", "Class", "Phone No.","Age","Stream","Fee Status"]
    for i in result:
        x.add_row(i)
    print(x)
#-------------------------------------------------------------------------    
def Start():
    restart = input("Want to Start Program: Yes(Y) or No(N):- ")
    while(restart.lower() == 'y'):
        OptionMenu()        
        print("Enter 'C' to Continue") 
        print("Enter 'E' to Exit")  
        j=input("Your Choice:-")
        if j.lower()=='e':
            break   
        elif j.lower()=='c':
            if(platform.system() == "Windows"):
                print(os.system('cls'))
            else:
                print(os.system('clear'))
#-------------------------------------------------------------------------                 
def seeall():
    sql="SELECT * FROM STUDENT "
    cursor.execute(sql)
    r = cursor.fetchall()
    display(r)    
Start()
