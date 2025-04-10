import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize the CustomTkinter app
class TargetApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("📊 Target Progress Dashboard")
        self.geometry("1000x700")
        ctk.set_appearance_mode("dark")  # Set Dark Mode 🌙

        # Title Label
        ctk.CTkLabel(self, text="📊 Target Progress Charts", font=("Arial", 24, "bold")).pack(pady=10)

        # Back Button to Dashboard (Optional, you can link this back to the dashboard)
        self.back_button = ctk.CTkButton(self, text="⬅ Back to Dashboard", command=self.go_to_dashboard)
        self.back_button.pack(pady=5, padx=10, anchor="nw")

        # Frame to hold the charts
        self.chart_frame = ctk.CTkFrame(self)
        self.chart_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Button to generate new progress data
        self.refresh_button = ctk.CTkButton(self, text="🔄 Update Target Progress", command=self.update_charts)
        self.refresh_button.pack(pady=10)

        # Predefined target goals and current progress
        self.target_goals = {
            "Category A": 500,  # Sales or tasks target (example)
            "Category B": 300,
            "Category C": 400,
            "Category D": 600,
            "Category E": 200
        }

        self.current_progress = {
            "Category A": 350,  # Current progress (e.g., tasks completed)
            "Category B": 250,
            "Category C": 150,
            "Category D": 500,
            "Category E": 100
        }

        # Initial charts
        self.update_charts()

    def go_to_dashboard(self):
        """Close this window and open the dashboard (d.py)."""
        self.destroy()

    def update_charts(self):
        """Clear old charts and update with new progress data."""
        for widget in self.chart_frame.winfo_children():
            widget.destroy()  # Remove old plots

        categories = list(self.target_goals.keys())
        target_values = list(self.target_goals.values())
        current_values = [self.current_progress[category] for category in categories]

        # Create Matplotlib figures
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        fig.patch.set_facecolor('#222222')  # Dark background

        pastel_colors = ["#87CEFA", "#9370DB", "#FFB6C1", "#FFD700", "#FF7F50"]  # Light colors

        # Bar Chart: Show target vs progress
        axes[0].bar(categories, target_values, color='gray', label="Target", alpha=0.6)
        axes[0].bar(categories, current_values, color=pastel_colors, label="Progress", alpha=0.9)
        axes[0].set_title("📊 Target vs Progress", fontsize=14, color="white")
        axes[0].set_facecolor("#222222")
        axes[0].tick_params(colors="white")
        axes[0].spines["bottom"].set_color("white")
        axes[0].spines["left"].set_color("white")
        axes[0].legend()

        # Line Chart: Show progress trend over time (dummy example of monthly progress)
        time_period = ["Week 1", "Week 2", "Week 3", "Week 4"]
        progress_trend = [150, 250, 350, 450]  # Dummy data for trend (could be real-time data)
        axes[1].plot(time_period, progress_trend, marker="o", linestyle="-", color="#6A5ACD")  # Soft Purple
        axes[1].set_title("📈 Progress Trend Over Time", fontsize=14, color="white")
        axes[1].set_facecolor("#222222")
        axes[1].tick_params(colors="white")
        axes[1].spines["bottom"].set_color("white")
        axes[1].spines["left"].set_color("white")

        # Embed the Matplotlib figure in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def update_progress(self, category, progress):
        """Update the current progress for a specific category."""
        if category in self.current_progress:
            self.current_progress[category] = progress
            self.update_charts()  # Re-update charts after progress update

# Run the app
if __name__ == "__main__":
    app = TargetApp()
    app.mainloop()
