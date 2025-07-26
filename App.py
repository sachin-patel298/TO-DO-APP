from tkinter import *
from tkinter import messagebox

# --- Setup main window ---
root = Tk()
root.title("To-Do List")
root.geometry("500x400")
root.config(bg="black")

tasks = []
footer_visible = True  # To track whether footer is showing

# --- Functions ---
def update_tasks():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

    # Only show footer if no tasks are present
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
        update_tasks()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def delete_all_tasks():
    if messagebox.askyesno("Confirm Delete", "Delete all tasks?"):
        tasks.clear()
        update_tasks()

# --- UI Layout ---
# Entry Label
task_label = Label(root, text="Enter the Task:", font=("Arial", 12), fg="white", bg="black")
task_label.pack(pady=5)

# Task Entry
task_entry = Entry(root, font=("Arial", 12), width=40)
task_entry.pack(pady=5)

# Buttons Frame
button_frame = Frame(root, bg="black")
button_frame.pack(pady=10)

btn_style = {"font": ("Arial", 12, "bold"), "bg": "#DAA520", "fg": "black", "padx": 10, "pady": 5}

add_btn = Button(button_frame, text="Add Task", command=add_task, **btn_style)
add_btn.grid(row=0, column=0, padx=5)

del_btn = Button(button_frame, text="Delete Task", command=delete_task, **btn_style)
del_btn.grid(row=0, column=1, padx=5)

del_all_btn = Button(button_frame, text="Delete All Tasks", command=delete_all_tasks, **btn_style)
del_all_btn.grid(row=0, column=2, padx=5)

# Listbox
listbox = Listbox(root, font=("Arial", 12), width=60, height=10, selectbackground="gray")
listbox.pack(pady=10)

# Exit Button
exit_btn = Button(root, text="Exit", command=root.quit, font=("Arial", 12, "bold"), bg="#DAA520", fg="black", width=50)
exit_btn.pack(pady=5)

# Show welcome footer at start
update_tasks()

root.mainloop()
