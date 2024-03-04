# Add Faculty Tab
from tkinter import ttk
import tkinter as tk

import requests


# Create the main window
root = tk.Tk()
root.title("Admin Dashboard")
root.minsize(root.winfo_screenwidth() // 2, 400) # set minimum width to half the screen width

# Create the tabs
tab_control = ttk.Notebook(root)
view_complaints_tab = ttk.Frame(tab_control)

tab_control.add(view_complaints_tab, text='View Complaints')

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
logout_tab = ttk.Frame(tab_control)
tab_control.add(logout_tab, text='Logout')

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

# Pack Tab Control
tab_control.pack(expand=1, fill='both')


# Run GUI
root.mainloop()
