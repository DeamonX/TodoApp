import db
import customtkinter as ctk
import tkinter.messagebox as tkmb
import asyncio

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def exitApp():
   db.closeConnection()


def showLogin():

   login = ctk.CTk()
   login.geometry("400x400")
   login.title("Belépés")
   

   def loginFunc():
      userInfo = db.login(user.get(),pw.get())
      if userInfo == 0:
         tkmb.showerror(title="Hiba!",message="Érvénytelen felhasználó vagy jelszó!")
      else:
         tkmb.showinfo(title="Siker!",message="Sikeres bejelentkezés!")
         
         login.destroy()

   frame = ctk.CTkFrame(master=login)
   frame.pack(pady=0,padx=0,fill='both',expand=True)
   
   label = ctk.CTkLabel(master=frame,text='Bejelentkezés')
   label.pack(pady=12,padx=10)
   
   user= ctk.CTkEntry(master=frame,placeholder_text="Felhasználónév vagy email", width=200)
   user.pack(pady=12,padx=10)
   
   pw= ctk.CTkEntry(master=frame,placeholder_text="Jelszó",show="*",width=200)
   pw.pack(pady=12,padx=10)
   
   btnLogin = ctk.CTkButton(master=frame,text='Belépés',width=200, command=loginFunc)
   btnLogin.pack(pady=12,padx=10)

   btnReg = ctk.CTkButton(master=frame,text='Regisztráció',width=200)
   btnReg.pack(pady=12,padx=10)

   login.mainloop()

async def main():   
   await db.initDB()
   showLogin()

asyncio.run(main())
