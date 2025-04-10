import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

# Create the main window
root = tk.Tk()
root.title("Monthly Calendar for 2025")
root.geometry("800x600")  # Adjusted window size
root.configure(bg="black")  # Set background color to black

# Create a notebook widget (which allows for tab switching)
notebook = ttk.Notebook(root)

# List of months
months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

# Style for the notebook to ensure black background and white text
style = ttk.Style()
style.configure("TNotebook", background="black", borderwidth=0)
style.configure("TNotebook.Tab", background="black", foreground="white", padding=[10, 5], font=("Verdana", 12))
style.map("TNotebook.Tab", background=[("selected", "black")], foreground=[("selected", "white")])

# Color palette from Coolors
color_palette = {
    "color1": "#600a6a",  # Dark purple
    "color2": "#562779",  # Purple
    "color3": "#292954",  # Dark blue
    "color4": "#150d35",  # Very dark blue
    "color5": "#80aebd",  # Light blue
}

# List of dates to mark with different colors
marked_dates = {
    "2025-01-01": {"event": "New Year's Day", "color": "color1"},
    "2025-02-14": {"event": "Valentine's Day", "color": "color2"},
    "2025-07-04": {"event": "Independence Day", "color": "color3"},
    "2025-12-25": {"event": "Christmas Day", "color": "color4"},
    "2025-06-21": {"event": "Summer Solstice", "color": "color5"},
}

# Function to mark specific dates on the calendar
def mark_dates(calendar_widget, marked_dates, color_palette):
    for date_str, details in marked_dates.items():
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        event = details["event"]
        color_tag = details["color"]
        calendar_widget.calevent_create(date, event, color_tag)  # Add event to the date with a color tag
    # Configure the tags with the color palette
    for tag, color in color_palette.items():
        calendar_widget.tag_config(tag, background=color, foreground="white")  # Style marked dates

# Create and add tabs for each month
for month_index, month in enumerate(months, start=1):
    tab_frame = ttk.Frame(notebook, style="Black.TFrame")
    
    # Create a Calendar widget for the month
    cal = Calendar(
        tab_frame,
        year=2025,
        month=month_index,
        background=color_palette["color4"],  # Very dark blue
        foreground="white",
        bordercolor=color_palette["color3"],  # Dark blue
        headersbackground=color_palette["color2"],  # Purple
        headersforeground="white",
        selectbackground=color_palette["color5"],  # Light blue
        selectforeground="black",
        normalbackground=color_palette["color4"],  # Very dark blue
        normalforeground="white",
        weekendbackground=color_palette["color4"],  # Very dark blue
        weekendforeground="white",
        othermonthbackground=color_palette["color4"],  # Very dark blue for previous/next month dates
        othermonthforeground=color_palette["color5"],  # Light blue for previous/next month dates
        font=("Verdana", 12),
        date_pattern="yyyy-mm-dd"
    )
    cal.pack(pady=20, padx=20, fill="both", expand=True)

    # Mark specific dates on the calendar
    mark_dates(cal, marked_dates, color_palette)

    notebook.add(tab_frame, text=month)

# Style for the frame to ensure black background
style.configure("Black.TFrame", background="black")

# Pack the notebook widget to display the tabs
notebook.pack(expand=True, fill="both")

# Start the Tkinter event loop
root.mainloop()