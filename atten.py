import customtkinter as ctk
import mysql.connector
from datetime import datetime


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


# Function to retrieve attendance data from the database
def get_attendance_data():
    conn = connect_to_db()
    if not conn:
        return []

    cursor = conn.cursor()

    # Fetch attendance records with check-in and check-out times
    query = """
    SELECT u.name, u.email, u.employee_id, a.check_in_time, a.check_out_time
    FROM users u
    LEFT JOIN attendance a ON u.employee_id = a.employee_id
    """
    cursor.execute(query)
    attendance_records = cursor.fetchall()

    conn.close()
    return attendance_records


# Function to display the attendance table
def show_attendance(root):
    global attendance_frame

    # Remove previous frame if it exists
    if "attendance_frame" in globals() and attendance_frame:
        attendance_frame.destroy()

    # Create a scrollable frame for attendance records
    attendance_frame = ctk.CTkScrollableFrame(root, width=1100, height=500, fg_color="#2A2A2A", corner_radius=10)
    attendance_frame.pack(pady=20, padx=20, fill="both", expand=True)

    attendance_data = get_attendance_data()  # Fetch attendance records

    # Table headers
    headers = ["Name", "Email", "Employee ID", "Check-in Time", "Check-out Time"]
    for col, header in enumerate(headers):
        header_label = ctk.CTkLabel(attendance_frame, text=header, font=("Helvetica", 18, "bold"), text_color="white",
                                    padx=20, pady=10, fg_color="#444")
        header_label.grid(row=0, column=col, sticky="w", padx=10, pady=10)

    # Table divider
    divider = ctk.CTkLabel(attendance_frame, text="-" * 120, font=("Helvetica", 16), text_color="white")
    divider.grid(row=1, column=0, columnspan=len(headers), pady=10)

    # Insert attendance data into table rows
    for row_idx, record in enumerate(attendance_data, start=2):
        name, email, emp_id, check_in, check_out = record
        row_data = [name, email, emp_id, check_in or "Not Checked-in", check_out or "Not Checked-out"]

        for col_idx, data in enumerate(row_data):
            cell_label = ctk.CTkLabel(attendance_frame, text=data, font=("Helvetica", 16), text_color="white", padx=20,
                                      pady=10)
            cell_label.grid(row=row_idx, column=col_idx, sticky="w", padx=10, pady=10)


# Create the main application window
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Dark mode
    ctk.set_default_color_theme("blue")  # Theme

    root = ctk.CTk()
    root.title("Attendance Record Page")
    root.geometry("1200x700")  # Bigger window size for better view
    root.state("zoomed")  # Open in full-screen

    attendance_frame = None  # Placeholder for the UI frame

    show_attendance(root)  # Call function to display attendance

    root.mainloop()
