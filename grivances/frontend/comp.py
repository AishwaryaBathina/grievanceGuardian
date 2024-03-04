import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import scrolledtext
from credentials import get_credentials
import requests

# Define the API URL
api_url = 'http://localhost:8000/api/'

# Create the main window
root = tk.Tk()
root.title("Student Dashboard")
root.minsize(root.winfo_screenwidth() // 2, 400) # set minimum width to half the screen width

username = get_credentials()
print("Username", username)

welcome_label = tk.Label(root, text=f"Welcome, {username}!", font=("Arial", 16))
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

view_complaints_tab = ttk.Frame(tab_control)
tab_control.add(view_complaints_tab, text='View Complaints')
add_complaint_tab = ttk.Frame(tab_control)
tab_control.add(add_complaint_tab, text='Add Complaint')

addComplaint_form_frame = tk.Frame(add_complaint_tab)
addComplaint_form_frame.grid(row=0, column=0, padx=600, pady=100, sticky="NS")

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


def updateComplaits():
    view_complaints_tree.delete(*view_complaints_tree.get_children())
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
        if(complaint['studentid'] == username):
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
            print("severity 63",severity)
            view_complaints_tree.insert('', 'end', text=complaint['id'], values=(complaint['studentid'], complaint['complainttype'], complaint['date'], complaint['description'], complaint['status'], severity), tags=(tag,))

    
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
    if(complaint['studentid'] == username):
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
        print("severity 63",severity)
    
        view_complaints_tree.insert('', 'end', text=complaint['id'], values=(complaint['studentid'], complaint['complainttype'], complaint['date'], complaint['description'], complaint['status'], severity), tags=(tag,))
        style = ttk.Style()
        style.configure(f"{tag}.Treeview", background=tag)
        view_complaints_tree.tag_configure(tag, background=tag)
def add_complaint():
    complaint_data = {
        'studentid': complaint_student_id_entry.get(),
        'complainttype': complaint_type_var.get(),
        'date': complaint_date_entry.get(),
        'description': complaint_desc_entry.get("1.0", "end-1c"),
        'status': 'pending', # Default status
        'severity': 'Low' # Default severity set to low
    }
    
    
    # Make POST request to REST API
    response = requests.post('http://localhost:8000/api/complaint/', data=complaint_data)
    
    # Show success message
    messagebox.showinfo('Success', 'Complaint added successfully')
    
    # Clear the form
    complaint_student_id_entry.delete(0, tk.END)
    complaint_type_var.set(complaint_type_options[0])
    complaint_date_entry.delete(0, tk.END)
    complaint_desc_entry.delete(1.0, tk.END)

    updateComplaits()


# Add Complaint Form
complaint_student_id_label = ttk.Label(addComplaint_form_frame, text='Student ID')
complaint_student_id_entry = ttk.Entry(addComplaint_form_frame)
complaint_student_id_entry.config(width=50)


complaint_type_options = ['--Select--', 'Ragging', 'Fee', 'Library', 'Canteen', 'Neatness', 'Teaching', 'Bus', 'Sports', 'Infrastructure', 'Social Issues', 'Others']
padded_complaint_type_options = [dep.ljust(85) for dep in complaint_type_options]

complaint_type_label = ttk.Label(addComplaint_form_frame, text='Complaint Type')
complaint_type_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

complaint_type_var = tk.StringVar(addComplaint_form_frame)
complaint_type_var.set(complaint_type_options[0])
complaint_type_menu = tk.OptionMenu(addComplaint_form_frame, complaint_type_var, *padded_complaint_type_options)
complaint_type_menu.config(width=45)
complaint_type_menu.grid(row=1, column=1, padx=5, pady=5, sticky="w")

complaint_date_label = ttk.Label(addComplaint_form_frame, text='Date')
complaint_date_entry = DateEntry(addComplaint_form_frame, width=50, background='darkblue', foreground='white', borderwidth=2)
complaint_date_entry.config(date_pattern='dd/MM/yyyy')

complaint_desc_label = ttk.Label(addComplaint_form_frame, text='Description')
complaint_desc_entry = scrolledtext.ScrolledText(addComplaint_form_frame, width=40, height=10)
# complaint_desc_entry.config(width=50)


complaint_student_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
complaint_student_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# complaint_type_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
# complaint_type_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

complaint_date_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
complaint_date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

complaint_desc_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
complaint_desc_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

spacer_label = tk.Label(addComplaint_form_frame, height=2)
spacer_label.grid(row=8)

add_complaint_button = ttk.Button(addComplaint_form_frame, text='Add Complaint', command=add_complaint)
add_complaint_button.config(width=20)
add_complaint_button.grid(row=4, columnspan=2, padx=5, pady=5)


# Logout Tab
logout_tab = ttk.Frame(tab_control)
tab_control.add(logout_tab, text='Logout')

# Logout Tab
logout_label = ttk.Label(logout_tab, text='Are you sure you want to logout?', font=('Arial', 14))
logout_label.pack(pady=20)

logout_button_frame = ttk.Frame(logout_tab)
logout_button_frame.pack(pady=20)

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
tab_control.select(view_complaints_tab)

# Run GUI
root.mainloop()
