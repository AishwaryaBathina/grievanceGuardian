import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import requests
from credentials import get_credentialsfromfile

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
root.title("Home Page")
# root.configure(bg='light blue')

welcome_label = tk.Label(root, text=f"Welcome to our Grievance Guardian!", font=("Arial", 16))
welcome_label.pack()

def set_style():
    # Define the style
    style = ttk.Style()
    
    # Define the color scheme
    primary_color = '#00529b'  # dark blue
    secondary_color = '#ffcd00'  # yellow
    background_color = '#f5f5f5'  # light gray
    complaints_color = '#c6e2ff'  # light blue
    font = 'Helvetica Neue'  # a modern sans-serif font
    
    # Configure the style
    style.theme_use('clam')
    style.configure('TFrame', background='light blue', foreground=primary_color)
    #style.configure("TNotebook", background="#bfe6ff")
    style.configure('TLabel', background=background_color, foreground=primary_color, font=(font, 12, 'bold'))
    style.configure('TButton', background=primary_color, foreground='white', font=(font, 12))
    style.configure('view_complaints_tab.TFrame', background=secondary_color)
    style.configure('Treeview.Heading', foreground='white', background='dark blue', font=(font, 12, 'bold'))
    style.configure('Treeview.column', foreground='white', background=primary_color)
    style.map('Treeview.Column', background=[('!disabled', primary_color)])
    style.configure('Treeview', tag_foreground={'red': 'red', 'green': 'green'}, background='light blue', foreground=primary_color, fieldbackground='#f0f0f0', selectbackground=complaints_color, selectforeground=primary_color, font=(font, 11))
    style.map('TNotebook.Tab', background=[('selected', 'dark blue'), ('active', 'light blue')], foreground=[('selected', 'white'), ('active', 'white')])

    style.configure('view_complaints_tab', background=secondary_color)
    style.configure('TEntry', background=background_color, foreground=primary_color, font=(font, 12))
    
    # Apply the style to all existing widgets
    root.update()
    for widget in root.winfo_children():
        widget.winfo_class() in ('view_complaint_tab', 'TFrame', 'Treeview.column', 'Treeview.Heading', 'TLabel', 'TButton', 'Treeview') and style.configure(widget.winfo_class(), **style.lookup(widget.winfo_class(), 'background', 'foreground', 'font'))
        
# Set the custom style
set_style()







#style.configure("TNotebook.Tab", background="#bfe6ff", selectedbackground="#4a90e2", foreground="#333333")


# Set the minimum width of the window to half the screen width
screen_width = root.winfo_screenwidth()
root.minsize(int(screen_width / 2), 400)

# Create the tab control
tab_control = ttk.Notebook(root)

# Create the tabs
home_tab = tk.Frame(tab_control, bg='light blue')
reg_tab = tk.Frame(tab_control, bg='light blue')
activate_tab = tk.Frame(tab_control, bg='light blue')

# Add the tabs to the tab control
tab_control.add(home_tab, text="Home")
tab_control.add(reg_tab, text="Registration")
tab_control.add(activate_tab, text="Activate Account")

# Set the minimum width of the window to half the screen width
screen_width = root.winfo_screenwidth()
root.minsize(int(screen_width / 2), 400)
# root.configure(background="light blue")


home_form_frame = tk.Frame(home_tab)
home_form_frame.grid(row=0, column=0, padx=600, pady=100, sticky="NS")

reg_form_frame = tk.Frame(reg_tab)
reg_form_frame.grid(row=0, column=0, padx=600, pady=100, sticky="NS")

activation_form_frame = tk.Frame(activate_tab)
activation_form_frame.grid(row=0, column=0, padx=600, pady=100, sticky="NS")

# Create the Home fields
# home_username_label = tk.Label(home_tab, text="Username")
# home_username_label.pack()

# home_username_entry = tk.Entry(home_tab)
# home_username_entry.pack()
home_username_label = tk.Label(home_form_frame, text="Username")
home_username_label.grid(row=0, column=0, padx=10, pady=5)

home_username_entry = tk.Entry(home_form_frame)
home_username_entry.config(width=50)
home_username_entry.grid(row=0, column=1, padx=5, pady=5)

home_password_label = tk.Label(home_form_frame, text="Password")
home_password_label.grid(row=1, column=0, padx=5, pady=5)

home_password_entry = tk.Entry(home_form_frame, show="*")
home_password_entry.config(width=50)
home_password_entry.grid(row=1, column=1, padx=5, pady=5)

home_account_type_label = tk.Label(home_form_frame, text="Account Type")
home_account_type_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Set up the account type dropdown
account_types = ["--Select--","Student", "Faculty", "Admin"]
padded_account_types = [act.ljust(85) for act in account_types]

home_account_type_var = tk.StringVar(home_form_frame)
home_account_type_var.set(account_types[0])
home_account_type_dropdown = tk.OptionMenu(home_form_frame, home_account_type_var, *padded_account_types)
home_account_type_dropdown.config(width=45)
home_account_type_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Create a function to handle the login button click
def handle_login():
    # Get the user input from the entry widgets
    username = home_username_entry.get()
    password = home_password_entry.get()
    accountType = home_account_type_var.get().strip()

    # Make a GET request to the server to retrieve all the students
    response = requests.get("http://localhost:8000/api/user/")

    # Check if the GET request was successful
    if response.status_code == 200 or response.status_code == 201:
        # Parse the response data as JSON
        students = response.json()
        print(students)
        print(username, password, accountType)

        # Check if the username and password match any of the students
        for student in students:
            if student["username"] == username and student["password"] == password and student["accounttype"].strip().lower() == accountType.lower():
                # Redirect to the appropriate page based on the account type
                print(student["username"])
                get_credentialsfromfile(username=username)
                if student["accounttype"].strip().lower() == "admin":
                    # Open the admin window in a new Python file
                    
                    root.destroy()
                    import admin
                    admin.open_window()
                elif student["accounttype"].strip().lower() == "faculty":
                    # Open the faculty window in a new Python file
                    root.destroy()

                    import faculty
                    faculty.open_window()
                elif student["accounttype"].strip().lower() == "student":
                    # Open the faculty window in a new Python file
                    root.destroy()

                    import comp
                    comp.open_window()
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

spacer_label = tk.Label(home_form_frame, height=1)
spacer_label.grid(row=3)

login_button = tk.Button(home_form_frame, text="Login", command=handle_login)
login_button.config(width=20)
login_button.grid(row=4, column=1)


# Create the Registration fields
reg_rno_label = tk.Label(reg_form_frame, text="Roll No:")
reg_rno_label.grid(row=0, column=0, padx=5, pady=5)

reg_rno_entry = tk.Entry(reg_form_frame)
reg_rno_entry.config(width=50)
reg_rno_entry.grid(row=0, column=1, padx=5, pady=5)

reg_password_label = tk.Label(reg_form_frame, text="Password")
reg_password_label.grid(row=1, column=0, padx=5, pady=5)

reg_password_entry = tk.Entry(reg_form_frame, show="*")
reg_password_entry.config(width=50)
reg_password_entry.grid(row=1, column=1, padx=5, pady=5)

reg_name_label = tk.Label(reg_form_frame, text="Name")
reg_name_label.grid(row=2, column=0, padx=5, pady=5)

reg_name_entry = tk.Entry(reg_form_frame)
reg_name_entry.config(width=50)
reg_name_entry.grid(row=2, column=1, padx=5, pady=5)

reg_email_label = tk.Label(reg_form_frame, text="Email")
reg_email_label.grid(row=3, column=0, padx=5, pady=5)

reg_email_entry = tk.Entry(reg_form_frame)
reg_email_entry.config(width=50)
reg_email_entry.grid(row=3, column=1, padx=5, pady=5)

reg_mobile_label = tk.Label(reg_form_frame, text="Mobile")
reg_mobile_label.grid(row=4, column=0, padx=5, pady=5)

reg_mobile_entry = tk.Entry(reg_form_frame)
reg_mobile_entry.config(width=50)
reg_mobile_entry.grid(row=4, column=1, padx=5, pady=5)

reg_department_label = tk.Label(reg_form_frame, text="Department")
reg_department_label.grid(row=5, column=0, padx=5, pady=5)

# Set up the department dropdown
departments = ["--Select--", "CSE", "IT", "EEE", "ECE", "Civil", "Mech"]
padded_departments = [dep.ljust(85) for dep in departments]

reg_department_var = tk.StringVar(reg_form_frame)
reg_department_var.set(departments[0])
reg_department_dropdown = tk.OptionMenu(reg_form_frame, reg_department_var, *padded_departments)
reg_department_dropdown.config(width=45)
reg_department_dropdown.grid(row=5, column=1, padx=5, pady=5)

reg_year_label = tk.Label(reg_form_frame, text="Year")
reg_year_label.grid(row=6, column=0, padx=5, pady=5)

# Set up the year dropdown
years = ["--Select--", "1", "2", "3", "4"]
padded_years = [yrs.ljust(85) for yrs in years]

reg_year_var = tk.StringVar(reg_form_frame)
reg_year_var.set(years[0])
reg_year_dropdown = tk.OptionMenu(reg_form_frame, reg_year_var, *padded_years)
reg_year_dropdown.config(width=45)
reg_year_dropdown.grid(row=6, column=1, padx=5, pady=5)

reg_section_label = tk.Label(reg_form_frame, text="Section")
reg_section_label.grid(row=7, column=0, padx=5, pady=5)

# Set up the section dropdown
sections = ["--Select--","A", "B", "C", "D"]
padded_sections = [sec.ljust(85) for sec in sections]

reg_section_var = tk.StringVar(reg_form_frame)
reg_section_var.set(sections[0])

_reg_section_dropdown = tk.OptionMenu(reg_form_frame, reg_section_var, *padded_sections)
_reg_section_dropdown.config(width=45)
_reg_section_dropdown.grid(row=7, column=1, padx=5, pady=5)



# Set up the register button
def register():
    data1 = {
        "username": reg_rno_entry.get(),
        "password": reg_password_entry.get(),
        "accounttype": 'student'
    }
    response1 = requests.post("http://localhost:8000/api/user/", data=data1)
    if response1.status_code == 200 or response1.status_code == 201:
        messagebox.showinfo("Registration Success", "Your account has been registered successfully!")
    else:
        messagebox.showerror("Registration Error", f"Failed to register your account! {str(response1)}")

    data = {
        "rno": reg_rno_entry.get(),
        "password": reg_password_entry.get(),
        "name": reg_name_entry.get(),
        "email": reg_email_entry.get(),
        "mobile": reg_mobile_entry.get(),
        "branch": reg_department_var.get().strip(),
        "year": reg_year_var.get().strip(),
        "section": reg_section_var.get().strip()
    }

    print("Data", data)
    response = requests.post("http://localhost:8000/api/student/", data=data)
    if response.status_code == 200 or  response.status_code == 201:
        messagebox.showinfo("Registration Success", "Your details has been added")
        reg_rno_entry.delete(0, tk.END)
        reg_password_entry.delete(0, tk.END)
        reg_name_entry.delete(0, tk.END)
        reg_email_entry.delete(0, tk.END)
        reg_mobile_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Registration Error", f"Failed to add your data! {str(response)}")


spacer_label = tk.Label(reg_form_frame, height=2)
spacer_label.grid(row=8)

reg_button = tk.Button(reg_form_frame, text="Register", command=register)
reg_button.config(width=20)
reg_button.grid(row=9, column=1, padx=5, pady=5)

# Create the Activate Account fields
activate_otp_label = tk.Label(activation_form_frame, text="OTP")
activate_otp_label.grid(row=0, column=0)

activate_otp_entry = tk.Entry(activation_form_frame)
activate_otp_entry.grid(row=0, column=1)

activate_activate_button = tk.Button(activation_form_frame, text="Activate")
activate_activate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Pack the tab control
tab_control.pack(expand=True, fill='both')

# Start the main event loop
root.mainloop()





