import customtkinter as ctk
from tkinter import filedialog, messagebox
import shutil
import os

# Initialize CustomTkinter
ctk.set_appearance_mode("dark")  # Dark mode
ctk.set_default_color_theme("blue")  # Blue theme

class DocumentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Upload & Download App")
        self.root.geometry("900x700")

        self.uploaded_files = []  # List to store uploaded file paths

        # Back Button (Top-Left)
        self.back_button = ctk.CTkButton(root, text="⬅ Back to Dashboard", fg_color="red", command=self.back_to_dashboard)
        self.back_button.pack(pady=10, padx=10, anchor="w")

        # Title Label
        self.label = ctk.CTkLabel(root, text="Upload Your Documents", font=("Arial", 32, "bold"))
        self.label.pack(pady=20)

        # Upload Button
        self.upload_button = ctk.CTkButton(root, text="Upload Document", font=("Arial", 24), width=300, command=self.upload_document)
        self.upload_button.pack(pady=20)

        # File List Frame
        self.frame = ctk.CTkFrame(root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Listbox for uploaded files
        self.file_listbox = ctk.CTkTextbox(self.frame, height=250, font=("Arial", 18))
        self.file_listbox.pack(pady=10, padx=10, fill="both", expand=True)

        # Download Button
        self.download_button = ctk.CTkButton(root, text="Download PDF", font=("Arial", 24), width=300, command=self.download_pdf)
        self.download_button.pack(pady=20)

    def upload_document(self):
        filetypes = (
            ('Text files', '*.txt'),
            ('PDF files', '*.pdf'),
            ('Word files', '*.docx'),
            ('All files', '*.*')
        )
        file_path = filedialog.askopenfilename(title="Select a document", filetypes=filetypes)

        if file_path:
            filename = os.path.basename(file_path)
            self.uploaded_files.append(file_path)

            # Update the listbox with the new file
            self.file_listbox.insert("end", f"{filename}\n")
        else:
            messagebox.showwarning("No file", "No document selected.")

    def download_pdf(self):
        selected_text = self.file_listbox.get("1.0", "end").strip()
        if not selected_text:
            messagebox.showwarning("No Selection", "Please upload and select a file to download.")
            return

        for file in self.uploaded_files:
            if selected_text in file and file.lower().endswith('.pdf'):
                download_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                             filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
                if download_path:
                    shutil.copy(file, download_path)
                    messagebox.showinfo("Download Complete", f"PDF saved as {download_path}")
                return

        messagebox.showwarning("Invalid Selection", "Please select a PDF document to download.")

    def back_to_dashboard(self):
        """Go back to the dashboard."""
        response = messagebox.askquestion("Back", "Do you want to return to the dashboard?")
        if response == "yes":
            self.root.quit()  # Close the app

if __name__ == "__main__":
    root = ctk.CTk()
    app = DocumentApp(root)
    root.mainloop()
