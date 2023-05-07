import db;


def exitApp():
   db.closeConnection()

if __name__ == '__main__':
   a = db.initDB()
   exitApp()

