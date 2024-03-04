import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

SERVER_URL = "http://localhost:8000" # Replace with your server URL

# def login(username, password, account_type):
#     # Make a POST request to the login API endpoint
#     endpoint = "/api/login/"
#     url = SERVER_URL + endpoint
#     data = {
#         "username": username,
#         "password": password,
#         "account_type": account_type,
#     }
#     response = requests.post(url, data=data)
#     return response.json()

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

def adduser(username, password, account_type):
    # Make a POST request to the login API endpoint
    endpoint = "/api/user/"
    url = SERVER_URL + endpoint
    data = {
        "username": username,
        "password": password,
        "account_type": account_type,
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


# Create the root window
root = tk.Tk()

# Set the minimum width of the window to half the screen width
screen_width = root.winfo_screenwidth()
root.minsize(int(screen_width / 2), 400)

# Create the tab control
tab_control = ttk.Notebook(root)

# Create the tabs
home_tab = tk.Frame(tab_control)
reg_tab = tk.Frame(tab_control)
activate_tab = tk.Frame(tab_control)

# Add the tabs to the tab control
tab_control.add(home_tab, text="Home")
tab_control.add(reg_tab, text="Registration")
tab_control.add(activate_tab, text="Activate Account")

# Create the Home fields
home_username_label = tk.Label(home_tab, text="Username")
home_username_label.pack()

home_username_entry = tk.Entry(home_tab)
home_username_entry.pack()

home_password_label = tk.Label(home_tab, text="Password")
home_password_label.pack()

home_password_entry = tk.Entry(home_tab, show="*")
home_password_entry.pack()

home_account_type_label = tk.Label(home_tab, text="Account Type")
home_account_type_label.pack()

# Set up the account type dropdown
account_types = ["Student", "Faculty", "Admin"]
home_account_type_var = tk.StringVar(home_tab)
home_account_type_var.set(account_types[0])
home_account_type_dropdown = tk.OptionMenu(home_tab, home_account_type_var, *account_types)
home_account_type_dropdown.pack()

# def handle_login():
#     username = home_username_label.get()
#     password = home_password_label.get()
#     account_type = home_account_type_label.get().lower()

#     response = login(username, password, account_type)

#     if response["success"]:
#         print("Login successful!")
#         # TODO: Add logic to redirect to appropriate page
#     else:
#         print("Login failed: " + response["message"])


# Create a function to handle the login button click
def handle_login():
    # Get the user input from the entry widgets
    username = home_username_entry.get()
    password = home_password_entry.get()

    # Make a GET request to the server to retrieve all the students
    response = requests.get("http://localhost:8000/api/user/")

    # Check if the GET request was successful
    if response.status_code == 200:
        # Parse the response data as JSON
        students = response.json()

        # Check if the username and password match any of the students
        for student in students:
            if student["username"] == username and student["password"] == password:
                # Redirect to the appropriate page based on the account type
                if student["accounttype"] == "admin":
                    # Open the admin window in a new Python file
                    import admin
                    admin.open_window()
                elif student["accounttype"] == "faculty":
                    # Open the faculty window in a new Python file
                    import faculty
                    faculty.open_window()
                elif student["accounttype"] == "student":
                    # Open the faculty window in a new Python file
                    import addc
                    addc.open_window()
                else:
                    # Show an error message if the account type is invalid
                    messagebox.showerror("Error", "Invalid account type")
                break
        else:
            # Show an error message if the username and password don't match any of the students
            messagebox.showerror("Error", "Invalid username or password")
    else:
        # Show an error message if the GET request failed
        messagebox.showerror("Error", "Failed to retrieve students")


login_button = tk.Button(home_tab, text="Login", command=handle_login)
login_button.pack()


# Create the Registration fields
reg_rno_label = tk.Label(reg_tab, text="Roll No.")
reg_rno_label.pack()

reg_rno_entry = tk.Entry(reg_tab)
reg_rno_entry.pack()

reg_password_label = tk.Label(reg_tab, text="Password")
reg_password_label.pack()

reg_password_entry = tk.Entry(reg_tab, show="*")
reg_password_entry.pack()

reg_name_label = tk.Label(reg_tab, text="Name")
reg_name_label.pack()

reg_name_entry = tk.Entry(reg_tab)
reg_name_entry.pack()

reg_email_label = tk.Label(reg_tab, text="Email")
reg_email_label.pack()

reg_email_entry = tk.Entry(reg_tab)
reg_email_entry.pack()

reg_mobile_label = tk.Label(reg_tab, text="Mobile")
reg_mobile_label.pack()

reg_mobile_entry = tk.Entry(reg_tab)
reg_mobile_entry.pack()

reg_department_label = tk.Label(reg_tab, text="Department")
reg_department_label.pack()

# Set up the department dropdown
departments = ["CSE", "IT", "EEE", "ECE", "Civil", "Mech"]
reg_department_var = tk.StringVar(reg_tab)
reg_department_var.set(departments[0])
reg_department_dropdown = tk.OptionMenu(reg_tab, reg_department_var, *departments)
reg_department_dropdown.pack()

reg_year_label = tk.Label(reg_tab, text="Year")
reg_year_label.pack()

# Set up the year dropdown
years = ["1", "2", "3", "4"]
reg_year_var = tk.StringVar(reg_tab)
reg_year_var.set(years[0])
reg_year_dropdown = tk.OptionMenu(reg_tab, reg_year_var, *years)
reg_year_dropdown.pack()

reg_section_label = tk.Label(reg_tab, text="Section")
reg_section_label.pack()

# Set up the section dropdown
sections = ["A", "B", "C", "D"]
reg_section_var = tk.StringVar(reg_tab)
reg_section_var.set(sections[0])

_reg_section_dropdown = tk.OptionMenu(reg_tab, reg_section_var, *sections)
_reg_section_dropdown.pack()



# Set up the register button
def register():
    data1 = {
        "username": reg_rno_entry.get(),
        "password": reg_password_entry.get(),
        "accounttype": 'student'
    }
    response1 = requests.post("http://localhost:8000/api/user/", data=data1)
    if response1.status_code == 200:
        messagebox.showinfo("Registration Success", "Your account has been registered successfully!")
    else:
        messagebox.showerror("Registration Error", f"Failed to register your account! {str(response1)}")

    data = {
        "rno": reg_rno_entry.get(),
        "password": reg_password_entry.get(),
        "name": reg_name_entry.get(),
        "email": reg_email_entry.get(),
        "mobile": reg_mobile_entry.get(),
        "branch": reg_department_var.get(),
        "year": reg_year_var.get(),
        "section": reg_section_var.get()
    }
    response = requests.post("http://localhost:8000/api/student/", data=data)
    if response.status_code == 200:
        messagebox.showinfo("Registration Success", "Your details has been added")
        reg_rno_label.delete(0, tk.END)
        reg_password_entry.delete(0, tk.END)
        reg_name_entry.delete(0, tk.END)
        reg_email_entry.delete(0, tk.END)
        reg_mobile_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Registration Error", f"Failed to add your data! {str(response)}")


reg_button = tk.Button(reg_tab, text="Register", command=register)
reg_button.pack()

# Create the Activate Account fields
activate_otp_label = tk.Label(activate_tab, text="OTP")
activate_otp_label.pack()

activate_otp_entry = tk.Entry(activate_tab)
activate_otp_entry.pack()

activate_activate_button = tk.Button(activate_tab, text="Activate")
activate_activate_button.pack()

# Pack the tab control
tab_control.pack(expand=True, fill='both')

# Start the main event loop
root.mainloop()





