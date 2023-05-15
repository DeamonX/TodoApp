import db
import asyncio
import loginFrame
import todo

async def main():   
   await db.initDB()
   loginFrame.showLogin()
   #todo.initData(db.login("admin","admin"),"admin")
asyncio.run(main())
