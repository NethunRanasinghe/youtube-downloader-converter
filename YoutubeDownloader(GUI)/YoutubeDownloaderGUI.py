from tkinter import *
from tkinter import messagebox
import pytube

fpage = Tk()
fpage.geometry("500x100")
fpage.configure(bg="Black")
fpage.title("Youtube Downloader by #Nethun_Ranasinghe (PreAlpha)")
fpage.iconbitmap('C:/Python/Projects/Youtube Downloader/y.ico')
fpage.resizable(width=False, height=False)

messagebox.showinfo("Youtube Downloader", "Copy the Link using (CTRL + C) \nand \npaste it in the box using (CTRL + V) \n  \nThen Click DOWNLOAD.")
messagebox.showinfo("Youtube Downloader", "To download multiple Videos at same time(Not a playlist) \nClick the appropiate button several times to\ncreate multiple instances.")

def SingleDownloadWindow():

    def SingleDownload():
    
        video = pytube.YouTube(U.get())
        stream = video.streams.get_by_itag(18)       
        messagebox.showinfo("Single Youtube Video", "Downloading...")
        stream.download()       
        messagebox.showinfo("Single Youtube Video", "Done!")

    spage = Tk()
    spage.geometry("500x75")
    spage.title("Single Youtube Video")
    spage.iconbitmap('C:/Python/Projects/Youtube Downloader/y.ico')
    spage.configure(bg="Black")
    spage.resizable(width=False, height=False)
    U = Entry(spage,width=500,borderwidth=5)
    SUBbutton = Button(spage, borderwidth=5, text="Download", font=("Consolas 10 bold"), padx=50, pady=10, command=SingleDownload )
    
    U.pack()
    SUBbutton.pack()
    spage.mainloop()

def Playlistwindow():
    
    messagebox.showwarning("Playlist", "You won't be able to exit main menu \nuntill all the videos are downloaded. ")

    def Playlist():
        url = U.get()
        playlist = pytube.Playlist(url)
        for url in playlist:
            video = pytube.YouTube(url)
            stream = video.streams.get_by_itag(18)
            messagebox.showinfo("Playlist", "Downloading...")
            stream.download()
            messagebox.showinfo("Playlist", "Done!")

    
    
    ppage = Tk()
    ppage.geometry("500x75")
    ppage.title("Download a complete Playlist")
    ppage.iconbitmap('C:/Python/Projects/Youtube Downloader/y.ico')
    ppage.configure(bg="Black")
    ppage.resizable(width=False, height=False)
    U = Entry(ppage,width=500,borderwidth=5)
    SUBbutton = Button(ppage, borderwidth=5, text="Download", font=("Consolas 10 bold"), padx=50, pady=10, command=Playlist )

    U.pack()
    SUBbutton.pack()
    ppage.mainloop()


#User Input Buttons

fButton = Button(fpage, borderwidth=5, text="Single Download", font=("Consolas 10 bold"), padx=50, pady=10, command=SingleDownloadWindow)
sButton = Button(fpage, borderwidth=5, text="Download a complete playlist", font=("Consolas 10 bold"), padx=50, pady=10, command=Playlistwindow)
fButton.pack()
sButton.pack()

fpage.mainloop()
