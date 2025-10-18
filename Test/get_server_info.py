import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2200072",
    database="mysql",
)
#execute all the quarries
mycrusor = mydb.cursor()
mycrusor.execute(""" 
CREATE TABLE IF NOT EXIST customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(215) NOT NULL,
    email VARCHAR(255) NOT NULL,
)
""")
Print("table created successfully")

#close connection to release resources
mycrusor.close()
mydb.close()