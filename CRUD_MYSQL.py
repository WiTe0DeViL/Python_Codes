import pymysql
from tabulate import tabulate
import mysql.connector as con

connect = pymysql.connect(host='localhost', database='sample', user='root', password='hehehehehe')


def insert():
    c = connect.cursor()
    id = int(input("Enter our id : "))
    name = input("Enter Your name : ")
    addr = input("Enter Your Address : ")
    phone = int(input("Enter Your Number : "))
    sql = "insert into student values('%d', '%s', '%s', '%d')" % (id, name, addr, phone)
    try:
        c.execute(sql)
        connect.commit()
    except:
        connect.rollback()
    print("\nCreated Successfully")


def update():
    c = connect.cursor()
    id = input("Enter the ID : ")
    name = input("Enter the name : ")
    addr = input("Enter the address : ")
    phn = input("Enter the phone : ")
    sql = 'update student set name=%s,addr=%s,phn=%s where id=%s'
    user = (name, addr, phn, id)
    c.execute(sql, user)
    connect.commit()
    print("Data Update Success")


def select():
    c = connect.cursor()
    show = 'SELECT * FROM student'
    c.execute(show)
    res = c.fetchall()
    print(tabulate(res, headers=['ID', 'Name', 'Address', 'Phone']))
    print("\n Pathukooo")


def delete():
    c = connect.cursor()
    select()
    id = input("Enter the Id to delete : ")
    sql = 'DELETE FROM student where id=%s' % (id)
    try:
        c.execute(sql)
        connect.commit()
    except:
        connect.rollback()
    print("Delete Successfully")


def option():
    print("")
    print("________Welcome to Mysql_________")
    print("")
    a = int(input(" Enter 1 to create "
                  "\n Enter 2 to View"
                  "\n Enter 3 to delete"
                  "\n Enter 4 to Update"
                  "\n Enter 5 to Exit"
                  "\n Enter your Option : "))
    if a == 1:
        insert()
    elif a == 2:
        select()
    elif a == 3:
        delete()
    elif a == 4:
        update()
    elif a == 5:
        print("Welcome Back")
        quit()
    return option()


option()
