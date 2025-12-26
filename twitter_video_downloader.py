import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import yt_dlp
import threading
import requests
from io import BytesIO
import os


DOWNLOAD_DIR = os.getcwd()

root = tk.Tk()
root.title("X (Twitter) Video Downloader by Yashvir Gaming")
root.geometry("520x520")
root.resizable(False, False)

url_var = tk.StringVar()
progress_var = tk.DoubleVar()

thumbnail_label = tk.Label(root)
thumbnail_label.pack(pady=10)


def load_thumbnail(url):
    try:
        ydl_opts = {"quiet": True, "skip_download": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            thumb_url = info.get("thumbnail")

        if thumb_url:
            response = requests.get(thumb_url)
            img = Image.open(BytesIO(response.content))
            img = img.resize((420, 240))
            photo = ImageTk.PhotoImage(img)
            thumbnail_label.config(image=photo)
            thumbnail_label.image = photo
    except Exception:
        thumbnail_label.config(image="")

def progress_hook(d):
    if d["status"] == "downloading":
        total = d.get("total_bytes") or d.get("total_bytes_estimate")
        downloaded = d.get("downloaded_bytes", 0)
        if total:
            progress = downloaded / total * 100
            progress_var.set(progress)

def download_video():
    url = url_var.get().strip()
    if not url:
        messagebox.showerror("Error", "Please paste a video URL")
        return

    progress_var.set(0)
    load_thumbnail(url)

    def run():
        try:
            ydl_opts = {
                "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
                "progress_hooks": [progress_hook],
                "merge_output_format": "mp4",
                "quiet": True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            messagebox.showinfo("Done", "Video downloaded successfully!")
            progress_var.set(100)

        except Exception as e:
            messagebox.showerror("Download Failed", str(e))

    threading.Thread(target=run, daemon=True).start()

tk.Label(root, text="Paste X / Twitter Video URL:", font=("Segoe UI", 10)).pack(pady=5)

tk.Entry(root, textvariable=url_var, width=65).pack(pady=5)

ttk.Button(root, text="Download", command=download_video).pack(pady=10)

ttk.Progressbar(
    root,
    orient="horizontal",
    length=450,
    mode="determinate",
    variable=progress_var
).pack(pady=10)

tk.Label(
    root,
    text="Supports: .mp4 | .ts | .mov (auto)",
    font=("Segoe UI", 9),
    fg="gray"
).pack(pady=5)

root.mainloop()
