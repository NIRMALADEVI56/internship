import tkinter as tk
import random
import string
def generate_password():
    length=int(length_entry.get())
    all_characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(all_characters)for _ in range(length))
    password_label.config(text=f"Generated Password: \n{password}")
root=tk.Tk()
root.title("Password Generator")
tk.Label(root,text="Enter password length:").grid(row=0, column=0, padx=10, pady=5)
length_entry=tk.Entry(root,width=10)
length_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root,text="Generate Password",command=generate_password).grid(row=1,column=0, columnspan=2, pady=10)
password_label=tk.Label(root,text="Generate Password:")
password_label.grid(row=2, column=0, columnspan=2, pady=5)
root.mainloop()
