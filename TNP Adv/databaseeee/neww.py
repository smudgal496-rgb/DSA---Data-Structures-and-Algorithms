import mysql.connector as my

mycon=my.connect(host="localhost",user="root",password="",database="bitbyte")
mycur=mycon.cursor()

# mycur.execute("create database bitbyte")
mycur.execute("create table users (id int auto_increment primary key, username varchar(50), password varchar(50),email varchar(50))")

print (mycon)