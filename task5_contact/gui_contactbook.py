import customtkinter as ctk
from tkinter import messagebox
import json
import os

# ---------------- Appearance ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FILE_NAME = "contacts.json"

contacts = []


# ---------------- File Functions ----------------
def load_contacts():
    global contacts
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            contacts = json.load(file)
    refresh_contacts()


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# ---------------- Display ----------------
def refresh_contacts():
    contact_box.delete("1.0", "end")

    if not contacts:
        contact_box.insert("end", "No contacts available.")
        return

    for contact in contacts:
        contact_box.insert(
            "end",
            f"👤 {contact['Name']}\n"
            f"📞 {contact['Phone']}\n"
            f"📧 {contact['Email']}\n"
            f"🏠 {contact['Address']}\n"
            "-----------------------------------------\n"
        )


# ---------------- Add ----------------
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and Phone are required.")
        return

    contacts.append({
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    })

    save_contacts()
    refresh_contacts()
    clear_entries()


# ---------------- Search ----------------
def search_contact():
    keyword = search_entry.get().lower()

    contact_box.delete("1.0", "end")

    found = False

    for contact in contacts:
        if keyword in contact["Name"].lower():
            contact_box.insert(
                "end",
                f"👤 {contact['Name']}\n"
                f"📞 {contact['Phone']}\n"
                f"📧 {contact['Email']}\n"
                f"🏠 {contact['Address']}\n"
                "-----------------------------------------\n"
            )
            found = True

    if not found:
        contact_box.insert("end", "Contact not found.")


# ---------------- Delete ----------------
def delete_contact():
    name = name_entry.get()

    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contacts.remove(contact)
            save_contacts()
            refresh_contacts()
            clear_entries()
            messagebox.showinfo("Success", "Contact deleted.")
            return

    messagebox.showerror("Error", "Contact not found.")


# ---------------- Update ----------------
def update_contact():
    name = name_entry.get()

    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contact["Phone"] = phone_entry.get()
            contact["Email"] = email_entry.get()
            contact["Address"] = address_entry.get()

            save_contacts()
            refresh_contacts()
            clear_entries()

            messagebox.showinfo("Success", "Contact updated.")
            return

    messagebox.showerror("Error", "Contact not found.")


# ---------------- Clear ----------------
def clear_entries():
    name_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    email_entry.delete(0, "end")
    address_entry.delete(0, "end")
    search_entry.delete(0, "end")


# ---------------- Window ----------------
app = ctk.CTk()

app.title("Modern Contact Book")
app.geometry("750x650")
app.resizable(False, False)

title = ctk.CTkLabel(
    app,
    text="📒 Contact Book",
    font=("Arial", 30, "bold")
)

title.pack(pady=15)

# ---------------- Input Frame ----------------
frame = ctk.CTkFrame(app)

frame.pack(padx=20, pady=10, fill="x")

ctk.CTkLabel(frame, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = ctk.CTkEntry(frame, width=250)
name_entry.grid(row=0, column=1)

ctk.CTkLabel(frame, text="Phone").grid(row=1, column=0, padx=10, pady=10)
phone_entry = ctk.CTkEntry(frame, width=250)
phone_entry.grid(row=1, column=1)

ctk.CTkLabel(frame, text="Email").grid(row=2, column=0, padx=10, pady=10)
email_entry = ctk.CTkEntry(frame, width=250)
email_entry.grid(row=2, column=1)

ctk.CTkLabel(frame, text="Address").grid(row=3, column=0, padx=10, pady=10)
address_entry = ctk.CTkEntry(frame, width=250)
address_entry.grid(row=3, column=1)

# ---------------- Buttons ----------------
button_frame = ctk.CTkFrame(app, fg_color="transparent")

button_frame.pack(pady=10)

ctk.CTkButton(
    button_frame,
    text="➕ Add",
    command=add_contact
).grid(row=0, column=0, padx=10)

ctk.CTkButton(
    button_frame,
    text="✏ Update",
    command=update_contact
).grid(row=0, column=1, padx=10)

ctk.CTkButton(
    button_frame,
    text="🗑 Delete",
    command=delete_contact
).grid(row=0, column=2, padx=10)

# ---------------- Search ----------------
search_frame = ctk.CTkFrame(app)

search_frame.pack(fill="x", padx=20)

search_entry = ctk.CTkEntry(
    search_frame,
    width=350,
    placeholder_text="Search by Name"
)

search_entry.grid(row=0, column=0, padx=10, pady=10)

ctk.CTkButton(
    search_frame,
    text="🔍 Search",
    command=search_contact
).grid(row=0, column=1)

# ---------------- Contact Box ----------------
contact_box = ctk.CTkTextbox(
    app,
    width=680,
    height=250,
    font=("Arial", 15)
)

contact_box.pack(pady=20)

load_contacts()

app.mainloop()