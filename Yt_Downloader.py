# $********IMPORTING MODULES*********$
import tkinter
from tkinter import *
from tkinter import filedialog

from tkinter import messagebox

# import pytube

# $********CREATING WINDOW***********$
wind = tkinter.Tk()
wind.title("YT Video Downloader")
wind.geometry("800x600")
wind.resizable(width=False, height=False)

# $**********CANVAS FOR BG************$
bg = PhotoImage(file="YouTube_Background.png")
canvas1 = Canvas(wind, width=800, height=600, cursor="circle")
canvas1.pack()
canvas1.create_image(0, 0, image=bg, anchor="nw")


def download_video():  # $*********FUNCTIONS TO DOWNLOAD AND CLOSE********$
    try:
        directory = filedialog.askdirectory(initialdir="C:\\Users\\admi\\Downloads")
        from pytube import YouTube
        text = url.get()
        yt = YouTube(text)
        video = yt.streams.filter(res="720p")
        video.first().download(directory)
    except:
        messagebox.showerror("Error", "Please check your network connection and Video URL again")


def close():         
    wind.destroy()


# $********** WIDGETS *************$
url_label = Label(wind, text="Paste your URL", font=("Fixedsys", 16,), bg="white", fg="purple", relief=RIDGE, bd=3)
url_label.place(x=165, y=250, width=145, height=40)

url = Entry(wind, bg="grey", font=("System", 16,), fg="black", relief=SUNKEN, bd=5)
url.place(x=350, y=250, width=435, height=40)


# $********** BUTTONS *************$
download = Button(wind, text="Download", command=download_video, font=("Fixedsys", 16, "bold"), bg="black", fg="green",
                  relief=RAISED, bd=6)
download.place(x=350, y=450)

close = Button(wind, text="Exit", command=close, font=("Fixedsys", 12, "bold"), bg="black", fg="red",
               relief=RAISED, bd=6)
close.place(x=720, y=540)

wind.mainloop()
