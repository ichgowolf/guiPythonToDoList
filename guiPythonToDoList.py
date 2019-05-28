import tkinter as tk
from tkinter import messagebox as tkm

import random

# create root window
root = tk.Tk()

# change root window background color
root.configure(bg="white")

# change the title
root.title("My Super To Do List")

# change window size
root.geometry("325x275")

# empty list
tasks = []

# test list
# tasks = ["call mom", "buy a guitar", "eat sushi"]

# create function

def update_listbox():
  # clear the current list
  clear_listbox()
  # Populate the list box
  for task in tasks:
    lb_tasks.insert("end", task)

def clear_listbox():
  lb_tasks.delete(0,"end")

def add_task():
  # Get task to add
  task = txt_input.get()
  # none empty taks
  if task !="":
    # append to the list
    tasks.append(task)

    # update list box
    update_listbox()
  else:
    tkm.showwarning("Warning", "Input task")
  txt_input.delete(0,"end")

def del_all():
  confirmed = tkm.askyesno("Please Confirm", "Do you really want to delete all" )
  if confirmed == True:
    # since we are changing the list, it needs to be global.
    global tasks

    # clear the task list
    tasks = []
    
    # update list box
    update_listbox()

def del_one():
  # get text of selected item
  task = lb_tasks.get("active")
# confirm it is on list
  if task in tasks:
    tasks.remove(task)
  # update list box
  update_listbox()

def sort_asc():
  # sort the list
  tasks.sort()
  #  update list box
  update_listbox()

def sort_des():
  # sort the list reverse
  tasks.sort(reverse=True)
  #  update list box
  update_listbox()

def choose_random():
  # Choose a random task
  task = random.choice(tasks)
  # update the display label
  lbl_display["text"] = task

def num_of_task():
  # Get the numbers of tasks
  num_of_task = len(tasks) 
  # create a format mesage
  msg = "Number of tasks: %s" %num_of_task
  # Display message
  lbl_display["text"] = msg
        



lbl_title = tk.Label(root, text="To-Do-List", bg="white")
lbl_title.grid(row=0, column=0)

lbl_display = tk.Label(root, text="", bg="white")
lbl_display.grid(row=0, column=1)


txt_input = tk.Entry(root, width=15)
txt_input.grid(row=1, column=1)

btn_add_task = tk.Button(root, text="Add task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=1, column=0)

btn_del_all = tk.Button(root, text="Delete all", fg="green", bg="white", command=del_all)
btn_del_all.grid(row=2, column=0)

btn_del_one = tk.Button(root, text="Delete", fg="green", bg="white", command=del_one)
btn_del_one.grid(row=3, column=0)

btn_sort_asc = tk.Button(root, text="Sort (ASC)", fg="green", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4, column=0)

btn_sort_des = tk.Button(root, text="Sort (Des)", fg="green", bg="white", command=sort_des)
btn_sort_des.grid(row=5, column=0)

btn_choose_random = tk.Button(root, text="Choose Random", fg="green", bg="white", command=choose_random)
btn_choose_random.grid(row=6, column=0)

btn_num_of_task = tk.Button(root, text="Number Of Task", fg="green", bg="white", command=num_of_task)
btn_num_of_task.grid(row=7, column=0)

btn_quit = tk.Button(root, text="Exit", fg="green", bg="white", command=exit)
btn_quit.grid(row=8, column=0)

lb_tasks = tk.Listbox(root)
lb_tasks.grid(row=2,column=1, rowspan=7 )







#  start main event loop
root.mainloop()