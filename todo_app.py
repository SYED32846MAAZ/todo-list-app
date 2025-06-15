import tkinter as tk
from tkinter import messagebox, ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x400")
        
        self.tasks = []
        
        # Create UI elements
        self.task_entry = ttk.Entry(root, font=('Arial', 12), width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        
        self.add_btn = ttk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=5, pady=10)
        
        self.task_listbox = tk.Listbox(root, height=15, width=50, font=('Arial', 12), selectbackground="#a6a6a6")
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        # Buttons frame
        btn_frame = ttk.Frame(root)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.complete_btn = ttk.Button(btn_frame, text="Mark Complete", command=self.mark_completed)
        self.complete_btn.grid(row=0, column=0, padx=5)
        
        self.edit_btn = ttk.Button(btn_frame, text="Edit Task", command=self.edit_task)
        self.edit_btn.grid(row=0, column=1, padx=5)
        
        self.delete_btn = ttk.Button(btn_frame, text="Delete Task", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)
        
        # Load tasks (if any)
        self.load_tasks()
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def mark_completed(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.tasks[selected]["completed"] = True
            self.update_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")
    
    def edit_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=self.tasks[selected]["task"])
            if new_task:
                self.tasks[selected]["task"] = new_task
                self.update_listbox()
                self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")
    
    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.tasks.pop(selected)
            self.update_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else " "
            self.task_listbox.insert(tk.END, f"[{status}] {task['task']}")
    
    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(f"{task['task']}|{task['completed']}\n")
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f.readlines():
                    task, completed = line.strip().split("|")
                    self.tasks.append({"task": task, "completed": completed == "True"})
            self.update_listbox()
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    from tkinter import simpledialog  # For the edit dialog
    app = TodoApp(root)
    root.mainloop()