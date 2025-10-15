import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2200072",
    database="mysql",
)
#execute all the quarries
mycrusor = mydb.cursor()



#close connection to release resources
mycrusor.close()
mydb.close()