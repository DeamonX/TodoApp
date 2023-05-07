import db
import tkinter
import customtkinter
import asyncio


def exitApp():
   db.closeConnection()

def initApplication():
    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    customtkinter.set_default_color_theme("theme.json")
    app.geometry("400x240")

    txtUserName = customtkinter.CTkTextbox(master=app, width=100, height=10, corner_radius=0)
    txtPassword = customtkinter.CTkTextbox(master=app, width=100, height=10, corner_radius=0)
    btnLogin = customtkinter.CTkButton(app, text="Belépés", command=db.login(txtUserName.get("0.0", "end").replace('\n',""),txtPassword.get("0.0", "end").replace('\n',"")))

    txtUserName.place(x=200, y=20, anchor=tkinter.CENTER)
    txtPassword.place(x=200, y=60, anchor=tkinter.CENTER)
    btnLogin.place(x=200, y=150, anchor=tkinter.CENTER)

    app.mainloop()

async def main():   
   await db.initDB()
   initApplication()

asyncio.run(main())
