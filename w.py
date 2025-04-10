import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os


def open_s_py():
    root.destroy()
    os.system('python s.py')

root = tk.Tk()
root.title("Fullscreen Image Background with Button")
root.attributes('-fullscreen', True)
root.configure(bg="black")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

image = Image.open("C:\\Users\\bhoja\\OneDrive\\Pictures\\project\\w.png")
image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=screen_width, height=screen_height, highlightthickness=0, bg="black")
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

button_width = 600  # Increased width
button_height = 100
corner_radius = 50

button_image = Image.new("RGBA", (button_width, button_height), (0, 0, 0, 0))
draw = ImageDraw.Draw(button_image)
draw.rounded_rectangle((0, 0, button_width, button_height), radius=corner_radius, fill="#ccf297")

font = ImageFont.truetype("arial.ttf", 48)
text = "Get Started with Ease"
text_width, text_height = font.getbbox(text)[2:4]
text_x = (button_width - text_width) // 2
text_y = (button_height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill="black")

button_tk_image = ImageTk.PhotoImage(button_image)

button = tk.Button(
    root,
    image = button_tk_image,
    borderwidth=0,
    highlightthickness=0,
    command=open_s_py,
    cursor="hand2",
    bg="#ccf297",
    activebackground="#ccf297"
)
button.image = button_tk_image

button_x = screen_width // 3.5
button_y = screen_height - 200
canvas.create_window(button_x, button_y, window=button)

root.bind("<Escape>", lambda event: root.destroy())
root.mainloop()
