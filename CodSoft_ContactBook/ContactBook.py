import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # List to store contacts
        self.contacts = []

        # Top frame for input fields and add button
        self.frame_top = tk.Frame(root)
        self.frame_top.pack(pady=10)

        # Bottom frame for listbox and action buttons
        self.frame_bottom = tk.Frame(root)
        self.frame_bottom.pack(pady=10)

        # Name label and entry field
        self.lbl_name = tk.Label(self.frame_top, text="Name:")
        self.lbl_name.grid(row=0, column=0, padx=5)
        self.entry_name = tk.Entry(self.frame_top)
        self.entry_name.grid(row=0, column=1, padx=5)

        # Phone label and entry field
        self.lbl_phone = tk.Label(self.frame_top, text="Phone:")
        self.lbl_phone.grid(row=1, column=0, padx=5)
        self.entry_phone = tk.Entry(self.frame_top)
        self.entry_phone.grid(row=1, column=1, padx=5)

        # Email label and entry field
        self.lbl_email = tk.Label(self.frame_top, text="Email:")
        self.lbl_email.grid(row=2, column=0, padx=5)
        self.entry_email = tk.Entry(self.frame_top)
        self.entry_email.grid(row=2, column=1, padx=5)

        # Address label and entry field
        self.lbl_address = tk.Label(self.frame_top, text="Address:")
        self.lbl_address.grid(row=3, column=0, padx=5)
        self.entry_address = tk.Entry(self.frame_top)
        self.entry_address.grid(row=3, column=1, padx=5)

        # Add contact button
        self.btn_add = tk.Button(self.frame_top, text="Add Contact", command=self.add_contact)
        self.btn_add.grid(row=4, columnspan=2, pady=10)

        # Listbox to display contacts
        self.contact_listbox = tk.Listbox(self.frame_bottom, width=50)
        self.contact_listbox.pack(side=tk.LEFT, padx=10)

        # View contacts button
        self.btn_view = tk.Button(self.frame_bottom, text="View Contacts", command=self.view_contacts)
        self.btn_view.pack(side=tk.LEFT, padx=5)

        # Search contact button
        self.btn_search = tk.Button(self.frame_bottom, text="Search Contact", command=self.search_contact)
        self.btn_search.pack(side=tk.LEFT, padx=5)

        # Update contact button
        self.btn_update = tk.Button(self.frame_bottom, text="Update Contact", command=self.update_contact)
        self.btn_update.pack(side=tk.LEFT, padx=5)

        # Delete contact button
        self.btn_delete = tk.Button(self.frame_bottom, text="Delete Contact", command=self.delete_contact)
        self.btn_delete.pack(side=tk.LEFT, padx=5)

    # Function to add a new contact
    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        if name and phone and email and address:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    # Function to view all contacts
    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    # Function to search for a contact
    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    # Function to update a contact
    def update_contact(self):
        selected_contact_index = self.contact_listbox.curselection()
        if selected_contact_index:
            selected_contact = self.contacts[selected_contact_index[0]]
            name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=selected_contact['name'])
            phone = simpledialog.askstring("Update Contact", "Enter new phone:", initialvalue=selected_contact['phone'])
            email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=selected_contact['email'])
            address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=selected_contact['address'])
            if name and phone and email and address:
                self.contacts[selected_contact_index[0]] = {"name": name, "phone": phone, "email": email, "address": address}
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.view_contacts()
            else:
                messagebox.showwarning("Input Error", "Please fill in all fields")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update")

    # Function to delete a contact
    def delete_contact(self):
        selected_contact_index = self.contact_listbox.curselection()
        if selected_contact_index:
            self.contacts.pop(selected_contact_index[0])
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.view_contacts()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete")

    # Function to clear input fields
    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
