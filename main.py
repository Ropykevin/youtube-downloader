import tkinter as tk
import customtkinter
from pytube import YouTube
import threading


def startDownload():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink, on_complete_callback=on_progress)
        video = ytobject.streams.get_highest_resolution()
        title.configure(text=ytobject.title)
        finish_label.configure(text="")
        threading.Thread(target=download_thread, args=(video,)).start()
    except Exception as e:
        finish_label.configure(text=f"Download error: {e}", text_color="red")


def download_thread(video):
    try:
        video.download()
        finish_label.configure(
            text="Downloaded successfully!", text_color="green")
    except Exception as e:
        finish_label.configure(text=f"Download error: {e}", text_color="red")


def on_progress(stream,  bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    app.after(100, update_progress, per, float(percentage_of_completion / 100))


def update_progress(per, percentage):
    progres_percentage.configure(text=per + '%')
    progres_bar.set(percentage)


# system settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")  # screen resolution
app.title("YouTube Downloader")

# adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# link input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=50, textvariable=url_var)
link.pack()

# finish downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

# download button
download_btn = customtkinter.CTkButton(
    app, text="Download", command=startDownload)
download_btn.pack(padx=10, pady=10)

# progress bar
progres_percentage = customtkinter.CTkLabel(app, text="0%")
progres_percentage.pack()

progres_bar = customtkinter.CTkProgressBar(app, width=400)
progres_bar.set(0)
progres_bar.pack(padx=10, pady=10)

# run app
app.mainloop()
