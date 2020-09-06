from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
import tkinter
from threading import *

# yt = YouTube("https://www.youtube.com/watch?v=GMYpOit3t4Y")



# st = yt.streams.get_highest_resolution()
# print(st)
# for i in st:
#     print(st)

font = ('Verdana',20)
file_size = 0


def completeDownload(stream=None, file_path=None):
    showinfo("Message", "File has been Downloaded...")
    downloadBtn['text'] = "Video Downloaded"
    downloadBtn['state'] = "active"
    urlField.delete(0, END)


def onProgress(stream=None,chunk=None,bytes_remaining=None):
    per = (100*((file_size-bytes_remaining)/file_size))
    downloadBtn['text']= "{:00.0f}% downloaded ".format(per)


def startDownload(url):
    global file_size
    path = askdirectory()
    if(path == None):
        return
    try:
        yt = YouTube(url)
        st = yt.streams.get_highest_resolution()

        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(onProgress)

        file_size = st.filesize
        st.download(output_path=path)
        
    except Exception as e:
        showinfo("Message", "Can't Download Your Video")

def btnClicked():
    try:
        downloadBtn['text'] = "Please Wait..."
        downloadBtn['state'] = "disabled"
        url = urlField.get()
        if url == '':
            showinfo("Message", "Please enter URL")
            downloadBtn['state'] = "active"
            downloadBtn['text'] = "Download Video"
    
        print(url)
        thread = Thread(target=startDownload,args=(url,))
        thread.start()
    except Exception as e:
        showinfo("Message", "Can't Download Your Video")

root = Tk()
root.title("Youtube Downloader")
root.iconbitmap("Resources//icons.ico")
root.geometry("500x600")

img = PhotoImage(file="Resources//image.png")
headingIcon = Label(root,image = img)
headingIcon.pack(side=TOP, pady=5)


urlField = Entry(root,font=font,justify=LEFT)
urlField.pack(side=TOP,fill=X, padx=10)
urlField.focus()

downloadBtn = Button(root,text="Download Video", font=font, relief='ridge', command=btnClicked)
downloadBtn.pack(side=TOP, pady=20)

root.mainloop()