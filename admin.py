import customtkinter as ctk
import subprocess
import sys
import os

# Create the main application window
root = ctk.CTk()
root.title("Admin Dashboard")
root.geometry("1000x600")

# Function to open a Python file
def open_script(script_name):
    script_path = os.path.join(os.getcwd(), script_name)  # Ensure correct file path
    if os.path.exists(script_path):
        subprocess.Popen([sys.executable, script_path])  # Open the script using the correct Python interpreter
    else:
        print(f"Error: {script_name} not found. Make sure it is in the same directory.")

# Create a frame for the buttons at the top
button_frame = ctk.CTkFrame(root)
button_frame.pack(fill="x", pady=40)

# Create buttons for each section
leave_button = ctk.CTkButton(button_frame, text="Leave Applications", font=("Helvetica", 22), width=200,
                             command=lambda: open_script("ls.py"))
leave_button.grid(row=0, column=0, padx=20, pady=10)

attendance_button = ctk.CTkButton(button_frame, text="Attendance Log", font=("Helvetica", 22), width=200,
                                  command=lambda: open_script("atten.py"))
attendance_button.grid(row=0, column=1, padx=20, pady=10)

task_button = ctk.CTkButton(button_frame, text="Task Remaining", font=("Helvetica", 22), width=200,
                            command=lambda: open_script("TD.py"))
task_button.grid(row=0, column=2, padx=20, pady=10)

# Run the application
root.mainloop()
