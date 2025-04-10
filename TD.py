import customtkinter as ctk
import matplotlib.pyplot as plt
import json
from datetime import datetime, timedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# JSON file to track task progress
TASK_FILE = "tasks.json"


# Load tasks from JSON
def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# Function to display Gantt Chart
def show_gantt_chart():
    global gantt_frame

    # Clear previous chart
    for widget in gantt_frame.winfo_children():
        widget.destroy()

    all_tasks = load_tasks()
    employee_id = entry_employee_id.get().strip()

    if employee_id not in all_tasks:
        error_label.configure(text="No tasks found for this ID.", text_color="red")
        return

    error_label.configure(text="")
    tasks = all_tasks[employee_id]

    fig, ax = plt.subplots(figsize=(8, 5))

    start_date = datetime.today()
    colors = {"Pending": "orange", "Completed": "green"}

    for i, (task, status) in enumerate(tasks.items()):
        task_start = start_date + timedelta(days=i)
        task_end = task_start + timedelta(days=2)  # Assume each task takes 2 days

        ax.barh(task, (task_end - task_start).days, left=task_start, color=colors[status])

    ax.set_xlabel("Date")
    ax.set_title(f"Gantt Chart for Employee {employee_id}")
    plt.xticks(rotation=45)

    # Embed Matplotlib figure into Tkinter
    canvas = FigureCanvasTkAgg(fig, master=gantt_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Main Window
root = ctk.CTk()
root.title("Gantt Chart Viewer")
root.geometry("900x600")

# Employee ID Entry
entry_label = ctk.CTkLabel(root, text="Enter Employee ID:", font=("Arial", 18))
entry_label.pack(pady=10)

entry_employee_id = ctk.CTkEntry(root, width=200)
entry_employee_id.pack(pady=5)

submit_button = ctk.CTkButton(root, text="Show Gantt Chart", command=show_gantt_chart)
submit_button.pack(pady=10)

error_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
error_label.pack()

# Gantt Chart Frame
gantt_frame = ctk.CTkFrame(root, width=800, height=400)
gantt_frame.pack(pady=20)

# Run App
if __name__ == "__main__":
    root.mainloop()

