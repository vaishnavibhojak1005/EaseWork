import customtkinter as ctk
from tkcalendar import Calendar
from datetime import datetime
import subprocess

# Initialize CTk
ctk.set_appearance_mode("dark")  # Set theme to dark
ctk.set_default_color_theme("blue")

def open_dashboard(root):
    """Opens the dashboard and closes the current window."""
    try:
        subprocess.Popen(["python", "d.py"])  # Ensure "d.py" is your dashboard script
        root.destroy()
    except Exception as e:
        print(f"Error while opening the dashboard: {e}")

def holiday_calendar():
    # Create main window
    root = ctk.CTk()
    root.title("Holiday Calendar 2025")
    root.geometry("900x700")
    root.state("zoomed")  # Start maximized

    # Top bar frame
    top_bar = ctk.CTkFrame(root, height=70, corner_radius=0)
    top_bar.pack(side="top", fill="x")

    # Add "Holiday Calendar" title
    title_label = ctk.CTkLabel(top_bar, text="Holiday Calendar 2025", font=("Arial", 24, "bold"), anchor="center")
    title_label.pack(side='top', padx=20, pady=10)

    # Back Button
    back_button = ctk.CTkButton(top_bar, text="Back to Dashboard", command=lambda: open_dashboard(root))
    back_button.pack(side="left", padx=20)

    # Main content frame
    main_frame = ctk.CTkFrame(root, corner_radius=15)
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Calendar widget
    cal = Calendar(
        main_frame,
        year=2025,
        font=("Verdana", 16),  # Increase font size for better visibility
        selectmode='day',
        date_pattern="yyyy-mm-dd",
        background="black",
        foreground="white",
        bordercolor="gray",
        headersbackground="gray",
        headersforeground="white",
        weekendbackground="lightblue",
        weekendforeground="white",
        othermonthbackground="lightgray",
        othermonthforeground="lightgray"
    )
    cal.pack(pady=20, padx=20, expand=True, fill="both")

    # Event Label
    event_label = ctk.CTkLabel(main_frame, text="", font=("Arial", 18), text_color="white")
    event_label.pack(pady=10)

    # Special dates
    marked_dates = {
        "2025-01-26": "Republic Day",
        "2025-02-19": "Chhatrapati Shivaji Maharaj Jayanti",
        "2025-02-26": "Mahashivratri",
        "2025-03-14": "Holi 2nd Day - Dhuleti",
        "2025-03-30": "Gudi Padwa",
        "2025-03-31": "Eid-Ul-Fitr (Ramzan)",
        "2025-04-06": "Shri Ram Navami",
        "2025-04-10": "Mahavir Jayanti",
        "2025-04-14": "Dr B R Ambedkar Jayanti",
        "2025-04-18": "Good Friday",
        "2025-05-01": "Maharashtra Din",
        "2025-05-12": "Buddha Poornima",
        "2025-06-07": "Bakri ID (Id-Uz-Zuha)",
        "2025-08-15": "Independence Day",
        "2025-08-27": "Ganesh Chaturthi (1st Day)",
        "2025-09-05": "Id A Milad (Milad-Un-Nabi)",
        "2025-10-02": "Mahatma Gandhi Jayanti",
        "2025-10-21": "Diwali (Laxmi Pujan)",
        "2025-10-22": "Diwali (Bali Pratipada)",
        "2025-11-05": "Gurunanak Jayanti",
        "2025-12-25": "Christmas",
    }

    # Function to highlight special dates
    def highlight_dates():
        for date, event in marked_dates.items():
            cal.calevent_create(datetime.strptime(date, "%Y-%m-%d").date(), event, "event")
            cal.tag_config("event", background="darkblue", foreground="white")

    # Function to display events
    def show_event(event):
        selected_date = cal.get_date()
        event_label.configure(text=marked_dates.get(selected_date, "No Event"))

    # Bind calendar selection to event display
    cal.bind("<<CalendarSelected>>", show_event)

    # Highlight special dates
    highlight_dates()

    root.mainloop()

if __name__ == "__main__":
    holiday_calendar()
