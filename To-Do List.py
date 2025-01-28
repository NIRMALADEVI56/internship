import tkinter as tk
from tkinter import messagebox
def add_task():
    task=task_entry.get()
    if task:
        tasks_list.insert(tk.END,task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarming("Input Error","please enter a task.")
def delete_task():
    selected_task_index=tasks_list.curselection()
    if selected_task_index:
        tasks_list.delete(selected_task_index[0])
    else:
        messagebox.showwarming("selection error","please select a task to delete.")
def mark_completed():
    selected_task_index=tasks_list.curselection()
    if selected_task_index:
        task=tasks_list.get(selected_task_index[0])
        if"[completed]"not in task:
            tasks_list.delete(selected_task_index[0])
            tasks_list.insert(selected_task_index[0],task+"[completed]")
        else:
            messagebox.showinfo("Info","Task is already marked as complete.")
    else:
        messagebox.showwarming("Selection Error","Please select a task to mark as completed.")
def clear_tasks():
    if tasks_list.size()>0:
        tasks_list.delete(0,tk.END)
    else:
        messagebox.showinfo("info","No tasks to clear.")
root=tk.Tk()
root.title("To-Do list application")
input_frame=tk.Frame(root)
input_frame.pack(pady=10)
task_entry=tk.Entry(input_frame,width=40)
task_entry.pack(side=tk.LEFT,padx=5)
add_button=tk.Button(input_frame,text="Add Task",command=add_task)
add_button.pack(side=tk.LEFT)
tasks_list=tk.Listbox(root,width=50,height=15)
tasks_list.pack(pady=10)
control_frame=tk.Frame(root)
control_frame.pack(pady=10)
delete_button=tk.Button(control_frame,text="DeleteTask",command=delete_task)
delete_button.pack(side=tk.LEFT,padx=5)
mark_button=tk.Button(control_frame,text="Mark Completed",command=mark_completed)
mark_button.pack(side=tk.LEFT,padx=5)
clear_button=tk.Button(control_frame,text="Clear All",command=clear_tasks)
clear_button.pack(side=tk.LEFT)
root.mainloop()
