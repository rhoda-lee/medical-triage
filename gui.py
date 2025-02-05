import tkinter as tk
from tkinter import ttk, messagebox
import requests
import ttkbootstrap as tb  # Modern styling for Tkinter

# Function to send symptoms to Flask API
def check_priority():
    symptoms = entry.get().strip().lower().split(",")
    if not symptoms or symptoms == [""]:
        messagebox.showerror("Error", "Please enter symptoms!")
        return

    response = requests.post("http://127.0.0.1:5000/classify", json={"symptoms": symptoms})
    if response.status_code == 200:
        result = response.json()
        messagebox.showinfo("Diagnosis", f"Priority: {result['priority']}\n{result['message']}")
    else:
        messagebox.showerror("Error", "Server error. Try again.")

# Create a themed Tkinter window
root = tb.Window(themename="superhero")  # Modern dark theme
root.title("Nexus Hospital Triage System")
root.geometry("450x350")

# Header Label
label = ttk.Label(root, text="Enter Symptoms", font=("Helvetica", 16, "bold"))
label.pack(pady=15)

# Entry field
entry = ttk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=10, ipady=5)

# Button
button = ttk.Button(root, text="Check Priority", command=check_priority, bootstyle="primary")
button.pack(pady=20)

# Run the app
root.mainloop()
