import os
import yt_dlp

def baixarVideo(url, caminho_pasta):
    caminho_arquivo = os.path.join(caminho_pasta, "%(title)s.%(ext)s")
    ydl_opts = {
        'format': 'best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': caminho_arquivo 
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print('Verifique o caminho e a url inseridas')

baixarVideo('https://www.youtube.com/watch?v=PDvd8NBYaSc', 'C:\\Users\\peron\\OneDrive\\Área de Trabalho\\Codes\\python')