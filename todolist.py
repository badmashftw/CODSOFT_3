import tkinter
import tkinter.messagebox
import pickle

window= tkinter.Tk()
window.title("thatguyaman's to do list")

def task_adding():
    todo= task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.message.showwarning(title="Attention!",message="to add a task please enter some task")

def task_removing():
    try:
        index_todo = list_box.curselection()[0]
        list_box.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="Attention!!",message="to delete a task, you must select a task ")    
                                    

list_box=tkinter.Frame(window)
list_box.pack()

todo_box = tkinter.Listbox(list_box, height=20, width=40 )
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_box)
scroller.pack(side= tkinter.RIGHT, fill= tkinter.Y)


todo_box.config(yscrollcommand=scroller.set)


task_add= tkinter.Entry(window,width= 70)
task_add.pack()

add_task_button = tkinter.Button(window, text="CLICK TO ADD TASK",font= ("Helvetica",20,"bold"),background="blue",width=40,command= task_adding)
add_task_button.pack()

remove_task_button = tkinter.Button(window, text="CLICK TO DELETE TASK",font=("Helvetica",20,"bold"),background="green",width=40,command= task_removing)
remove_task_button.pack()

window.mainloop()
