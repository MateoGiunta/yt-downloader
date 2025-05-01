from subprocess import check_output
from yt_dlp import YoutubeDL
from tkinter import *       
import subprocess


def menu():
    
    def video():

        def atras():
            video.destroy()
            menu()

        def descargar_video():
            url = e6.get()
            if url.strip() == "" :
                video.destroy()
                menu()
                
            else:    
                ytd_opt ={
                    "default_search": "auto",
                    "format": "mp4/bestvideo/best",
                    
                    

                }

                with YoutubeDL(ytd_opt) as ytd:
                    ytd.download(url)
                
                    


        video = Tk()
        video.geometry("600x400")
        ventana.destroy()
        e1 = Label(video, text="descargar video", bg="red", fg="white")
        e0 = Label(video, text="pon el link del video: ", fg="black")
        e6 = Entry(video, width=50)
        e2 = Button(video, text="descargar", fg="red",command=lambda: descargar_video())
        e3 = Button(video, text="atras", command=lambda: atras())
        e1.pack(fill=X)
        e3.pack(fill=X)
        e0.pack()
        e6.pack()
        e2.pack()
        video.mainloop()


    def audio():
        def atras():
            audio.destroy()
            menu()

        def descargar_audio():
            url = e8.get()
                
                
            ytd_opt ={
            
                'default_search': 'auto',
                "format": "mp3/bestaudio/best",
                
                'postprocessors': [{  # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',

                    }]
                }

            with YoutubeDL(ytd_opt) as ytd:
                ytd.download(url)
            """confirmar=check_output(f"yt-dlp -x --audio-format mp3 '{url}'", shell=True)
            if confirmar:
                e20=Label(audio, text="se descargo con exito")
                e20.pack()
            else:
                e20 = Label(audio, text="no se pudo descargar")
                e20.pack()"""


        audio = Tk()
        audio.geometry("600x400")
        ventana.destroy()
        e1 = Label(audio, text="descargar audio", bg="red", fg="white")
        e0 = Label(audio, text="pon el link del video: ", fg="black")
        e8 = Entry(audio, width=50)
        e2 = Button(audio, text="descargar", fg="red",command=lambda: descargar_audio())
        e3 = Button(audio, text="atras", command=lambda: atras())
        e1.pack(fill=X)
        e3.pack(fill=X)
        e0.pack()
        e8.pack()
        e2.pack()
        audio.mainloop()
        
    def spotify():
        def atras():
            spotify.destroy()
            menu()
        def descargar_cancion():
            if e3.get().strip() == "" :
                spotify.destroy()
                menu()
            else:
                subprocess.run(f"Scripts/python -m spotdl {e3.get().strip()}")


        spotify = Tk()
        spotify.geometry("600x400")
        ventana.destroy()
        e1 = Label(spotify, text="descargar audio spotify", bg="#1ed760", fg="black")
        e2 = Label(spotify, text="pon el link de la cancion: ", fg="black")
        e3 = Entry(spotify, width=50)
        e4 = Button(spotify, text="descargar", fg="green", command=lambda: descargar_cancion())
        e5 = Button(spotify, text="atras", fg="black", command=lambda: atras())
        e6 = Label(spotify, text="")

        e1.pack(fill=X)
        e5.pack(fill=X)
        e2.pack()
        e3.pack()
        e4.pack()
        e6.pack()
        spotify.mainloop()

    ventana = Tk()
    ventana.geometry("600x400")
    e0 = Label(ventana,text="descargador de videos de youtube (también audios de spotify)", fg="white", bg="red")
    e1 = Label(ventana,text="desea descargar el audio o el video", fg="black")
    e2 = Button(ventana,text="video",width=30, command=lambda: video() )
    e3 = Label(ventana,text="")
    e4 = Button(ventana,text="audio",width=30 , command=lambda: audio())
    e5 = Label(ventana,text="")
    e6 = Button(ventana,text="spotify",width=30, command=lambda: spotify())
    
    e0.pack(fill=X)
    e1.pack()
    e2.pack()
    e3.pack()
    e4.pack()
    e5.pack()
    e6.pack()
    ventana.mainloop()
    

if __name__=="__main__":
    menu()

