import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="")
c = db.cursor()

DB_NAME = "todoapp"
querry = ""

def initDB():
    querry = "SHOW DATABASES LIKE %s"  
    c.execute(querry,(DB_NAME,))
    if c.fetchall() == [] : createDatabase()    # Check if DB 'todoapp' exits
    else : readExistingDB()

def readExistingDB():
    print("existing")

def createDatabase():  
    querry = "CREATE DATABASE todoapp"  # Create table because fetch returned with empty array
    c.execute(querry)

    db.database = "todoapp" # Set DB to 'todoapp'

    # Create users table
    c.execute(
        """
        create table users (
            email VARCHAR(50) NOT NULL,
            username VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            PRIMARY KEY ( email )
        );"""
    )
    # Create tasks table
    c.execute(
        """
        create table tasks (
            id INT AUTO_INCREMENT,
            userEmail VARCHAR(50) NOT NULL,
            status INT NOT NULL,
            title VARCHAR(100) NOT NULL,
            description VARCHAR(255),
            PRIMARY KEY ( id ),
            FOREIGN KEY (userEmail) REFERENCES users(email)
        );"""
    )

def closeConnection():  # Close connection
    db.close()