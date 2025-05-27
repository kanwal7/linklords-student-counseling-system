import tkinter as tk
from tkinter import messagebox

# Dummy user store
users = {}

def register():
    username = reg_username.get()
    password = reg_password.get()
    if username in users:
        messagebox.showerror("Error", "User already exists!")
    else:
        users[username] = password
        messagebox.showinfo("Success", "User registered!")

def login():
    username = login_username.get()
    password = login_password.get()
    if users.get(username) == password:
        messagebox.showinfo("Success", "Logged in successfully!")
    else:
        messagebox.showerror("Error", "Invalid credentials")

# Main window
root = tk.Tk()
root.title("Login and Registration")
root.geometry("300x350")

# Registration Frame
tk.Label(root, text="Register", font=("Arial", 14)).pack()
reg_username = tk.Entry(root)
reg_username.pack(pady=5)
reg_password = tk.Entry(root, show="*")
reg_password.pack(pady=5)
tk.Button(root, text="Register", command=register).pack(pady=10)

# Separator
tk.Label(root, text="--------------------------").pack(pady=10)

# Login Frame
tk.Label(root, text="Login", font=("Arial", 14)).pack()
login_username = tk.Entry(root)
login_username.pack(pady=5)
login_password = tk.Entry(root, show="*")
login_password.pack(pady=5)
tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
