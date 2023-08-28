import tkinter as tk
import ttkbootstrap as ttk
from segno import helpers
import os
import sys


# Add this code on top of window.iconbitmap('xi.icon)
def resource_path(relative_path):
    """ Get absolute path to resource - for our icon """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Create the Window and add to Memory
window=ttk.Window(themename='cyborg')

# Add the Title
window.title('URL Code Generator')

# Add the icon
window.iconbitmap(resource_path('Photo.ico'))

# Create the fixed size of our window
window.geometry("550x750")

lbl_header=ttk.Label(text="Click the button to generate a qrcode")
lbl_header.pack(pady=5)

lbl_name=ttk.Label(text="Your Full Name")
lbl_name.pack(pady=5)

name_entry=ttk.Entry(width=25)
name_entry.pack(pady=5)


lbl_email=ttk.Label(text="Your Email")
lbl_email.pack(pady=5)

email_entry=ttk.Entry(width=25)
email_entry.pack(pady=5)

lbl_url=ttk.Label(text="Your URL")
lbl_url.pack(pady=5)

url_entry=ttk.Entry(width=25)
url_entry.pack(pady=5)

lbl_phone=ttk.Label(text="Your Phone Number")
lbl_phone.pack(pady=5)

phone_entry=ttk.Entry(width=25)
phone_entry.pack(pady=5)

lbl_qrcodename=ttk.Label(text="Enter the name of your Qrcode")
lbl_qrcodename.pack(pady=5)

qrcodename_entry=ttk.Entry(width=25)
qrcodename_entry.pack(pady=5)

def generate_qrcode():
    entry_name=name_entry.get()
    entry_email=email_entry.get()
    entry_url=url_entry.get()
    entry_phone=phone_entry.get()
    entry_qrcodename=qrcodename_entry.get()

    qrcode=helpers.make_mecard(entry_name, entry_email, entry_url, entry_phone)
    qrcode.save(entry_qrcodename, scale=4)
    lbl_infor['text']='QRCode Successfully Saved'


btn_qrcode=ttk.Button(text='Click to Generate', bootstyle="danger", command=generate_qrcode)
btn_qrcode.pack(pady=20)

lbl_infor=ttk.Label(text="")
lbl_infor.pack(pady=15)


window.mainloop()