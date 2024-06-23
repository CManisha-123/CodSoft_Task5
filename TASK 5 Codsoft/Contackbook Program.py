import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Contact manager")
contacts = {}

label1 = tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

label3 = tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=5)

label4 = tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
entry4 = tk.Entry(root)
entry4.grid(row=3, column=1, padx=10, pady=5)

def clear_entries():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)

def add_contact():
    name = entry1.get()
    phone = entry2.get()
    email = entry3.get()
    address = entry4.get()

    if name and phone:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Warning", "Name and phone number are required!")

    clear_entries()

def view_contacts():
    if contacts:
        contacts_str = "\n".join([f"{name}: {details['phone']}" for name, details in contacts.items()])
        messagebox.showinfo("Contacts", contacts_str)
    else:
        messagebox.showinfo("Contacts", "No contacts available")

def search_contact():
    name = entry1.get()
    if name in contacts:
        details = contacts[name]
        contact_info = f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}"
        messagebox.showinfo("Contact Details", contact_info)
    else:
        messagebox.showwarning("Warning", "Contact not found!")

def update_contact():
    name = entry1.get()
    if name in contacts:
        phone = entry2.get()
        email = entry3.get()
        address = entry4.get()

        contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showwarning("Warning", "Contact not found!")

def delete_contact():
    name = entry1.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showwarning("Warning", "Contact not found!")

    clear_entries()

button1 = tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, padx=10, pady=5)
button2 = tk.Button(root, text="View Contacts", command=view_contacts).grid(row=4, column=1, padx=10, pady=5)
button3 = tk.Button(root, text="Search Contact", command=search_contact).grid(row=5, column=0, padx=10, pady=5)
button4 = tk.Button(root, text="Update Contact", command=update_contact).grid(row=5, column=1, padx=10, pady=5)
button5 = tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=6, column=0, padx=10, pady=5)

root.mainloop()