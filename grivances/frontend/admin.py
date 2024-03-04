import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from credentials import get_credentials
# Define the API URL
api_url = 'http://localhost:8000/api/'

# Create the main window
root = tk.Tk()
root.title("Admin Dashboard")
root.minsize(root.winfo_screenwidth() // 2, 400) # set minimum width to half the screen width

username = get_credentials()
print("Username", username)

welcome_label = tk.Label(root, text=f"Welcome to the Admin Dashboard, {username}!", font=("Arial", 16))
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
# Create the tabs
tab_control = ttk.Notebook(root)

add_faculty_tab = ttk.Frame(tab_control)
view_faculty_tab = ttk.Frame(tab_control)
view_complaints_tab = ttk.Frame(tab_control)

tab_control.add(add_faculty_tab, text='Add Faculty')
tab_control.add(view_faculty_tab, text='View Faculty')
tab_control.add(view_complaints_tab, text='View Complaints')

addfaculty_form_frame = tk.Frame(add_faculty_tab)
addfaculty_form_frame.grid(row=0, column=0, padx=600, pady=100, sticky="NS")

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
    view_faculty_tree.insert('', 'end', text=faculty['name'], values=(faculty['username'], faculty['name'], faculty['email'], faculty['mobile'], faculty['branch']))


def update_faculty():
    # Populate View Faculty tab with existing faculty details
    faculty_data = api_call('faculty')
    view_faculty_tree.delete(*view_faculty_tree.get_children())
    
    view_faculty_tree.column('#0', width=50)
    view_faculty_tree.column('Username', width=100)
    view_faculty_tree.column('Name', width=150)
    view_faculty_tree.column('Email', width=200)
    view_faculty_tree.column('Mobile', width=100)
    view_faculty_tree.column('Branch', width=100)

    for faculty in faculty_data:
        view_faculty_tree.insert('', 'end', text=faculty['name'], values=(faculty['username'], faculty['name'], faculty['email'], faculty['mobile'], faculty['branch']))

# Add Faculty Tab
add_faculty_username_label = tk.Label(addfaculty_form_frame, text="Username:")
add_faculty_username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

add_faculty_username_entry = tk.Entry(addfaculty_form_frame)
add_faculty_username_entry.config(width=50)
add_faculty_username_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

add_faculty_password_label = tk.Label(addfaculty_form_frame, text="Password:")
add_faculty_password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

add_faculty_password_entry = tk.Entry(addfaculty_form_frame, show="*")
add_faculty_password_entry.config(width=50)
add_faculty_password_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")


add_faculty_name_label = tk.Label(addfaculty_form_frame, text="Name:")
add_faculty_name_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

add_faculty_name_entry = tk.Entry(addfaculty_form_frame)
add_faculty_name_entry.config(width=50)
add_faculty_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

add_faculty_email_label = tk.Label(addfaculty_form_frame, text="Email:")
add_faculty_email_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

add_faculty_email_entry = tk.Entry(addfaculty_form_frame)
add_faculty_email_entry.config(width=50)
add_faculty_email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

add_faculty_mobile_label = tk.Label(addfaculty_form_frame, text="Mobile:")
add_faculty_mobile_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

add_faculty_mobile_entry = tk.Entry(addfaculty_form_frame)
add_faculty_mobile_entry.config(width=50)
add_faculty_mobile_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

add_faculty_department_label = tk.Label(addfaculty_form_frame, text="Department:")
add_faculty_department_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

department_options = ['--Select--','CSE', 'IT', 'EEE', 'ECE', 'Civil', 'Mechanical']
padded_departments = [dep.ljust(85) for dep in department_options]

add_faculty_department_var = tk.StringVar(addfaculty_form_frame)
add_faculty_department_var.set(department_options[0])
add_faculty_department_menu = tk.OptionMenu(addfaculty_form_frame, add_faculty_department_var, *padded_departments)
add_faculty_department_menu.config(width=45)
add_faculty_department_menu.grid(row=5, column=1, padx=5, pady=5, sticky="w")

add_faculty_branch_label = tk.Label(addfaculty_form_frame, text="Branch")
add_faculty_branch_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

add_faculty_branch_entry = tk.Entry(addfaculty_form_frame)
add_faculty_branch_entry.config(width=50)
add_faculty_branch_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

add_faculty_complaint_type_label = tk.Label(addfaculty_form_frame, text="Complaint Type:")
add_faculty_complaint_type_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

complaint_type_options = ['--Select--','Ragging', 'Fee', 'Library', 'Canteen', 'Neatness', 'Teaching', 'Bus', 'Sports', 'Infrastructure', 'Social Issues', 'Others']
padded_complaint_type_options = [dep.ljust(85) for dep in complaint_type_options]

add_faculty_complaint_var = tk.StringVar(addfaculty_form_frame)
add_faculty_complaint_var.set(complaint_type_options[0])
add_faculty_complaint_type_menu = tk.OptionMenu(addfaculty_form_frame, add_faculty_complaint_var, *padded_complaint_type_options)
add_faculty_complaint_type_menu.config(width=45)
add_faculty_complaint_type_menu.grid(row=7, column=1, padx=5, pady=5, sticky="w")

def add_faculty():
    print("Inside Add Facultyu")
    # Get the values from the entries
    username = add_faculty_username_entry.get()
    password = add_faculty_password_entry.get()
    name = add_faculty_name_entry.get()
    email = add_faculty_email_entry.get()
    mobile = add_faculty_mobile_entry.get()
    branch = add_faculty_branch_entry.get().strip()
    dept = add_faculty_department_var.get().strip()
    complainttype = add_faculty_complaint_var.get().strip() 

    # Make the API call to add the faculty
    response = requests.post(api_url + 'faculty/', json={
        'username': username,
        'password': password,
        'name': name,
        'email': email,
        'mobile': mobile,
        'branch': dept,
        'complainttype': complainttype
    })

    response1 = requests.post(api_url + 'user/', json={
        "username": username,
        "password": password,
        "accounttype": 'faculty'
    })

    # Show a message box with the response
    messagebox.showinfo('Success', 'Faculty Added successfully')
    update_faculty()

spacer_label = tk.Label(addfaculty_form_frame, height=2)
spacer_label.grid(row=8)

add_faculty_button = tk.Button(addfaculty_form_frame, text="Add Faculty", command=add_faculty)
add_faculty_button.config(width=20)
add_faculty_button.grid(row=9, column=1, padx=5, pady=5)

# View Complaints Tab
view_complaints_tree = ttk.Treeview(view_complaints_tab, columns=('StudentID', 'ComplaintType', 'Date', 'Description', 'Status', 'Severity', 'SeverityColor'))
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
    complaint_type = complaint['complainttype']
    if complaint_type in ['Ragging', 'Social Issues']:
        severity = 'High'
        tag = 'red'
    elif complaint_type in ['Library', 'Canteen', 'Neatness', 'Teaching', 'Bus', 'Sports', 'Infrastructure']:
        severity = 'Medium'
        tag = 'light green'
    else:
        severity = 'Low'
        tag = ''
    view_complaints_tree.insert('', 'end', text=complaint['id'], values=(complaint['studentid'], complaint['complainttype'], complaint['date'], complaint['description'], complaint['status'], severity), tags=(tag,))
    # configure the background color based on the severity tag
    style = ttk.Style()
    style.configure(f"{tag}.Treeview", background=tag)
    view_complaints_tree.tag_configure(tag, background=tag)
    
# Logout Tab
logout_tab = ttk.Frame(tab_control)
tab_control.add(logout_tab, text='Logout')

# Logout Tab
logout_label = ttk.Label(logout_tab, text='Are you sure you want to logout?', font=('Arial', 14))
logout_label.pack(pady=20)

logout_button_frame = ttk.Frame(logout_tab)
logout_button_frame.pack(pady=20)

def delete_user():
    global selected_item
    print("id",selected_item)
    response = api_call(f'complaint/{selected_item}/', method='DELETE')
    print(f'Complaint {selected_item} has been removed')
    messagebox.showinfo('Success', 'Complaint deleted successfully')
    # view_complaints_tree.delete(selected_item)
    selected_item = 0
    
    # Clear the existing data in the treeview
    for item in view_complaints_tree.get_children():
        print(item)
        view_complaints_tree.delete(item)
    
    # Re-populate the treeview with updated data
    complaints_data = api_call('complaint')
    print(complaints_data)
    for complaint in complaints_data:
        complaint_type = complaint['complainttype']
        if complaint_type in ['Ragging', 'Social Issues']:
            severity = 'High'
            tag = 'red'
        elif complaint_type in ['Library', 'Canteen', 'Neatness', 'Teaching', 'Bus', 'Sports', 'Infrastructure']:
            severity = 'Medium'
            tag = 'light green'
        else:
            severity = 'Low'
            tag = ''
        view_complaints_tree.insert('', 'end', text=complaint['id'], values=(complaint['studentid'], complaint['complainttype'], complaint['date'], complaint['description'], complaint['status'], severity), tags=(tag,))


selected_item = 0
def on_click(event):
    item = view_complaints_tree.focus()
    if item:
        item_one = view_complaints_tree.item(item, "text")
        global selected_item
        selected_item = int(item_one)
        print(f"Clicked item: {selected_item}")

def resolve_user():
    global selected_item
    status = 'resolved'
    data = {'status': status}
    response = api_call(f'complaint/{selected_item}/', method='PUT', data=data)
    if response:
        print(f'Complaint {id} has been resolved')
        messagebox.showinfo('Success', 'Complaint resolved successfully')
        selected_item = 0
        
        # Clear the existing data in the treeview
        for item in view_complaints_tree.get_children():
            print(item)
            view_complaints_tree.delete(item)
            
        complaints_data = api_call('complaint')
        print(complaints_data)
        for complaint in complaints_data:
            complaint_type = complaint['complainttype']
            if complaint_type in ['Ragging', 'Social Issues']:
                severity = 'High'
                tag = 'red'
            elif complaint_type in ['Library', 'Canteen', 'Neatness', 'Teaching', 'Bus', 'Sports', 'Infrastructure']:
                severity = 'Medium'
                tag = 'light green'
            else:
                severity = 'Low'
                tag = ''
            view_complaints_tree.insert('', 'end', text=complaint['studentid'], values=(complaint['studentid'], complaint['complainttype'], complaint['date'], complaint['description'], complaint['status'], severity), tags=(tag,))


del_edit_label = ttk.Label(view_complaints_tab, text='Select then click the button below to delete/resolve', font=('Arial', 10))
del_edit_label.pack(pady=10)

del_edit_frame = ttk.Frame(view_complaints_tab)
del_edit_frame.pack(pady=10)

view_complaints_tree.bind("<ButtonRelease-1>", on_click)

def delete_complaint():
    print(selected_item)
    if(selected_item > 0):
        delete_user()

def resolve_complaint():
    print(selected_item)
    if(selected_item > 0):
        resolve_user()

del_button = ttk.Button(del_edit_frame, text='Delete', command=delete_complaint)
del_button.pack(side='left', padx=10)

del_button = ttk.Button(del_edit_frame, text='Resolve', command=resolve_complaint)
del_button.pack(side='left', padx=10)


def logout():
    root.destroy()

    import main
    main.open_window()

yes_button = ttk.Button(logout_button_frame, text='Yes', command=logout)
yes_button.pack(side='left', padx=10)

no_button = ttk.Button(logout_button_frame, text='No', command=logout)
no_button.pack(side='left', padx=10)

# Pack Tab Control
tab_control.pack(expand=1, fill='both')

# Set Add Faculty Tab as default
tab_control.select(add_faculty_tab)

# Run GUI
root.mainloop()