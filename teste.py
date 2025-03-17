import yt_dlp

def baixarVideo(url):
    titulo = ("%(title)s.%(ext)s")
    ydl_opts = {
        'format': 'best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': titulo 
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print('Verifique a url inserida')

baixarVideo('https://www.youtube.com/watch?v=PDvd8NBYaSc')