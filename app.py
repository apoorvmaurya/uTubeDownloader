import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from pytube.exceptions import RegexMatchError

def download_video():
    try:
        video_url = entry_url.get()
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        stream.download()
        status_label.config(text="Download successful!")
    except RegexMatchError:
        status_label.config(text="Error: Invalid YouTube URL")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and configure the GUI elements
frame = ttk.Frame(root, padding=10)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Enter YouTube Video URL:")
label.grid(column=0, row=0, sticky=tk.W)

entry_url = ttk.Entry(frame, width=40)
entry_url.grid(column=0, row=1)

download_button = ttk.Button(frame, text="Download", command=download_video)
download_button.grid(column=0, row=2)

status_label = ttk.Label(frame, text="")
status_label.grid(column=0, row=3)

# Start the GUI event loop
root.mainloop()
