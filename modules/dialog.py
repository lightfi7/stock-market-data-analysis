import tkinter as tk
from tkinter import ttk

from fontTools.ttx import process


def run_window(cb):
    def submit_action():
        start_date = start_entry.get()
        end_date = end_entry.get()
        print(f"Start Date: {start_date}")
        print(f"End Date: {end_date}")
        # Add your action here
        # dialog.destroy()  # Close the dialog after submission
        if cb:
            cb(start_date, end_date)

    def on_close():
        dialog.destroy()  # Close the dialog
        root.quit()  # Exit the application
        exit(0)

    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the root window (optional if you only want to show the dialog)

    # Create a dialog window
    dialog = tk.Toplevel(root)
    dialog.title("Stock Market Data Analysis")
    dialog.geometry("400x200")  # Set the size of the dialog window
    dialog.config(bg='#f0f0f0')  # Set a background color

    # Bind the dialog's close event
    dialog.protocol("WM_DELETE_WINDOW", on_close)

    # Style settings
    label_font = ("Arial", 12)
    entry_font = ("Arial", 11)
    button_font = ("Arial", 12, "bold")

    # Create a label and entry for the start date
    label_start = tk.Label(dialog, text="Start date:", font=label_font, bg='#f0f0f0')
    label_start.grid(row=0, column=0, padx=20, pady=10, sticky='w')

    start_entry = ttk.Entry(dialog, font=entry_font, width=30)
    start_entry.insert(0, "2017-01-01")
    start_entry.grid(row=0, column=1, padx=20, pady=10)

    # Create a label and entry for the end date
    label_end = tk.Label(dialog, text="End date:", font=label_font, bg='#f0f0f0')
    label_end.grid(row=1, column=0, padx=20, pady=10, sticky='w')

    end_entry = ttk.Entry(dialog, font=entry_font, width=30)
    end_entry.insert(0, "2017-12-31")
    end_entry.grid(row=1, column=1, padx=20, pady=10)

    # Create a submit button
    submit_button = ttk.Button(dialog, text="Submit", command=submit_action)
    submit_button.grid(row=2, column=0, columnspan=2, pady=20)

    # Configure grid weights for better spacing
    dialog.grid_columnconfigure(0, weight=1)
    dialog.grid_columnconfigure(1, weight=1)

    # Run the main event loop
    root.mainloop()
