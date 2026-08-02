import tkinter as tk

# Store tasks
tasks = []

# Add task function
def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Delete task function
def delete_task():
    selected_task = task_list.curselection()

    if selected_task:
        task_index = selected_task[0]
        task_list.delete(task_index)
        tasks.pop(task_index)

# Update task function
def update_task():
    selected_task = task_list.curselection()

    if selected_task:
        task_index = selected_task[0]
        new_task = task_entry.get()

        if new_task != "":
            tasks[task_index] = new_task
            task_list.delete(task_index)
            task_list.insert(task_index, new_task)
            task_entry.delete(0, tk.END)


# Create window
window = tk.Tk()

window.title("To-Do List")
window.geometry("400x400")


# Task input box
task_entry = tk.Entry(window, width=30)
task_entry.pack(pady=10)


# Buttons
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

update_button = tk.Button(window, text="Update Task", command=update_task)
update_button.pack()

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()


# Display tasks
task_list = tk.Listbox(window, width=40, height=10)
task_list.pack(pady=10)


# Keep window running
window.mainloop()