import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import mysql.connector

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

# Class for Leave Application
class LeaveRequestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Leave Request System")
        self.root.geometry("1200x800")
        self.root.state('zoomed')

        # Leave Balances
        self.leave_balance = {
            "Privilege Leave (PL)": 15,
            "Earned Leave (EL)": 15,
            "Casual Leave (CL)": 10,
            "Sick Leave (SL)": 10
        }

        self.main_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def submit_leave_request(self):
        try:
            name = self.entries["Name:"].get().strip()
            email = self.entries["Email:"].get().strip()
            leave_type = self.entries["Leave Type:"].get()
            start_date = self.entries["Leave Start Date (YYYY-MM-DD):"].get().strip()
            end_date = self.entries["Leave End Date (YYYY-MM-DD):"].get().strip()

            if not (name and email and leave_type and start_date and end_date):
                messagebox.showerror("Error", "All fields are required!")
                return

            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

            if end_date < start_date:
                messagebox.showerror("Error", "End date cannot be earlier than start date!")
                return

            leave_days = (end_date - start_date).days + 1

            if leave_days > self.leave_balance[leave_type]:
                messagebox.showerror("Error", f"Not enough balance for {leave_type}.")
                return

            # Store in database
            conn = connect_to_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO leave_requests (name, email, leave_type, start_date, end_date, days_requested, status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (name, email, leave_type, start_date.date(), end_date.date(), leave_days, "Pending"))
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Leave request submitted successfully!")
                self.main_screen()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format! Please use YYYY-MM-DD.")

    def main_screen(self):
        self.clear_window()

        self.center_frame = ctk.CTkFrame(self.root)
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(self.center_frame, text="Leave Request System", font=("Arial", 40, "bold")).pack(pady=40)
        ctk.CTkButton(self.center_frame, text="📩 APPLY FOR LEAVE", font=("Arial", 30), width=300, height=50,
                      command=self.leave_request_form).pack(pady=20)

    def leave_request_form(self):
        self.clear_window()

        self.center_frame = ctk.CTkFrame(self.root)
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(self.center_frame, text="Leave Request Form", font=("Arial", 28, "bold")).pack(pady=20)

        form_frame = ctk.CTkFrame(self.center_frame)
        form_frame.pack(pady=20)

        fields = ["Name:", "Email:", "Leave Type:", "Leave Start Date (YYYY-MM-DD):", "Leave End Date (YYYY-MM-DD):"]
        self.entries = {}

        for field in fields:
            ctk.CTkLabel(form_frame, text=field, font=("Arial", 18)).pack(anchor="w", pady=5)
            if field == "Leave Type:":
                self.entries[field] = ctk.CTkComboBox(form_frame, values=list(self.leave_balance.keys()),
                                                      font=("Arial", 16), width=400)
            else:
                self.entries[field] = ctk.CTkEntry(form_frame, font=("Arial", 16), width=400)
            self.entries[field].pack(pady=5)

        ctk.CTkButton(self.center_frame, text="📩 SUBMIT REQUEST", font=("Arial", 20, "bold"), width=300, height=50,
                      command=self.submit_leave_request).pack(pady=20)

        ctk.CTkButton(self.center_frame, text="⬅ Back to Dashboard", font=("Arial", 18), fg_color="gray30",
                      command=self.main_screen).pack(pady=20)


# Run the application
if __name__ == "__main__":
    root = ctk.CTk()
    app = LeaveRequestApp(root)
    root.mainloop()
