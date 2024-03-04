# Add Complaint Tab
from tkinter import messagebox, ttk
import tkinter as tk
import requests


# Create the root window
root = tk.Tk()

# Set the minimum width of the window to half the screen width
screen_width = root.winfo_screenwidth()
root.minsize(int(screen_width / 2), 400)

# Create the tab control
tab_control = ttk.Notebook(root)

add_complaint_tab = ttk.Frame(tab_control)
tab_control.add(add_complaint_tab, text='Add Complaint')

# Add Complaint Form
complaint_student_id_label = ttk.Label(add_complaint_tab, text='Student ID')
complaint_student_id_entry = ttk.Entry(add_complaint_tab)

complaint_type_label = ttk.Label(add_complaint_tab, text='Complaint Type')
complaint_type_entry = ttk.Entry(add_complaint_tab)

complaint_date_label = ttk.Label(add_complaint_tab, text='Date')
complaint_date_entry = ttk.Entry(add_complaint_tab)

complaint_desc_label = ttk.Label(add_complaint_tab, text='Description')
complaint_desc_entry = ttk.Entry(add_complaint_tab)

complaint_status_label = ttk.Label(add_complaint_tab, text='Status')
complaint_status_entry = ttk.Entry(add_complaint_tab)

def add_complaint():
    complaint_data = {
        'studentid': complaint_student_id_entry.get(),
        'complainttype': complaint_type_entry.get(),
        'date': complaint_date_entry.get(),
        'description': complaint_desc_entry.get(),
        'status': complaint_status_entry.get(),
        'severity': 'Low' # Default severity set to low
    }
    
    # Make POST request to REST API
    response = requests.post('http://localhost:8000/api/complaint/', data=complaint_data)
    
    # Show success message
    messagebox.showinfo('Success', 'Complaint added successfully')
    
    # Clear the form
    complaint_student_id_entry.delete(0, tk.END)
    complaint_type_entry.delete(0, tk.END)
    complaint_date_entry.delete(0, tk.END)
    complaint_desc_entry.delete(0, tk.END)
    complaint_status_entry.delete(0, tk.END)

add_complaint_button = ttk.Button(add_complaint_tab, text='Add Complaint', command=add_complaint)

complaint_student_id_label.grid(row=0, column=0, padx=5, pady=5)
complaint_student_id_entry.grid(row=0, column=1, padx=5, pady=5)

complaint_type_label.grid(row=1, column=0, padx=5, pady=5)
complaint_type_entry.grid(row=1, column=1, padx=5, pady=5)

complaint_date_label.grid(row=2, column=0, padx=5, pady=5)
complaint_date_entry.grid(row=2, column=1, padx=5, pady=5)

complaint_desc_label.grid(row=3, column=0, padx=5, pady=5)
complaint_desc_entry.grid(row=3, column=1, padx=5, pady=5)

complaint_status_label.grid(row=4, column=0, padx=5, pady=5)
complaint_status_entry.grid(row=4, column=1, padx=5, pady=5)

def viewc():
    import faculty
    faculty.open_window()

add_complaint_button.grid(row=5, columnspan=2, padx=5, pady=5, command=viewc)

# Pack the tab control
tab_control.pack(expand=True, fill='both')

# Start the main event loop
root.mainloop()