import customtkinter as ctk
import random
import json
import os

# JSON file to store task progress
TASK_FILE = "tasks.json"

# Random Task List
sample_tasks = [
    "Prepare Sales Report", "Update Client Database", "Develop Marketing Strategy",
    "Fix UI Bugs in Application", "Conduct Team Meeting", "Write Weekly Blog Post",
    "Optimize Database Queries", "Create Financial Forecast", "Research Market Trends",
    "Test New Software Release"
]

# Load task data from JSON
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return {}

# Save task data to JSON
def save_tasks(data):
    with open(TASK_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Generate 10 random tasks for an employee
def generate_random_tasks(employee_id):
    tasks = random.sample(sample_tasks, 10)
    task_data = {task: "Pending" for task in tasks}

    all_tasks = load_tasks()
    all_tasks[employee_id] = task_data
    save_tasks(all_tasks)

    return task_data

# Show Employee's Tasks
def show_tasks():
    global tasks_frame
    employee_id = entry_employee_id.get().strip()

    if not employee_id.isdigit():
        error_label.configure(text="Invalid Employee ID", text_color="red")
        return

    error_label.configure(text="")
    employee_id = str(employee_id)

    all_tasks = load_tasks()
    tasks = all_tasks.get(employee_id, generate_random_tasks(employee_id))

    # Clear previous tasks
    for widget in tasks_frame.winfo_children():
        widget.destroy()

    for task, status in tasks.items():
        row_frame = ctk.CTkFrame(tasks_frame)
        row_frame.pack(fill="x", padx=10, pady=5)

        task_label = ctk.CTkLabel(row_frame, text=task, font=("Arial", 14))
        task_label.pack(side="left", padx=10)

        status_label = ctk.CTkLabel(row_frame, text=f"Status: {status}", font=("Arial", 14))
        status_label.pack(side="left", padx=10)

        def update_status(new_status, task_name):
            tasks[task_name] = new_status
            all_tasks[employee_id] = tasks
            save_tasks(all_tasks)
            status_label.configure(text=f"Status: {new_status}")

        completed_button = ctk.CTkButton(row_frame, text="✅ Completed", width=100,
                                         command=lambda t=task: update_status("Completed", t))
        completed_button.pack(side="right", padx=5)

        pending_button = ctk.CTkButton(row_frame, text="⏳ Pending", width=100, fg_color="orange",
                                       command=lambda t=task: update_status("Pending", t))
        pending_button.pack(side="right", padx=5)

# Main Window
root = ctk.CTk()
root.title("Employee Task Manager")
root.geometry("800x600")

# Employee ID Entry
entry_label = ctk.CTkLabel(root, text="Enter Employee ID:", font=("Arial", 18))
entry_label.pack(pady=10)

entry_employee_id = ctk.CTkEntry(root, width=200)
entry_employee_id.pack(pady=5)

submit_button = ctk.CTkButton(root, text="Show Tasks", command=show_tasks)
submit_button.pack(pady=10)

error_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
error_label.pack()

# Task List Frame
tasks_frame = ctk.CTkScrollableFrame(root, width=700, height=400)
tasks_frame.pack(pady=20)

# Run App
root.mainloop()
