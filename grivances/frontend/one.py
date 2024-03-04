import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

SERVER_URL = "http://localhost:8000" # Replace with your server URL

def login(username, password, account_type):
    # Make a POST request to the login API endpoint
    endpoint = "/api/login/"
    url = SERVER_URL + endpoint
    data = {
        "username": username,
        "password": password,
        "account_type": account_type,
    }
    response = requests.post(url, data=data)
    return response.json()

def register(roll_no, name, password, email, mobile, department, year, section):
    # Make a POST request to the registration API endpoint
    endpoint = "/api/register/"
    url = SERVER_URL + endpoint
    data = {
        "roll_no": roll_no,
        "name": name,
        "password": password,
        "email": email,
        "mobile": mobile,
        "department": department,
        "year": year,
        "section": section,
    }
    response = requests.post(url, data=data)
    return response.json()

def activate_account(roll_no, otp):
    # Make a POST request to the OTP verification API endpoint
    endpoint = "/api/activate-account/"
    url = SERVER_URL + endpoint
    data = {
        "roll_no": roll_no,
        "otp": otp,
    }
    response = requests.post(url, data=data)
    return response.json()

# Set up the UI
root = tk.Tk()
root.geometry("800x500") # Set the window size
root.minsize(400, 250) # Set the minimum window size

# Set up the tab control
tab_control = ttk.Notebook(root)

# Set up the Login fields
login_tab = ttk.Frame(tab_control)
tab_control.add(login_tab, text="Login")

username_label = tk.Label(login_tab, text="Username")
username_label.pack()

username_entry = tk.Entry(login_tab)
username_entry.pack()

password_label = tk.Label(login_tab, text="Password")
password_label.pack()

password_entry = tk.Entry(login_tab, show="*")
password_entry.pack()

account_type_label = tk.Label(login_tab, text="Account Type")
account_type_label.pack()

account_types = ["Student", "Faculty", "Admin"]
account_type_var = tk.StringVar(login_tab)
account_type_var.set(account_types[0])
account_type_dropdown = tk.OptionMenu(login_tab, account_type_var, *account_types)
account_type_dropdown.pack()

def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    account_type = account_type_var.get().lower()

    response = login(username, password, account_type)

    if response["success"]:
        print("Login successful!")
        # TODO: Add logic to redirect to appropriate page
    else:
        print("Login failed: " + response["message"])

login_button = tk.Button(login_tab, text="Login", command=handle_login)
login_button.pack()

# Set up the Registration fields
reg_tab = ttk.Frame(tab_control)
tab_control.add(reg_tab, text="Registration")

reg_rno_label = tk.Label(reg_tab, text="Roll No.")
reg_rno_label.pack()

reg_rno_entry = tk.Entry(reg_tab)
reg_rno_entry.pack()

reg_name_label = tk.Label(reg_tab, text="Name")
reg_name_label.pack()

reg_name_entry = tk.Entry(reg_tab)
reg_name_entry.pack()

reg_email_label = tk.Label(reg_tab, text="email")
reg_email_label.pack()

reg_email_entry = tk.Entry(reg_tab)
reg_email_entry.pack()

reg_mobile_label = tk.Label(reg_tab, text="mobile")
reg_mobile_label.pack()

reg_mobile_entry = tk.Entry(reg_tab)
reg_mobile_entry.pack()

reg_password_label = tk.Label(reg_tab, text="Password")
reg_password_label.pack()

reg_password_entry = tk.Entry(reg_tab, show="*")
reg_password_entry.pack()

# Set up the department dropdown
departments = ["CSE", "IT", "EEE", "ECE", "Civil", "MEC"]
reg_department_var = tk.StringVar(reg_tab)
reg_department_var.set(departments[0])
reg_department_label = tk.Label(reg_tab, text="Department:")
reg_department_label.pack()
reg_department_dropdown = tk.OptionMenu(reg_tab, reg_department_var, *departments)
reg_department_dropdown.pack()

# Set up the year dropdown
years = ["1", "2", "3", "4"]
reg_year_var = tk.StringVar(reg_tab)
reg_year_var.set(years[0])
reg_year_label = tk.Label(reg_tab, text="Year:")
reg_year_label.pack()
reg_year_dropdown = tk.OptionMenu(reg_tab, reg_year_var, *years)
reg_year_dropdown.pack()

# Set up the section dropdown
sections = ["A", "B", "C", "D"]
reg_section_var = tk.StringVar(reg_tab)
reg_section_var.set(sections[0])
reg_section_label = tk.Label(reg_tab, text="Section:")
reg_section_label.pack()
reg_section_dropdown = tk.OptionMenu(reg_tab, reg_section_var, *sections)
reg_section_dropdown.pack()

# Set up the register button
def register():
    data = {
        "rno": reg_rno_label.get(),
        "password": reg_password_entry.get(),
        "name": reg_name_entry.get(),
        "email": reg_email_entry.get(),
        "mobile": reg_mobile_entry.get(),
        "branch": reg_department_var.get(),
        "year": reg_year_var.get(),
        "section": reg_section_var.get()
    }
    response = requests.post("http://localhost:8000/api/student/create/", data=data)
    if response.status_code == 200:
        messagebox.showinfo("Registration Success", "Your account has been registered successfully!")
        reg_rno_label.delete(0, tk.END)
        reg_password_entry.delete(0, tk.END)
        reg_name_entry.delete(0, tk.END)
        reg_email_entry.delete(0, tk.END)
        reg_mobile_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Registration Error", "Failed to register your account!")

reg_button = tk.Button(reg_tab, text="Register", command=register)
reg_button.pack()

# Set up the activate account tab
activate_tab = ttk.Frame(tab_control)
tab_control.add(activate_tab, text="Activate Account")

# Set up the OTP label and entry
activate_otp_label = tk.Label(activate_tab, text="OTP")
activate_otp_label.pack()
activate_otp_entry = tk.Entry(activate_tab)
activate_otp_entry.pack()

# Set up the activate button
def activate_account():
    data = {
        "rno": reg_rno_label.get(),
        "otp": activate_otp_entry.get()
    }
    response = requests.post("http://localhost:8000/api/student/activate/", data=data)
    if response.status_code == 200:
        messagebox.showinfo("Activation Success", "Your account has been activated successfully!")
        reg_rno_label.delete(0, tk.END)
        activate_otp_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Activation Error", "Failed to activate your account!")

activate_button = tk.Button(activate_tab, text="Activate", command=activate_account)
activate_button.pack()

root.mainloop()