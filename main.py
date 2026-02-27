import customtkinter as ctk
from pytubefix import YouTube
import tkinter as tk
import os
from PIL import Image
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app = ctk.CTk()
app.resizable(False, False)
app.title("TubeLoader")
img = tk.PhotoImage(file=resource_path("icon.png"))
app.wm_iconphoto(True, img)
app.iconbitmap(resource_path("icon.ico"))

app.geometry("700x350")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

header_photo = ctk.CTkImage(light_image=Image.open(resource_path("icon.png")), size=(70,70))

labelphoto = ctk.CTkLabel(app, text="", image=header_photo)
labelphoto.pack(pady=(10,0))

label_header = ctk.CTkLabel(app, text="TubeLoader - Fast and Reliable", font=("Arial", 24, "bold"))
label_header.pack(fill="x", padx = 10, pady = (30,0))

label_url = ctk.CTkLabel(app, text="Paste the link here down below!")
label_url.pack(pady=10)

entry = ctk.CTkEntry(app, width=300)
entry.pack(pady=(10,30))

def download():
    button.configure(text="Downloading...", state="disabled")
    app.update_idletasks()
    url = entry.get()
    if url:
        try:
            yt = YouTube(url)
            print(yt.title)
            ys = yt.streams.get_highest_resolution()
            ys.download(output_path="videos")
            entry.delete(0, 'end')
            button.configure(text="Download!", state="normal")
        except Exception as e:
            print(f"Errore: {e}")
    else:
        print("not valid")
        button.configure(text="Download!", state="normal")

def audio():
    audio_button.configure(text="Downloading...", state="disabled")
    app.update_idletasks()
    url = entry.get()
    if url:
        try:
            yt = YouTube(url)
            print(yt.title)
            ys = yt.streams.get_audio_only()
            ys.download(output_path="audio")
            entry.delete(0, 'end')
            audio_button.configure(text="Audio Downloaded!", state="normal")
        except Exception as e:
            print(f"Errore: {e}")
    else:
        print("not valid")
        audio_button.configure(text="Download!", state="normal")

button = ctk.CTkButton(app, width=45, height=30, corner_radius=5, command=download, text="Download!", fg_color="red")
button.pack(pady=5)

audio_button = ctk.CTkButton(app, width=45, height=30, corner_radius=5, command=audio, text="Audio Download!", fg_color="green")
audio_button.pack(pady=5)

app.mainloop()