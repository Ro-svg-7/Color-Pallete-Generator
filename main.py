import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk
import colorgram

root = TkinterDnD.Tk()
root.title("Color Pallete Generator")
root.geometry("800x750")
root.configure(bg="#F5FFFA")

selected_img = tk.StringVar()
status_text = tk.StringVar()

selected_img.set("No image selected")
status_text.set("Waiting for the img...")

def show_image(filepath):
    img = Image.open(filepath)
    img.thumbnail((480,320))

    photo = ImageTk.PhotoImage(img)
    drop_label.config(image = photo, text="")
    drop_label.image = photo

    status_text.set("Image upload successful!")

def upload_img():
    filepath = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if filepath:
        selected_img.set(filepath)
        show_image(filepath)

def drop_img(event):
    filepath = event.data.strip("{}")
    filepath = filepath.replace("{","").replace("}","")
    selected_img.set(filepath)
    show_image(filepath)

def extract_colors(filepath):
    colors = colorgram.extract(filepath,6)

    hex_codes = []

    for color in colors:
        rgb = color.rgb
        hex_code = "#{:02x}{:02x}{:02x}".format(
            rgb.r,
            rgb.g,
            rgb.b
        )

        hex_codes.append(hex_code)
    
    print(hex_codes)
    return hex_codes

def generate_pallete():
    filepath = selected_img.get()
    if filepath == "No image selected":
        status_text.set("Please upload an image first")
        return
    
    extract_colors(filepath)

title_label = tk.Label(
    root,
    text="Color Pallete Generator",
    font=("Arial", 24, "bold"),
    bg="#FFB6C1",
    fg="white",
)
title_label.pack(pady=(25,35))

drop_frame = tk.Frame(
    root,
    width=500,
    height=350,
    bg="#B0E0E6",
    relief="ridge",
    bd=3
)
drop_frame.pack(pady=(10,40))
drop_frame.pack_propagate(False)
drop_frame.drop_target_register(DND_FILES)
drop_frame.dnd_bind("<<Drop>>", drop_img)

drop_label = tk.Label(
    drop_frame,
    text="Drag and Drop your image here",
    font=("Arial", 15, "bold"),
    bg="#B0E0E6",
    fg="black"
)
drop_label.pack(fill="both",expand=True)
drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind("<<Drop>>", drop_img)

upload_button = tk.Button(
    root,
    text="Upload Image",
    font=("Arial", 12, "bold"),
    bg="lightgrey",
    fg="black",
    activebackground="lightgrey",
    padx=25,
    pady=12,
    command=upload_img
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
    pady=12,
    command=generate_pallete
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
