import tkinter as tk
import requests
from tkinter import ttk

# Define the API URL
api_url = 'http://localhost:8000/api/'

# Create the main window
root = tk.Tk()
root.title("Admin Dashboard")
root.minsize(root.winfo_screenwidth() // 2, 400) # set minimum width to half the screen width

# Create the tabs
tab_control = ttk.Notebook(root)

add_faculty_tab = ttk.Frame(tab_control)
view_faculty_tab = ttk.Frame(tab_control)
view_complaints_tab = ttk.Frame(tab_control)
logout_tab = ttk.Frame(tab_control)

tab_control.add(add_faculty_tab, text='Add Faculty')
tab_control.add(view_faculty_tab, text='View Faculty')
tab_control.add(view_complaints_tab, text='View Complaints')
tab_control.add(logout_tab, text='Logout')

# Add Faculty Tab
add_faculty_username_label = tk.Label(add_faculty_tab, text="Username")
add_faculty_username_label.pack()

add_faculty_username_entry = tk.Entry(add_faculty_tab)
add_faculty_username_entry.pack()

add_faculty_password_label = tk.Label(add_faculty_tab, text="Password")
add_faculty_password_label.pack()

add_faculty_password_entry = tk.Entry(add_faculty_tab, show="*")
add_faculty_password_entry.pack()

add_faculty_name_label = tk.Label(add_faculty_tab, text="Name")
add_faculty_name_label.pack()

add_faculty_name_entry = tk.Entry(add_faculty_tab)
add_faculty_name_entry.pack()

add_faculty_email_label = tk.Label(add_faculty_tab, text="Email")
add_faculty_email_label.pack()

add_faculty_email_entry = tk.Entry(add_faculty_tab)
add_faculty_email_entry.pack()

add_faculty_mobile_label = tk.Label(add_faculty_tab, text="Mobile")
add_faculty_mobile_label.pack()

add_faculty_mobile_entry = tk.Entry(add_faculty_tab)
add_faculty_mobile_entry.pack()

add_faculty_branch_label = tk.Label(add_faculty_tab, text="Branch")
add_faculty_branch_label.pack()

add_faculty_branch_entry = tk.Entry(add_faculty_tab)
add_faculty_branch_entry.pack()


def add_faculty():
    # Get the values from the entries
    username = add_faculty_username_entry.get()
    password = add_faculty_password_entry.get()
    name = add_faculty_name_entry.get()
    email = add_faculty_email_entry.get()
    mobile = add_faculty_mobile_entry.get()
    branch = add_faculty_branch_entry.get()

    # Make the API call to add the faculty
    response = requests.post(api_url + 'add_faculty/', json={
        'username': username,
        'password': password,
        'name': name,
        'email': email,
        'mobile': mobile,
        'branch': branch
    })

    # Show a message box with the response
    tk.messagebox.showinfo('Add Faculty', response.text)

add_faculty_button = tk.Button(add_faculty_tab, text="Add Faculty", command=add_faculty)
add_faculty_button.pack()

# View Faculty Tab
view_faculty_tree = ttk.Treeview(view_faculty_tab, columns=('Username', 'Name', 'Email', 'Mobile', 'Branch'))
view_faculty_tree.heading('#0', text='ID')
view_faculty_tree.heading('Username', text='Username')
view_faculty_tree.heading('Name', text='Name')
view_faculty_tree.heading('Email', text='Email')

# View Faculty Tab
view_faculty_tree = ttk.Treeview(view_faculty_tab, columns=('Username', 'Name', 'Email', 'Mobile', 'Branch'), show='headings')
view_faculty_tree.heading('#0', text='ID')
view_faculty_tree.heading('Username', text='Username')
view_faculty_tree.heading('Name', text='Name')
view_faculty_tree.heading('Email', text='Email')
view_faculty_tree.heading('Mobile', text='Mobile')
view_faculty_tree.heading('Branch', text='Branch')

view_faculty_tree.column('#0', width=50)
view_faculty_tree.column('Username', width=100)
view_faculty_tree.column('Name', width=150)
view_faculty_tree.column('Email', width=200)
view_faculty_tree.column('Mobile', width=100)
view_faculty_tree.column('Branch', width=100)

view_faculty_tree.pack(expand=True, fill='both')

import requests

def api_call(endpoint, method='GET', data=None):
    base_url = 'http://localhost:8000/api/'  # replace with your server's base URL
    url = base_url + endpoint
    headers = {'Content-Type': 'application/json'}
    response = requests.request(method=method, url=url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error {response.status_code}: {response.reason}')
        return None

# Populate View Faculty tab with existing faculty details
faculty_data = api_call('faculty')

for faculty in faculty_data:
    view_faculty_tree.insert('', 'end', text=faculty['id'], values=(faculty['username'], faculty['name'], faculty['email'], faculty['mobile'], faculty['branch']))

# View Complaints Tab
view_complaints_tree = ttk.Treeview(view_complaints_tab, columns=('StudentID', 'ComplaintType', 'Date', 'Description', 'Status', 'Severity'))
view_complaints_tree.heading('#0', text='ID')
view_complaints_tree.heading('StudentID', text='Student ID')
view_complaints_tree.heading('ComplaintType', text='Complaint Type')
view_complaints_tree.heading('Date', text='Date')
view_complaints_tree.heading('Description', text='Description')
view_complaints_tree.heading('Status', text='Status')
view_complaints_tree.heading('Severity', text='Severity')

view_complaints_tree.column('#0', width=50)
view_complaints_tree.column('StudentID', width=100)
view_complaints_tree.column('ComplaintType', width=150)
view_complaints_tree.column('Date', width=100)
view_complaints_tree.column('Description', width=200)
view_complaints_tree.column('Status', width=100)
view_complaints_tree.column('Severity', width=100)

view_complaints_tree.pack(expand=True, fill='both')

# Populate View Complaints tab with existing complaints
complaints_data = api_call('complaint')

for complaint in complaints_data:
    view_complaints_tree.insert('', 'end', text=complaint['studentid'], values=(complaint['studentid'], complaint['complainttype'], complaint['date'], complaint['description'], complaint['status'], 'severity'))

# Logout Tab
logout_label = ttk.Label(logout_tab, text='Are you sure you want to logout?', font=('Arial', 14))
logout_label.pack(pady=20)

logout_button_frame = ttk.Frame(logout_tab)
logout_button_frame.pack(pady=20)

def logout():
    import main
    main.open_window()

yes_button = ttk.Button(logout_button_frame, text='Yes', command=logout)
yes_button.pack(side='left', padx=10)

no_button = ttk.Button(logout_button_frame, text='No', command=logout)
no_button.pack(side='left', padx=10)

# Populate View Complaints tab with existing complaints
complaints_data = api_call('complaint')

for complaint in complaints_data:
    view_complaints_tree.insert('', 'end', text=complaint['studentid'], values=(complaint['studentid'], complaint['complainttype'], complaint['date'], complaint['description'], complaint['status'], 'severity'))

root.mainloop()