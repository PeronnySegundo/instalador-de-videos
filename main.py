import customtkinter as ctk
import yt_dlp
import re

def validar_url_youtube(url):
    if(url == ''):
        label_atualizacao.configure(text='A URL nao pode ser nula', text_color='red')
        return
    padrao = re.compile(
        r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(?:-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|live\/|v\/)?)([\w\-]+)(\S+)?$"
    )
    valido = padrao.match(url)
    if(valido):
        label_atualizacao.configure(text='URL valida', text_color='green')
        baixar_video(url)
        return
    else:
        label_atualizacao.configure(text='URL invalida', text_color='red')

def baixar_video(url):
    titulo = ("%(title)s.%(ext)s")
    ydl_opts = {
        'format': 'best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': titulo 
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            label_atualizacao.configure(text='Baixando...', text_color='green')
            ydl.download([url])
    except Exception as e:
        label_atualizacao.configure(text='Ocorreu algum erro!', text_color='red')
        print('Verifique a url inserida')

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Instalador de vídeos do YouTube')
app.geometry('500x230')

label_url = ctk.CTkLabel(app, text = 'URL do vídeo')
label_url.pack(pady = 10)

entry_url = ctk.CTkEntry(app, placeholder_text='cole a url aqui', width = 400, border_color = '#1f6aa5')
entry_url.pack(pady = 10)

button_baixar = ctk.CTkButton(app, text = 'Download', command=lambda : validar_url_youtube(entry_url.get()))
button_baixar.pack(pady = 15)

label_atualizacao = ctk.CTkLabel(app, text = 'Caso ocorra algum erro será mostrado aqui', text_color='white')
label_atualizacao.pack(pady=15)

app.mainloop()