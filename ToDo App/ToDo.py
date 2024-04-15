import tkinter as tk
from tkinter import messagebox


class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do App by Rajat Gupta")

        self.tasks = []

        self.task_entry = tk.Entry(self.master, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task, bg="green")
        self.add_button.pack()

        self.task_listbox = tk.Listbox(self.master, width=40)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task, bg="red")
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")


def main():
    root = tk.Tk()
    todo_app = TodoListApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
