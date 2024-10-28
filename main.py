import tkinter as tk
from tkinter import messagebox

# Function to evaluate password strength
def check_password_strength():
    password = entry.get()
    length = len(password)
    
    if length < 6:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 10:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"
    
    # Display strength in the label and color it accordingly
    strength_label.config(text=f"Strength: {strength}", fg=color)

# Create the main window
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("300x200")

# Create and place label and entry for password
label = tk.Label(window, text="Enter Password:")
label.pack(pady=10)

entry = tk.Entry(window, show="*", width=30)
entry.pack(pady=5)

# Create and place a button to check password strength
check_button = tk.Button(window, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

# Create and place a label to display password strength
strength_label = tk.Label(window, text="Strength: ")
strength_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
