import tkinter as tk
from tkinter import messagebox
import json

tasks = {}

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = entry.get()
    if task:
        tasks[task] = {"status": "pending"}
        save_tasks()
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Enter a task name!")

def delete_task():
    task = listbox.get(tk.ACTIVE)
    if task in tasks:
        del tasks[task]
        save_tasks()
        listbox.delete(tk.ACTIVE)
    else:
        messagebox.showwarning("Input Error", "Select a task!")

def mark_completed():
    task = listbox.get(tk.ACTIVE)
    if task in tasks:
        tasks[task]["status"] = "completed"
        save_tasks()
        messagebox.showinfo("Success", f"Marked '{task}' as completed!")
    else:
        messagebox.showwarning("Error", "Task not found!")

def refresh_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Load existing tasks
tasks = load_tasks()

# Initialize the main window
window = tk.Tk()
window.title("To-Do List")

# Create input field for new tasks
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Add task button
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(window, width=50, height=10)
listbox.pack(pady=10)
refresh_task_list()

# Buttons for task actions
delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

complete_button = tk.Button(window, text="Mark Completed", command=mark_completed)
complete_button.pack(side=tk.LEFT, padx=10)

# Start the application
window.mainloop()
