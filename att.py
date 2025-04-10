import customtkinter as ctk
import datetime
import os
from PIL import Image, ImageTk

# Path for storing the user profile image
PROFILE_IMAGE_PATH = "profile_image.png"


class AttendanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Attendance System")
        self.geometry("1000x700")
        self.state('zoomed')

        # Set Dark Theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_ui()

    def create_ui(self):
        """Create the user profile and attendance UI."""
        self.clear_window()

        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Profile Frame (Left Side)
        profile_frame = ctk.CTkFrame(main_frame, width=250, corner_radius=10)
        profile_frame.pack(side="left", padx=20, pady=20, fill="y")

        # Profile Image
        self.profile_image_label = ctk.CTkLabel(profile_frame, text="No Image", width=200, height=200, fg_color="gray")
        self.profile_image_label.pack(pady=10)

        # Profile Name
        self.profile_name_label = ctk.CTkLabel(profile_frame, text="Unknown User", font=("Arial", 20, "bold"))
        self.profile_name_label.pack(pady=10)

        # Load existing profile image and name
        self.load_profile_data()

        # Attendance Frame (Right Side)
        attendance_frame = ctk.CTkFrame(main_frame, corner_radius=10)
        attendance_frame.pack(side="right", padx=20, pady=20, fill="both", expand=True)

        # Attendance Table
        self.attendance_text = ctk.CTkTextbox(attendance_frame, width=600, height=300, font=("Arial", 14))
        self.attendance_text.pack(pady=10, padx=10)
        self.attendance_text.insert("end", "Date\t\tCheck-in\t\tCheck-out\n")
        self.attendance_text.configure(state="disabled")

        # Buttons
        button_frame = ctk.CTkFrame(attendance_frame)
        button_frame.pack(pady=10)

        self.checkin_button = ctk.CTkButton(button_frame, text="Mark Check-in", command=self.mark_checkin,
                                            fg_color="green", width=150, height=50)
        self.checkin_button.pack(side="left", padx=20)

        self.checkout_button = ctk.CTkButton(button_frame, text="Mark Check-out", command=self.mark_checkout,
                                             fg_color="red", width=150, height=50)
        self.checkout_button.pack(side="left", padx=20)

    def clear_window(self):
        """Clear all widgets from the window."""
        for widget in self.winfo_children():
            widget.destroy()

    def load_profile_data(self):
        """Load and display the profile image and name."""
        if os.path.exists(PROFILE_IMAGE_PATH):
            image = Image.open(PROFILE_IMAGE_PATH)
            image = image.resize((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.profile_image_label.configure(image=photo, text="")
            self.profile_image_label.image = photo  # Keep a reference

        self.profile_name_label.configure(text="John Doe")  # Replace with actual user data retrieval

    def mark_checkin(self):
        """Mark check-in time."""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.attendance_text.configure(state="normal")
        self.attendance_text.insert("end", f"{current_time}\t\tChecked In\n")
        self.attendance_text.configure(state="disabled")

    def mark_checkout(self):
        """Mark check-out time."""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.attendance_text.configure(state="normal")
        self.attendance_text.insert("end", f"{current_time}\t\tChecked Out\n")
        self.attendance_text.configure(state="disabled")


if __name__ == "__main__":
    app = AttendanceApp()
    app.mainloop()