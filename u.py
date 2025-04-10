import customtkinter as ctk
import subprocess
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Path for storing the user profile image
PROFILE_IMAGE_PATH = "profile_image.png"

class UserProfileApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("User Profile")
        self.geometry("800x600")
        self.state('zoomed')

        # Set Dark Theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_profile_ui()

    def create_profile_ui(self):
        """Create the user profile UI."""
        self.clear_window()

        ctk.CTkLabel(self, text="User Profile", font=("Arial", 28, "bold")).pack(pady=20)

        form_frame = ctk.CTkFrame(self, corner_radius=15)
        form_frame.pack(pady=10, padx=20, fill="both", expand=True)

        label_font = ("Arial", 16)
        entry_font = ("Arial", 14)

        # Name
        ctk.CTkLabel(form_frame, text="Name:", font=label_font).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = ctk.CTkEntry(form_frame, font=entry_font)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Email
        ctk.CTkLabel(form_frame, text="Email:", font=label_font).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.email_entry = ctk.CTkEntry(form_frame, font=entry_font)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        # Contact
        ctk.CTkLabel(form_frame, text="Contact:", font=label_font).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.contact_entry = ctk.CTkEntry(form_frame, font=entry_font)
        self.contact_entry.grid(row=2, column=1, padx=10, pady=10)

        # Employee ID
        ctk.CTkLabel(form_frame, text="Employee ID:", font=label_font).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.emp_id_entry = ctk.CTkEntry(form_frame, font=entry_font)
        self.emp_id_entry.grid(row=3, column=1, padx=10, pady=10)

        # Emergency Contact
        ctk.CTkLabel(form_frame, text="Emergency Contact:", font=label_font).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.emergency_contact_entry = ctk.CTkEntry(form_frame, font=entry_font)
        self.emergency_contact_entry.grid(row=4, column=1, padx=10, pady=10)

        # Profile Picture
        self.profile_frame = ctk.CTkFrame(form_frame, corner_radius=10)
        self.profile_frame.grid(row=0, column=2, rowspan=5, padx=20, pady=10, sticky="nsew")

        self.profile_image_label = ctk.CTkLabel(self.profile_frame, text="No Image", width=180, height=180, fg_color="gray")
        self.profile_image_label.pack(pady=10)

        ctk.CTkButton(self.profile_frame, text="Upload Image", command=self.upload_image).pack(pady=5)
        ctk.CTkButton(self.profile_frame, text="Delete Image", command=self.delete_image).pack(pady=5)

        # Load existing profile image
        self.load_profile_image()

        # Buttons
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=20)

        ctk.CTkButton(btn_frame, text="Save", command=self.save_profile, fg_color="green").pack(side="left", padx=20)
        ctk.CTkButton(btn_frame, text="Edit", command=self.edit_profile, fg_color="blue").pack(side="left", padx=20)

        # Back Button
        ctk.CTkButton(self, text="⬅ Back to Dashboard", command=self.go_to_dashboard, fg_color="gray").pack(pady=10, anchor="w")

    def clear_window(self):
        """Clear all widgets from the window."""
        for widget in self.winfo_children():
            widget.destroy()

    def go_to_dashboard(self):
        """Close this window and open d.py."""
        self.destroy()
        subprocess.Popen(["python", "d.py"])  # Opens the dashboard script

    def upload_image(self):
        """Upload a profile image."""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((180, 180), Image.Resampling.LANCZOS)
            image.save(PROFILE_IMAGE_PATH)  # Save image locally
            self.load_profile_image()

    def delete_image(self):
        """Delete the profile image."""
        if os.path.exists(PROFILE_IMAGE_PATH):
            os.remove(PROFILE_IMAGE_PATH)
            self.profile_image_label.configure(image=None, text="No Image")
            self.profile_image_label.image = None

    def load_profile_image(self):
        """Load and display the profile image if available."""
        if os.path.exists(PROFILE_IMAGE_PATH):
            image = Image.open(PROFILE_IMAGE_PATH)
            image = image.resize((180, 180), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            self.profile_image_label.configure(image=photo, text="")
            self.profile_image_label.image = photo  # Keep a reference

    def save_profile(self):
        """Save user profile data."""
        user_data = {
            "name": self.name_entry.get(),
            "email": self.email_entry.get(),
            "contact": self.contact_entry.get(),
            "employee_id": self.emp_id_entry.get(),
            "emergency_contact": self.emergency_contact_entry.get(),
        }

        if any(value.strip() == "" for value in user_data.values()):
            messagebox.showwarning("Warning", "All fields must be filled!")
        else:
            # Save the name in a text file
            with open("profile_data.txt", "w") as f:
                f.write(user_data["name"])  # Save only the name

            messagebox.showinfo("Save", "Profile saved successfully!")

    def edit_profile(self):
        """Enable editing of profile fields."""
        messagebox.showinfo("Edit", "Edit mode enabled. Now you can update your details.")
        self.name_entry.configure(state="normal")
        self.email_entry.configure(state="normal")
        self.contact_entry.configure(state="normal")
        self.emp_id_entry.configure(state="normal")
        self.emergency_contact_entry.configure(state="normal")


if __name__ == "__main__":
    app = UserProfileApp()
    app.mainloop()
