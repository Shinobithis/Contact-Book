import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Contact Book")
    root.geometry("500x700")

    for i in range(5):
        root.grid_columnconfigure(i, weight=1)

    title = tk.Label(root, text="Contact Book", font=("Arial", 24))
    title.grid(row=0, column=0, columnspan=5, pady=20)

    name = tk.Label(root, text="Name: ", font=("Arial", 15))
    name.grid(row=1, column=0, pady=10)

    phone = tk.Label(root, text="Number: ", font=("Arial", 15))
    phone.grid(row=2, column=0, pady=5)

    name_entry = tk.Entry(root, font=("Arial", 12))
    name_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    phone_entry = tk.Entry(root, font=("Arial", 12))
    phone_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5)

    add_btn = tk.Button(
        root, 
        text="Add Contact", 
        font=("Arial", 12), 
        command=lambda: add_contact(name_entry, phone_entry, contact_frame)
    )
    add_btn.grid(row=3, column=0, columnspan=5, pady=18)

    search_entry = tk.Entry(root, font=("Arial", 12))
    search_entry.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

    search_btn = tk.Button(
        root, 
        text="Search", 
        font=("Arial", 12), 
        command=lambda: search_contact(search_entry, contact_frame)
    )
    search_btn.grid(row=4, column=1, pady= 10)

    contact_frame = tk.Frame(root)
    contact_frame.grid(row=5, column=0, columnspan=5, pady=10)
    show_contacts(contact_frame)

    root.mainloop()

def add_contact(name_entry, phone_entry, contact_frame):
    name = name_entry.get().lower()
    phone = phone_entry.get()
    with open('contact.txt', 'a') as file:
        file.write(f"Name: {name} Phone: {phone}\n")
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    show_contacts(contact_frame)

def search_contact(search_entry, contact_frame):

    search = search_entry.get().lower()
    found = False

    with open('contact.txt') as file:
        contacts = file.readlines()
        for line in contacts:
            if search in line:
                show = line.strip()
                search_entry.delete(0, tk.END)
                show_contacts(contact_frame, show)
                found = True

    if not found:
        print("Contact not found.")

def delete_contact(l, contact_frame):
    search = l.split("Phone: ")[1]
    found = False

    with open('contact.txt') as file:
        contacts = file.readlines()

    new_contacts = []
    for line in contacts:
        if search not in line:
            new_contacts.append(line)
        else:
            found = True
    
    with open('contact.txt', 'w') as refile:
        refile.writelines(new_contacts)
    
    if found:
        print("Contact deleted successfully.")
        show_contacts(contact_frame)
    if not found:
        print("Contact not found.")
             
def show_contacts(contact_frame, show = None):
    for widget in contact_frame.winfo_children():
        widget.destroy()
    
    if show:
        row = tk.Label(contact_frame, text=show, font=("Arial", 12))
        row.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        btn = tk.Button(contact_frame, text="X", command=lambda: delete_contact(show, contact_frame))
        btn.grid(row=0, column=1, padx=5, pady=5)
        return
    with open('contact.txt') as file:
        contacts = file.readlines()
        for line in contacts:
            row = tk.Label(contact_frame, text=line.strip(), font=("Arial", 12))
            row.grid(row=contacts.index(line), column=0, sticky="w", padx=10, pady=5)
            btn = tk.Button(contact_frame, text="X", command=lambda l=line: delete_contact(l, contact_frame))
            btn.grid(row=contacts.index(line), column=1, padx=5, pady=5)

main()