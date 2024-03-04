# Add Faculty Tab
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import requests
from credentials import get_credentials

# Create the main window
root = tk.Tk()
root.title("Faculty Dashboard")
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
view_complaints_tree = ttk.Treeview(view_complaints_tab, columns=('StudentID', 'ComplaintType', 'Date', 'Description', 'Status', 'Severity','SeverityColor' ))
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
faculty_data = api_call('faculty')
final_fac_data = {}

for fdata in faculty_data:
    if(fdata['username'] == username ):
        final_fac_data = fdata

print("finalFac Data", final_fac_data, final_fac_data['complainttype'], complaints_data)
for complaint in complaints_data:
    if(final_fac_data['complainttype'] == complaint['complainttype']):
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
    
selected_item = 0
def on_click(event):
    item = view_complaints_tree.focus()
    if item:
        item_one = view_complaints_tree.item(item, "text")
        global selected_item
        selected_item = int(item_one)
        print(f"Clicked item: {selected_item}")

# def delete_user():
#     print("id",selected_item)
#     response = api_call(f'complaint/{selected_item}/', method='DELETE')
#     if response:
#         print(f'Complaint {id} has been removed')
#         view_complaints_tree.delete(selected_item)

# def resolve_user():
#     status = 'resolved'
#     data = {'status': status}
#     response = api_call(f'complaint/{selected_item}/', method='PUT', data=data)
#     if response:
#         print(f'Complaint {id} has been resolved')

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
        if(final_fac_data['complainttype'] == complaint['complainttype']):
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
            if(final_fac_data['complainttype'] == complaint['complainttype']):
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


# Add the click listener to the tree
view_complaints_tree.bind("<ButtonRelease-1>", on_click)

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

# Populate View Complaints tab with existing complaints
# complaints_data = api_call('complaint')

# for complaint in complaints_data:
#     view_complaints_tree.insert('', 'end', text=complaint['studentid'], values=(complaint['studentid'], complaint['complainttype'], complaint['date'], complaint['description'], complaint['status'], 'severity'))



# Logout Tab
del_edit_label = ttk.Label(view_complaints_tab, text='Select then click the button below to delete/resolve', font=('Arial', 10))
del_edit_label.pack(pady=10)

del_edit_frame = ttk.Frame(view_complaints_tab)
del_edit_frame.pack(pady=10)

def delete_complaint():
    print(selected_item)
    if(selected_item > 0):
        delete_user()

def resolve_complaint():
    print(selected_item)
    if(selected_item > 0):
        resolve_user()

def edit_complaint():
    import edit_complaint
    edit_complaint.open_window()

del_button = ttk.Button(del_edit_frame, text='Delete', command=delete_complaint)
del_button.pack(side='left', padx=10)

del_button = ttk.Button(del_edit_frame, text='Resolve', command=resolve_complaint)
del_button.pack(side='left', padx=10)

# edit_button = ttk.Button(del_edit_frame, text='Edit', command=edit_complaint)
# edit_button.pack(side='left', padx=10)



# Pack Tab Control
tab_control.pack(expand=1, fill='both')


# Run GUI
root.mainloop()
