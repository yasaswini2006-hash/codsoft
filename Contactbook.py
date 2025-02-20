import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.geometry("800x500")
window.title("ContactBook")
window.config(bg="black")
contacts=[]
def add_contact():
    name=name_entry.get().strip()
    phone=phone_entry.get()
    email=email_entry.get()
    if name!="":
        contacts.append((name,phone,email))
        messagebox.showinfo("Save","Contact Saved Successfully")
    name_entry.delete(0,tk.END) 
    phone_entry.delete(0,tk.END)   
    email_entry.delete(0,tk.END)
    update_listbox()
def remove_contact():
    selected=contacts_listbox.curselection()
    if selected:
        index=selected[0]
        del contacts[index]
        update_listbox()
        messagebox.showinfo("Deleted","Contact Deleted Successfully")    
def display_contacts():
    for contact in contacts:
        messagebox.showinfo("Details","Name  :  "+contact[0]+
                            '\n'+"Phone  :  "+contact[1]+
                            '\n'+"Email  :  "+contact[2])    
def update_listbox():
    contacts_listbox.delete(0,tk,END)
    for contact in contacts:
        contacts_listbox.insert(tk,END,contact[0])
heading_label=tk.Label(window,
                       text="ContactBook",font=("Arial",30,"bold"),
                       foreground="white",
                       bg="black",) 
heading_label.place(x=300,y=3)
name_label=tk.Label(window,
                    text="Name:",
                    font=("Arial",17,"bold"),
                    foreground="white",
                    bg="black")
name_label.grid(row=0,column=0)
name_label.place(x=80,y=70)
name_entry=tk.Entry(window,
                    font=("Arial",17,"bold"),width=20)
name_entry.grid(row=0,column=1)                   
name_entry.place(x=200,y=70)
phone_label=tk.Label(window,text="Phone:",
                     font=("Arial",17,"bold"),
                     foreground="white",
                     bg="black")
phone_label.grid(row=1,column=0)
phone_label.place(x=80,y=120)
phone_entry=tk.Entry(window,
                     font=("Arial",17,"bold"),width=20)
phone_entry.grid(row=1,column=1)
phone_entry.place(x=200,y=120)
email_label=tk.Label(window,
                     text="Email:",
                     font=("Arial",17,"bold"),
                     foreground="white",
                     bg="black")  
email_label.grid(row=2,column=0)
email_label.place(x=80,y=170)
email_entry=tk.Entry(window,
                     font=("Arial",17,"bold"),width=20)
email_entry.grid(row=2,column=1)
email_entry.place(x=200,y=170) 
add_button=tk.Button(window,
                     text="ADD CONTACT",
                     command=add_contact,
                     font=("Tahona",13,"bold"),
                     relief="raised",
                     borderwidth=4,
                     width=18,
                     activeforeground="white",
                     background="green",
                     activebackground="dark green")
add_button.grid(rowspan=1)       
add_button.place(x=50,y=280)
remove_button=tk.Button(window,
                        text="REMOVE CONTACT",
                        command=remove_contact,
                        font=("Tahona",13,"bold"),
                        relief="raised",
                        borderwidth=4,
                        width=18,
                        activeforeground="white",
                        background="red",
                        activebackground="dark red")
remove_button.grid(rowspan=1)
remove_button.place(x=50,y=330)
display_button=tk.Button(window,
                        text="DISPLAY CONTACT",
                        command=display_contacts,
                        font=("Tahona",13,"bold"),
                        relief="raised",
                        borderwidth=4,
                        width=18,
                        activeforeground="white",
                        background="Light blue",
                        activebackground="dark blue")
display_button.grid(rowspan=1)
display_button.place(x=50,y=380)
conhead_label=tk.Label(window,
                       text="CONTACT LIST",
                        font=("Arial",20,"bold"),
                        foreground="white",
                        bg="black")
conhead_label.place(x=510,y=230)
contacts_listbox=tk.Listbox(window,
                            font=("Arial",12),width=40)
contacts_listbox.place(x=400,y=200)
window.mainloop()        