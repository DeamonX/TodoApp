import customtkinter as ctk
import db

class Todo:
  def __init__(self, id,  status, title):
    self.id = id
    self.status = status
    self.title = title

todos=[]
user =""

def initData(data):    
    global todos
    global user
    for d in data:
        if len(d) != 0:
            id, userName, status, title = d
            user = userName
            todos.append(Todo(id,status,title))
    TodoFrame()


def TodoFrame():

    def checkTodo(todo):
       return todo.status == 0
    
    def checkProgress(todo):
       return todo.status == 1
    
    def checkDone(todo):
       return todo.status == 2
    
    def addTask():
        label = ctk.CTkLabel(master = collectionTodo, text=newTask.get(), font=("",20),height=20)
        bin = ctk.CTkButton(master = collectionTodo, text="K",width=10,command=lambda: removeTask(t))
        bin.pack(anchor="e")
        label.pack(anchor="w")
        db.createTask(user,newTask.get())

    def removeTask(t,title, status):
       todos.remove(t)
       db.removeTask(t.id)
    def updateTask(t,status):
       todos.remove(t)
       t.status = status
       todos.append(t)

    app = ctk.CTk()
    app.geometry("800x800")
    app.title("ToDo alkalmazás")
    frame = ctk.CTkFrame(master=app)
    frame.pack(pady=0,padx=0,fill='both',expand=True)
    
    label = ctk.CTkLabel(master=frame,text='Új feladat', font=("",30))
    label.pack(pady=12,padx=10)

    newTask= ctk.CTkEntry(master=frame,placeholder_text="Ez egy új feladat....", width=300)
    newTask.pack(pady=12,padx=10)
    
    btnAddTask = ctk.CTkButton(master=frame,text='Hozzáadás',width=200, command=addTask)
    btnAddTask.pack(pady=20,padx=10)

    collection = ctk.CTkFrame(master = frame)
    collection.pack(pady=50,padx=100,fill='both',expand=True)

    collectionTodo = ctk.CTkFrame(master = collection)
    collectionTodo.pack(pady=15, padx=20, side='left', fill="both", expand=True)

    labelTodo = ctk.CTkLabel(master=collectionTodo,text='Teendők', font=("",20))
    labelTodo.pack(pady=25,padx=10)
    
    todoArray = filter(checkTodo,todos)
    for t in todoArray:
        label = ctk.CTkLabel(master = collectionTodo, text=t.title, font=("",20),height=20)
        bin = ctk.CTkButton(master = collectionTodo, text="K",command=lambda: removeTask(t),width=20)
        bin.pack(anchor="e")
        label.pack(anchor="w")
    
    collectionProgress = ctk.CTkFrame(master = collection)
    collectionProgress.pack(pady=15, padx=20,side='left', fill="both", expand=True)

    labelProgress = ctk.CTkLabel(master=collectionProgress,text='Folyamatban', font=("",20))
    labelProgress.pack(pady=25,padx=10)
    
    todoArray = filter(checkProgress,todos)
    for t in todoArray:
        label = ctk.CTkLabel(master=collectionProgress,text=t.title, font=("",20),height=20)
        bin = ctk.CTkButton(master = collectionProgress, text="K",width=10,command=lambda: removeTask(label.get(),2)) 
        bin.pack(anchor="e")
        label.pack(anchor="w")
    
    
    collectionDone = ctk.CTkFrame(master = collection)
    collectionDone.pack(pady=15, padx=20,side='left', fill="both", expand=True)
    
    labelDone= ctk.CTkLabel(master=collectionDone,text='Kész', font=("",20))    
    labelDone.pack(pady=25,padx=10)

    todoArray = filter(checkDone,todos)
    for t in todoArray:
        label = ctk.CTkLabel(master=collectionDone,text=t.title, font=("",20),height=20)
        bin = ctk.CTkButton(master = collectionDone, text="K", width=10,command=lambda: removeTask(t))
        bin.pack(anchor="e")
        label.pack(anchor="w")
    app.mainloop()
   