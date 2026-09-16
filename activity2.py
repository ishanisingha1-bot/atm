import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Task Checker")
root.geometry("280x200")
tasks = ["1. Wash hands", "2. Complete homework", "3. Pack school bag"]
def complete_task(button, task_name):
    messagebox.showinfo("Task Update", f"Done: {task_name}")
    tasks.remove(task_name)
    if not tasks:
        messagebox.showinfo("Congratulations", " you completed all your tasks")
tk.Label(root, text="Click a task to mark it done:", font=("Arial", 10, "bold")).pack(pady=8)
for task in list(tasks):
    btn = tk.Button(root, text=task, width=22)
    btn.config(command=lambda b=btn, t=task: complete_task(b, t))
    btn.pack(pady=4)

root.mainloop()
