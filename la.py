import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess

def show_dashboard():
    """Displays the dashboard with 3 buttons (Exit, Leave Application, Attendance Log, HR Documents)."""
    root = tk.Tk()
    root.title("Dashboard")
    root.state("zoomed")
    root.configure(bg="white")

    # Load background image
    image_path = r"C:\Users\bhoja\OneDrive\Pictures\l.png"

    # Handle missing background image gracefully
    if not os.path.isfile(image_path):
        print(f"Error: Background image not found at {image_path}")
        messagebox.showerror("Error", "Background image not found!")
        root.destroy()
        return

    image = Image.open(image_path)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    # Background image canvas
    canvas = tk.Canvas(root, width=screen_width, height=screen_height, highlightthickness=0)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    # Buttons with white background and white text (except Exit button)
    exit_button = tk.Button(root, text="Exit", font=("Helvetica", 16), command=root.quit,
                          bg="#2c3e50", fg="white", relief="flat")  # Only Exit button changed
    exit_button.place(relx=0.05, rely=0.95, anchor="center")

    leave_app_button = tk.Button(root, text="L", font=("Helvetica", 16),
                              command=leave_application, bg="white", fg="white", relief="flat")
    leave_app_button.place(relx=0.23, rely=0.5, anchor="center")

    attendance_log_button = tk.Button(root, text="a", font=("Helvetica", 16),
                                   command=attendance_log, bg="white", fg="white", relief="flat")
    attendance_log_button.place(relx=0.55, rely=0.5, anchor="center")

    hr_docs_button = tk.Button(root, text="h", font=("Helvetica", 16),
                             command=hr_documents, bg="white", fg="white", relief="flat")
    hr_docs_button.place(relx=0.85, rely=0.5, anchor="center")

    root.mainloop()

def leave_application():
    """Handle leave application button click and open l2.py."""
    open_script("l2.py", "Leave Application")

def attendance_log():
    """Handle attendance log button click and open att.py."""
    open_script("att.py", "Attendance Log")

def hr_documents():
    """Handle HR documents button click and open HR.py."""
    open_script("HR.py", "HR Documents")

def open_script(script_name, action_name):
    """Open a script using subprocess and handle errors."""
    try:
        subprocess.Popen(["python", script_name], shell=True)
    except Exception as e:
        messagebox.showerror("Error", f"Error opening {action_name}: {e}")

if __name__ == "__main__":
    show_dashboard()