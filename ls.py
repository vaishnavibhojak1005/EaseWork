import customtkinter as ctk
import mysql.connector
from tkinter import messagebox

# Function to connect to the database
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1005",
            database="employeeinfo"
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Function to retrieve pending leave requests
def get_leave_requests():
    conn = connect_to_db()
    if not conn:
        return []

    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, leave_type, start_date, end_date, days_requested FROM leave_requests WHERE status = 'Pending'")
    requests = cursor.fetchall()
    conn.close()
    return requests

# Function to update leave request status
def update_leave_status(leave_id, status):
    conn = connect_to_db()
    if not conn:
        return

    cursor = conn.cursor()
    cursor.execute("UPDATE leave_requests SET status = %s WHERE id = %s", (status, leave_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", f"Leave request {status}!")
    show_leave_application()  # Refresh UI

# Function to display leave requests
def show_leave_application():
    global leave_frame
    if leave_frame:
        leave_frame.destroy()

    leave_frame = ctk.CTkScrollableFrame(root, width=900, height=400)
    leave_frame.pack(pady=20)

    leave_requests = get_leave_requests()
    if not leave_requests:
        ctk.CTkLabel(leave_frame, text="No pending leave requests.", font=("Helvetica", 16)).pack(pady=20)
        return

    for row_idx, request in enumerate(leave_requests, start=1):
        leave_id, name, email, leave_type, start_date, end_date, days_requested = request

        row_data = [name, email, leave_type, start_date, end_date, days_requested]
        for col_idx, data in enumerate(row_data):
            ctk.CTkLabel(leave_frame, text=data, font=("Helvetica", 14), padx=10, pady=5).grid(row=row_idx, column=col_idx)

        ctk.CTkButton(leave_frame, text="✅ Approve", command=lambda leave_id=leave_id: update_leave_status(leave_id, "Approved")).grid(row=row_idx, column=6)
        ctk.CTkButton(leave_frame, text="❌ Reject", fg_color="red", command=lambda leave_id=leave_id: update_leave_status(leave_id, "Rejected")).grid(row=row_idx, column=7)

# Main UI
root = ctk.CTk()
root.title("Leave Approval System")
leave_frame = None
show_leave_application()
root.mainloop()
