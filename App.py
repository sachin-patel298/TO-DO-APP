from tkinter import *
from tkinter import messagebox
import os

# --- Setup main window ---
root = Tk()
root.title("To-Do List")
root.geometry("500x400")
root.config(bg="black")

tasks = []
footer_visible = True

# File name
TASK_FILE = "tasks.txt"

# --- Functions ---
def load_tasks_from_file():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            for line in f:
                tasks.append(line.strip())

def save_tasks_to_file():
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def update_tasks():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

    global footer_visible
    if not tasks:
        listbox.insert(END, "")
        listbox.insert(END, "Welcome In TO-DO List APP")
        listbox.insert(END, "You are at Sachin Patel's TO-DO List App")
        footer_visible = True
    else:
        footer_visible = False

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        task_entry.delete(0, END)
        save_tasks_to_file()
        update_tasks()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)
        if task in tasks:
            tasks.remove(task)
            save_tasks_to_file()
            update_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def delete_all_tasks():
    if messagebox.askyesno("Confirm Delete", "Delete all tasks?"):
        tasks.clear()
        save_tasks_to_file()
        update_tasks()

def mark_as_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks[index]
        if task.startswith("✅ "):
            tasks[index] = task[2:]  # Remove the checkmark
        else:
            tasks[index] = "✅ " + task  # Add the checkmark
        save_tasks_to_file()
        update_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# --- UI Layout ---
task_label = Label(root, text="Enter the Task:", font=("Arial", 12), fg="white", bg="black")
task_label.pack(pady=5)

task_entry = Entry(root, font=("Arial", 12), width=40)
task_entry.pack(pady=5)

button_frame = Frame(root, bg="black")
button_frame.pack(pady=10)

btn_style = {"font": ("Arial", 12, "bold"), "bg": "#DAA520", "fg": "black", "padx": 10, "pady": 5}

add_btn = Button(button_frame, text="Add Task", command=add_task, **btn_style)
add_btn.grid(row=0, column=0, padx=5)

del_btn = Button(button_frame, text="Delete Task", command=delete_task, **btn_style)
del_btn.grid(row=0, column=1, padx=5)

mark_btn = Button(button_frame, text="✔️ Mark as Done", command=mark_as_done, **btn_style)
mark_btn.grid(row=0, column=2, padx=5)

del_all_btn = Button(button_frame, text="Delete All Tasks", command=delete_all_tasks, **btn_style)
del_all_btn.grid(row=1, column=1, pady=5)

listbox = Listbox(root, font=("Arial", 12), width=60, height=10, selectbackground="gray")
listbox.pack(pady=10)

exit_btn = Button(root, text="Exit", command=root.quit, font=("Arial", 12, "bold"), bg="#DAA520", fg="black", width=50)
exit_btn.pack(pady=5)

# Load and show tasks
load_tasks_from_file()
update_tasks()

root.mainloop()
