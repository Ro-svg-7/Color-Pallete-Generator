import tkinter as tk
from tkinter import filedialog, ttk
from tkinterdnd2 import TkinterDnD, DND_FILES

root = TkinterDnD.Tk()
root.title("Color Pallete Generator")
root.geometry("700x650")
root.configure(bg="#F5FFFA")

selected_img = tk.StringVar()
status_text = tk.StringVar()

selected_img.set("No image selected")
status_text.set("Waiting for the img...")

title_label = tk.Label(
    root,
    text="Color Pallete Generator",
    font=("Arial", 24, "bold"),
    bg="#FFB6C1",
    fg="white",
)
title_label.pack(pady=(25,35))

drop_label = tk.Label(
    root,
    text="Drag and Drop your image here",
    font=("Arial", 15, "bold"),
    bg="#B0E0E6",
    fg="black",
    width=50,
    height=8,
    relief="ridge",
    bd=3
)
drop_label.pack(pady=(10,40))
drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind("<<Drop>>")

upload_button = tk.Button(
    root,
    text="Upload Image",
    font=("Arial", 12, "bold"),
    bg="lightgrey",
    fg="black",
    activebackground="lightgrey",
    padx=25,
    pady=12
)
upload_button.pack(pady=(0,30))

generate_button = tk.Button(
    root,
    text="Generate dem colours!",
    font=("Arial", 12, "bold"),
    bg="#EFE40F",
    fg="red",
    activebackground="#EFE40F",
    relief="flat",
    padx=25,
    pady=12
)
generate_button.pack(pady=(0,50))

status_label = tk.Label(
    root,
    textvariable=status_text,
    font=("Arial", 14, "bold"),
    bg="#F5FFFA",
    fg="#1E0FEF"
)
status_label.pack(pady=(20,0))
root.mainloop()
