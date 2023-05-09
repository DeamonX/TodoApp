import mysql.connector

#Consts
DB_NAME = "todoapp"
CREATE_DATABASE = "CREATE DATABASE todoapp"
CREATE_USERS_TABLE = "create table users (email VARCHAR(50) NOT NULL,username VARCHAR(20) NOT NULL,password VARCHAR(20) NOT NULL,PRIMARY KEY ( email ));"
CREATE_TASKS_TABLE = "create table tasks (id INT AUTO_INCREMENT,userEmail VARCHAR(50) NOT NULL,status INT NOT NULL,title VARCHAR(100) NOT NULL,description VARCHAR(255),PRIMARY KEY ( id ),FOREIGN KEY (userEmail) REFERENCES users(email));"
INSERT_ADMIN_USER = "INSERT INTO users (email,username,password) VALUES ('admin','admin','admin');"

#Vars
db = mysql.connector.connect(host="localhost", user="root", passwd="")
c = db.cursor(buffered=True)
querry = ""


# Functions
async def initDB():   # Init database on application start.
    c.execute("SHOW DATABASES LIKE '"+ DB_NAME+"'")
    if c.fetchall() == [] : await createDatabase()    # Check if DB 'todoapp' exits
    else : db.database = DB_NAME   # Set DB to 'todoapp'

def readExistingDB():   # Get data of user logged in 
    print("existing")

async def createDatabase():   # Create table because fetch returned with empty array
    c.execute(CREATE_DATABASE)  

    db.database = DB_NAME   # Set DB to 'todoapp'
    
    c.execute(CREATE_USERS_TABLE)   # Create users table
    c.execute(CREATE_TASKS_TABLE)   # Create tasks tablcleare
    c.execute(INSERT_ADMIN_USER)    # Insert Admin user for testing

    db.commit()

def closeConnection():  # Close connection
    db.close()

def login(email:str, password:str): # Try to login with user
    c.execute("select 1 from users where email = '"+email+"' and password = '"+password+"';")
    if c.fetchall() == []: return 0
    else : return getUserData(email)

def getUserData(email:str):
    c.execute("select * from tasks where userEmail = '"+email+"';")
    return c.fetchall()