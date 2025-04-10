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


def on_enter(button):
    """Change the button text color to grey when mouse hovers over it."""
    button.config(fg="grey")


def on_leave(button):
    """Revert the button text color back to white when mouse leaves."""
    button.config(fg="white")


def show_dashboard():
    """Displays the dashboard with navigation buttons."""
    root = tk.Tk()
    root.title("Dashboard")
    root.state("zoomed")
    root.configure(bg="black")

    # Load background image
    image_path = r"C:\Users\bhoja\OneDrive\Pictures\h.png"

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
        {"text": "hc", "page": "hc", "x": screen_width * 0.23, "y": screen_height * 0.5},  # hc button
        {"text": "p", "page": "p", "x": screen_width * 0.55, "y": screen_height * 0.5},  # p button
        {"text": "vc", "page": "vc", "x": screen_width * 0.85, "y": screen_height * 0.5}  # vc button
    ]

    # Create buttons with white background and white text
    for btn in button_data:
        button = tk.Button(
            root,
            text=btn["text"],
            font=("Helvetica", 12, "bold"),
            width=8,  # Adjusted width for visibility
            height=2,
            bg="white",  # Set a white background for buttons
            fg="white",  # Set button text color to white initially
            activebackground="white",  # Keep white when active
            activeforeground="white",  # Keep text white when active
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda p=btn["page"]: open_page(p)
        )

        # Bind hover events to change text color
        button.bind("<Enter>", lambda e, b=button: on_enter(b))
        button.bind("<Leave>", lambda e, b=button: on_leave(b))

        button.place(x=btn["x"], y=btn["y"])

    # Create the 'Exit' button with #2c3e50 background and font color
    exit_button = tk.Button(
        root,
        text="Exit",
        font=("Helvetica", 12, "bold"),
        width=8,
        height=2,
        bg="#2c3e50",  # Set background to #2c3e50
        fg="white",  # Set text color to white
        activebackground="#2c3e50",  # Keep #2c3e50 background when active
        activeforeground="white",  # Keep white text when active
        relief="flat",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: root.destroy()  # Close the current window
    )
    exit_button.place(x=20, y=screen_height - 100)  # Bottom left corner

    root.mainloop()


if __name__ == "__main__":
    show_dashboard()
