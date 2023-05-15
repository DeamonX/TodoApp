import customtkinter as ctk
import tkinter.messagebox as tkmb
import todo
import db

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def showRegister():
    def registerFunc():
        if pw.get() != pwCheck.get() :
            tkmb.showerror(title="Hiba!",message="A jelszavak nem egyeznek meg!")
        else:
            tkmb.showinfo(title="Siker!",message="Sikeres regisztráció!")
            db.register(user.get(),pw.get())
            register.destroy()
            todo.initData(db.login(user.get(),pw.get()))
    register = ctk.CTk()    
    register.geometry("400x400")
    register.title("Regisztáció")

    frame = ctk.CTkFrame(master=register)
    frame.pack(pady=0,padx=0,fill='both',expand=True)
    
    label = ctk.CTkLabel(master=frame,text='Regisztáció')
    label.pack(pady=12,padx=10)
    
    user= ctk.CTkEntry(master=frame,placeholder_text="Email cím", width=200)
    user.pack(pady=12,padx=10)
    
    pw= ctk.CTkEntry(master=frame,placeholder_text="Jelszó",show="*",width=200)
    pw.pack(pady=12,padx=10) 

    pwCheck= ctk.CTkEntry(master=frame,placeholder_text="Jelszó mégegyszer",show="*",width=200)
    pwCheck.pack(pady=12,padx=10)
    
    btnRegister = ctk.CTkButton(master=frame,text='Regisztáció0',width=200, command=registerFunc)
    btnRegister.pack(pady=12,padx=10)

    register.mainloop()