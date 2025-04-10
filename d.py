import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os

# Set the path to your Python interpreter
PYTHON_EXECUTABLE = r"C:\Users\bhoja\PycharmProjects\EaseWork\.venv\Scripts\python.exe"
PROJECT_DIR = r"C:\Users\bhoja\PycharmProjects\EaseWork"

def open_page(page_name):
    """Opens a new page using subprocess with the correct Python interpreter."""
    script_path = os.path.join(PROJECT_DIR, f"{page_name}.py")

    if not os.path.isfile(script_path):
        print(f"Error: {script_path} not found!")
        tk.messagebox.showerror("File Not Found", f"{page_name}.py does not exist.")
        return

    try:
        print(f"Opening page: {script_path}")
        subprocess.Popen([PYTHON_EXECUTABLE, script_path])
    except Exception as e:
        print(f"Error while opening {script_path}: {e}")
        tk.messagebox.showerror("Error", f"Failed to open {page_name}.py: {e}")

def show_dashboard():
    """Displays the dashboard with navigation buttons."""
    root = tk.Tk()
    root.title("Dashboard")
    root.state("zoomed")
    root.configure(bg="black")

    # Load background image
    image_path = r"C:\Users\bhoja\OneDrive\Pictures\d.png"

    # Handle missing background image gracefully
    if not os.path.isfile(image_path):
        print(f"Error: Background image not found at {image_path}")
        tk.messagebox.showerror("Error", "Background image not found!")
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

    # Button properties
    button_data = [
        {"text": "u", "page": "u", "x": 45, "y": 225},  # User Profile
        {"text": "l", "page": "la", "x": 38, "y": 355},  # Leave Application
        {"text": "h", "page": "h", "x": 47, "y": 500}   # HR Documents (changed to h.py)
    ]

    # Create buttons
    for btn in button_data:
        button = tk.Button(
            root,
            text=btn["text"],
            font=("Helvetica", 12, "bold"),
            width=2,
            height=1,
            bg="#2c3e50",
            fg="#2c3e50",
            activebackground="#2c3e50",
            activeforeground="#2c3e50",
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda p=btn["page"]: open_page(p)
        )
        button.place(x=btn["x"], y=btn["y"])

    # Create 'User Profile' button (small, hidden style)
    user_profile_button = tk.Button(
        root,
        text="User Profile",
        font=("Helvetica", 1, "bold"),  # Very small font
        width=1,
        height=1,
        bg="white",
        fg="white",
        activebackground="white",
        activeforeground="white",
        relief="flat",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_page("u")
    )
    user_profile_button.place(x=150, y=225)  # Adjust position as needed

    # Create the 'Exit' button to redirect to d.py
    exit_button = tk.Button(
        root,
        text="Exit",
        font=("Helvetica", 12, "bold"),
        width=4,
        height=1,
        bg="#2c3e50",
        fg="#2c3e50",
        activebackground="white",
        activeforeground="white",
        relief="flat",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_page("d")  # Redirect to d.py
    )
    exit_button.place(x=50, y=screen_height - 100)  # Bottom left corner

    root.mainloop() # Keeps the window open until you press Enter


if __name__ == "__main__":
    show_dashboard()
