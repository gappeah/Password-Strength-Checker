import string
import tkinter as tk
import customtkinter
from tkinter import messagebox

def check_password_strength(password: str) -> int:
    """Returns a score indicating the strength of the password.
    A higher score means the password is stronger.
    """

    score = 0

    # Check character classes
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    # Check password length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if len(password) >= 20:
        score += 1

    return score

def check_password(password: str) -> None:
    """Checks the password for various issues and updates the GUI with its strength."""

    # Read common passwords file (ensure it exists)
    try:
        with open("common.txt", "r") as f:
            common_passwords = set(f.read().splitlines())
    except FileNotFoundError:
        messagebox.showerror("Error", "Common password file not found.")
        return

    # Check for common password
    if password in common_passwords:
        message_label.configure(text="Password is too common. Your password strength is 0.")
        return

    # Check password strength
    score = check_password_strength(password)

    # Update GUI with feedback
    if score <= 2:
        message_label.configure(text="Password is too weak.")
    elif score == 3:
        message_label.configure(text="Password is average.")
    else:
        message_label.configure(text="Password is strong.")

root = customtkinter.CTk()
root.title("Password Strength Checker")
root.geometry("700x300")

label = customtkinter.CTkLabel(root, text="Please enter your password and check its strength:")
label.pack()

message_label = customtkinter.CTkLabel(root, text="")
message_label.pack(pady=10)

guess_entry = customtkinter.CTkEntry(root, width=200, placeholder_text="Enter your password")
guess_entry.pack(pady=10)

check_button = customtkinter.CTkButton(root, text="Check Password Strength", command=lambda: check_password(guess_entry.get()))
check_button.pack(pady=5)

root.mainloop()
