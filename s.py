import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random
import subprocess
import os
import sys

# Global variable to store the last generated employee ID
last_generated_id = None

# Single admin credentials
ADMIN_CREDENTIALS = {
    'admin_id': 1000,
    'password': 'admin123'
}

# Set the path to your Python interpreter and project directory
PYTHON_EXECUTABLE = r"C:\Users\bhoja\PycharmProjects\EaseWork\.venv\Scripts\python.exe"
PROJECT_DIR = r"C:\Users\bhoja\PycharmProjects\EaseWork"

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1005",
        database="employeeinfo"
    )

def clear_fields():
    """Clear all widgets inside main_frame."""
    for widget in main_frame.winfo_children():
        widget.destroy()

def hide_buttons():
    """Hide the login and signup buttons."""
    signup_button.place_forget()
    login_button.place_forget()
    admin_link.place_forget()

def show_buttons():
    """Show the buttons again."""
    signup_button.place(relx=0.75, y=300, anchor=tk.CENTER)
    login_button.place(relx=0.75, y=400, anchor=tk.CENTER)
    admin_link.place(relx=0.75, y=500, anchor=tk.CENTER)

def show_admin_login():
    """Show admin login fields with fixed admin ID."""
    clear_fields()
    hide_buttons()

    ttk.Label(main_frame, text="Admin Login", font=("Helvetica", 24, "bold"), background="white").pack(pady=15)

    # Display fixed admin ID (not editable)
    id_frame = ttk.Frame(main_frame, style="White.TFrame")
    id_frame.pack(pady=8, fill='x')
    ttk.Label(id_frame, text="Admin ID:", font=("Helvetica", 16), width=14, anchor='e', background="white").pack(side='left', padx=8)
    admin_id_label = ttk.Label(id_frame, text=str(ADMIN_CREDENTIALS['admin_id']), font=("Helvetica", 16), width=22, background="white")
    admin_id_label.pack(side='left', fill='x', expand=True)

    # Password entry
    pass_frame = ttk.Frame(main_frame, style="White.TFrame")
    pass_frame.pack(pady=8, fill='x')
    ttk.Label(pass_frame, text="Password:", font=("Helvetica", 16), width=14, anchor='e', background="white").pack(side='left', padx=8)
    password_entry = ttk.Entry(pass_frame, font=("Helvetica", 16), show="*", width=22)
    password_entry.pack(side='left', fill='x', expand=True)
    password_entry.focus_set()

    submit_button = ttk.Button(main_frame, text="Login", style="Accent.TButton",
                             command=lambda: login_user(ADMIN_CREDENTIALS['admin_id'], password_entry.get(), True))
    submit_button.pack(pady=25)

    back_button = ttk.Button(main_frame, text="Back", style="Accent.TButton", command=show_main_screen)
    back_button.pack(pady=15)

def show_login_fields(emp_id=None, admin=False):
    """Display login form inside main_frame."""
    if admin:
        show_admin_login()
        return

    clear_fields()
    hide_buttons()

    ttk.Label(main_frame, text="Login", font=("Helvetica", 24, "bold"), background="white").pack(pady=15)

    # Employee ID field
    emp_frame = ttk.Frame(main_frame, style="White.TFrame")
    emp_frame.pack(pady=8, fill='x')
    emp_id_label = ttk.Label(emp_frame, text="Employee ID:", font=("Helvetica", 16), width=14, anchor='e', background="white")
    emp_id_label.pack(side='left', padx=8)
    emp_id_entry = ttk.Entry(emp_frame, font=("Helvetica", 16), width=22)
    emp_id_entry.pack(side='left', fill='x', expand=True)

    if emp_id:
        emp_id_entry.insert(0, str(emp_id))
        emp_id_entry.config(state='readonly')

    # Password field
    pass_frame = ttk.Frame(main_frame, style="White.TFrame")
    pass_frame.pack(pady=8, fill='x')
    password_label = ttk.Label(pass_frame, text="Password:", font=("Helvetica", 16), width=14, anchor='e', background="white")
    password_label.pack(side='left', padx=8)
    password_entry = ttk.Entry(pass_frame, font=("Helvetica", 16), show="*", width=22)
    password_entry.pack(side='left', fill='x', expand=True)

    if emp_id:
        password_entry.focus_set()

    submit_button = ttk.Button(main_frame, text="Login", style="Accent.TButton",
                             command=lambda: login_user(emp_id_entry.get(), password_entry.get(), False))
    submit_button.pack(pady=25)

    back_button = ttk.Button(main_frame, text="Back", style="Accent.TButton", command=show_main_screen)
    back_button.pack(pady=15)

def show_signup_fields():
    """Display signup form inside main_frame."""
    clear_fields()
    hide_buttons()

    ttk.Label(main_frame, text="Sign Up", font=("Helvetica", 24, "bold"), background="white").pack(pady=15)

    # Name field
    name_frame = ttk.Frame(main_frame, style="White.TFrame")
    name_frame.pack(pady=8, fill='x')
    name_label = ttk.Label(name_frame, text="Name:", font=("Helvetica", 16), width=14, anchor='e', background="white")
    name_label.pack(side='left', padx=8)
    name_entry = ttk.Entry(name_frame, font=("Helvetica", 16), width=22)
    name_entry.pack(side='left', fill='x', expand=True)

    # Email field
    email_frame = ttk.Frame(main_frame, style="White.TFrame")
    email_frame.pack(pady=8, fill='x')
    email_label = ttk.Label(email_frame, text="Email:", font=("Helvetica", 16), width=14, anchor='e', background="white")
    email_label.pack(side='left', padx=8)
    email_entry = ttk.Entry(email_frame, font=("Helvetica", 16), width=22)
    email_entry.pack(side='left', fill='x', expand=True)

    # Password field
    pass_frame = ttk.Frame(main_frame, style="White.TFrame")
    pass_frame.pack(pady=8, fill='x')
    password_label = ttk.Label(pass_frame, text="Password:", font=("Helvetica", 16), width=14, anchor='e', background="white")
    password_label.pack(side='left', padx=8)
    password_entry = ttk.Entry(pass_frame, font=("Helvetica", 16), show="*", width=22)
    password_entry.pack(side='left', fill='x', expand=True)

    submit_button = ttk.Button(main_frame, text="Sign Up", style="Accent.TButton",
                             command=lambda: signup_user(name_entry.get(), email_entry.get(), password_entry.get()))
    submit_button.pack(pady=25)

    back_button = ttk.Button(main_frame, text="Back", style="Accent.TButton", command=show_main_screen)
    back_button.pack(pady=15)

def show_main_screen():
    """Show the main screen with login and signup buttons."""
    clear_fields()
    show_buttons()

def login_user(emp_id, password, is_admin=False):
    """Authenticate user login."""
    password = password.strip()

    if not password:
        messagebox.showerror("Input Error", "Please enter the password!")
        return

    try:
        if is_admin:
            # Verify admin credentials with proper syntax
            if str(emp_id) == str(ADMIN_CREDENTIALS['admin_id']) and password == ADMIN_CREDENTIALS['password']:
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                root.destroy()
                script_path = os.path.join(PROJECT_DIR, "admin.py")
                subprocess.Popen([sys.executable, script_path, str(emp_id)])
            else:
                messagebox.showerror("Login Failed", "Invalid admin credentials!")
            return

        # Regular employee login
        emp_id = emp_id.strip()
        if not emp_id:
            messagebox.showerror("Input Error", "Please enter your Employee ID!")
            return

        conn = connect_to_db()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE employee_id = %s AND password = %s"
        cursor.execute(query, (emp_id, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Login Successful", f"Welcome, {user[2]}!")
            root.destroy()
            script_path = os.path.join(PROJECT_DIR, "d.py")
            print(f"Running script: {script_path}")  # Debugging the path
            subprocess.Popen([sys.executable, script_path, str(emp_id)])
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open application: {e}")

def signup_user(name, email, password):
    """Handle new user signup with validation."""
    global last_generated_id

    name = name.strip()
    email = email.strip()
    password = password.strip()

    if not name or not email or not password:
        messagebox.showerror("Input Error", "Please fill in all fields!")
        return

    if "@" not in email or "." not in email:
        messagebox.showerror("Input Error", "Please enter a valid email address!")
        return

    if len(password) < 8:
        messagebox.showerror("Input Error", "Password must be at least 8 characters long!")
        return

    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        while True:
            employee_id = random.randint(1000, 9999)
            cursor.execute("SELECT * FROM users WHERE employee_id = %s", (employee_id,))
            if not cursor.fetchone():
                break

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            messagebox.showerror("Sign Up Failed", "Email already exists!")
        else:
            insert_query = "INSERT INTO users (employee_id, name, email, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (employee_id, name, email, password))
            conn.commit()
            last_generated_id = employee_id
            messagebox.showinfo("Sign Up Successful",
                              f"Your Employee ID: {employee_id}\nPlease remember this for login!")
            show_login_fields(employee_id)

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Initialize main window
root = tk.Tk()
root.title("Dynamic Login and Signup Form")
root.state('zoomed')
root.attributes("-fullscreen", True)

# Configure styles
style = ttk.Style(root)
style.theme_use('clam')
style.configure("White.TFrame", background="white")
style.configure("TLabel", background="white")
style.configure("TEntry", fieldbackground="white")
style.configure("Accent.TButton", font=("Helvetica", 16), background="#ccf297", foreground="black")
style.map("Accent.TButton",
          background=[("active", "#b9d878")],
          foreground=[("active", "black")])
style.configure("Admin.TLabel", font=("Helvetica", 12), background="#f0f0f0", foreground="blue")
style.map("Admin.TLabel",
          foreground=[("active", "darkblue")],
          background=[("active", "#e0e0e0")])

# Load background image
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
image_path = r"C:\Users\bhoja\OneDrive\Pictures\project\s.png"
image = Image.open(image_path)
image = image.resize((screen_width, screen_height))
bg_image = ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Main Frame
main_frame = ttk.Frame(root, padding=25, style="White.TFrame")
main_frame.place(relx=0.75, rely=0.55, anchor=tk.CENTER)

# Buttons
signup_button = ttk.Button(root, text="SIGN UP", style="Accent.TButton", command=show_signup_fields)
signup_button.place(relx=0.75, y=300, anchor=tk.CENTER)

login_button = ttk.Button(root, text="LOG IN", style="Accent.TButton", command=show_login_fields)
login_button.place(relx=0.75, y=400, anchor=tk.CENTER)

admin_link = ttk.Label(root, text="Log in as Admin", style="Admin.TLabel", cursor="hand2")
admin_link.place(relx=0.75, y=500, anchor=tk.CENTER)
admin_link.bind("<Button-1>", lambda e: show_admin_login())

root.bind("<Escape>", lambda event: root.destroy())
root.mainloop()
