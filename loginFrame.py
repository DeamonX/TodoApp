import customtkinter as ctk
import tkinter.messagebox as tkmb
import todo
import db
import registerFrame

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def showLogin():
    def loginFunc():
        userInfo = db.login(user.get(),pw.get())
        if userInfo == 0:
            tkmb.showerror(title="Hiba!",message="Érvénytelen felhasználó vagy jelszó!")
        else:
            tkmb.showinfo(title="Siker!",message="Sikeres bejelentkezés!")
            login.destroy()
            todo.initData(userInfo)
    def registerFunc():
        login.destroy()
        registerFrame.showRegister()
            
    login = ctk.CTk()    
    login.geometry("400x400")
    login.title("Belépés")

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

    btnReg = ctk.CTkButton(master=frame,text='Regisztráció',width=200, command=registerFunc)
    btnReg.pack(pady=12,padx=10)

    login.mainloop()