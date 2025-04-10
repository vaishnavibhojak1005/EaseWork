import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import qrcode


class VisitingCardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visiting Card Generator")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Back to Dashboard button at the TOP
        self.back_button = ctk.CTkButton(root, text="⬅ Back to Dashboard", fg_color="red", command=self.back_to_dashboard)
        self.back_button.pack(pady=10, padx=10, anchor="w")

        # Frame for inputs
        self.frame = ctk.CTkFrame(root)
        self.frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Labels & Input Fields
        self.name_label = ctk.CTkLabel(self.frame, text="Your Name:")
        self.name_label.pack(pady=5)
        self.name_entry = ctk.CTkEntry(self.frame, width=300)
        self.name_entry.pack(pady=5)

        self.title_label = ctk.CTkLabel(self.frame, text="Your Title:")
        self.title_label.pack(pady=5)
        self.title_entry = ctk.CTkEntry(self.frame, width=300)
        self.title_entry.pack(pady=5)

        self.contact_label = ctk.CTkLabel(self.frame, text="Contact Number:")
        self.contact_label.pack(pady=5)
        self.contact_entry = ctk.CTkEntry(self.frame, width=300)
        self.contact_entry.pack(pady=5)

        self.email_label = ctk.CTkLabel(self.frame, text="Email Address:")
        self.email_label.pack(pady=5)
        self.email_entry = ctk.CTkEntry(self.frame, width=300)
        self.email_entry.pack(pady=5)

        # Button to select background image
        self.bg_button = ctk.CTkButton(self.frame, text="Select Background Image", command=self.select_background)
        self.bg_button.pack(pady=10)

        # Generate & Download Buttons
        self.generate_button = ctk.CTkButton(self.frame, text="Generate Card", command=self.create_visiting_card)
        self.generate_button.pack(pady=10)

        self.download_button = ctk.CTkButton(self.frame, text="Download Card", command=self.download_card)
        self.download_button.pack(pady=10)

        # Canvas to display the generated visiting card
        self.canvas = ctk.CTkCanvas(root, width=600, height=300)
        self.canvas.pack(pady=10)

        self.bg_image_path = None  # Store background image path

    def select_background(self):
        self.bg_image_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if self.bg_image_path:
            messagebox.showinfo("Background Selected", "Background image selected successfully!")

    def create_visiting_card(self):
        name = self.name_entry.get()
        title = self.title_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()

        if not name or not title or not contact or not email:
            messagebox.showerror("Error", "All fields must be filled!")
            return

        # Load background image if selected
        if self.bg_image_path:
            try:
                bg_image = Image.open(self.bg_image_path).convert("RGBA").resize((600, 300))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load background image: {e}")
                return
        else:
            bg_image = Image.new("RGBA", (600, 300), "white")

        # Create an image with background
        card = Image.new("RGBA", (600, 300))
        card.paste(bg_image, (0, 0), bg_image)
        draw = ImageDraw.Draw(card)

        # Load fonts
        try:
            title_font = ImageFont.truetype("arial.ttf", 28)
            text_font = ImageFont.truetype("arial.ttf", 20)
        except:
            title_font = ImageFont.load_default()
            text_font = ImageFont.load_default()

        # Add text to the card
        draw.text((20, 20), title.upper(), font=title_font, fill="black")
        draw.text((20, 60), name.upper(), font=title_font, fill="black")
        draw.text((20, 100), f"Contact: {contact}", font=text_font, fill="black")
        draw.text((20, 140), f"Email: {email}", font=text_font, fill="black")
        draw.line((0, 180, 600, 180), fill="blue", width=2)

        # Generate QR Code
        qr_data = f"Name: {name}\nTitle: {title}\nContact: {contact}\nEmail: {email}"
        qr = qrcode.make(qr_data)
        qr = qr.resize((100, 100))  # Resize for better fit
        card.paste(qr, (480, 180))  # Paste QR code on the card

        # Display the generated image
        self.show_image(card)

        # Save the visiting card temporarily
        self.card_file = "visiting_card_with_qr.png"
        card.save(self.card_file)
        messagebox.showinfo("Card Generated", "Your visiting card has been generated!")

    def show_image(self, card):
        img = card.copy()
        img.thumbnail((600, 300))
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor="nw", image=img_tk)
        self.canvas.image = img_tk

    def download_card(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            card = Image.open(self.card_file)
            card.save(file_path)
            messagebox.showinfo("Saved", f"Your visiting card has been saved as {file_path}.")

    def back_to_dashboard(self):
        response = messagebox.askquestion("Back", "Do you want to return to the dashboard?")
        if response == "yes":
            self.root.quit()


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("700x650")
    app = VisitingCardApp(root)
    root.mainloop()
