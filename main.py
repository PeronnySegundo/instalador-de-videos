import customtkinter as ctk
import yt_dlp
import os

def baixarVideo(url, caminho_pasta):
    button_baixar.configure(text = 'Baixando...',command = print('espere!'))
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
            button_baixar.configure(text = 'Donwload', command = baixarVideo(entry_url.get(), entry_caminho_arquivo.get()))
    except Exception as e:
        print('Verifique o caminho e a url inseridas')

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Instalador de vídeos do YouTube')
app.geometry('500x270')

label_url = ctk.CTkLabel(app, text = 'URL do vídeo')
label_url.pack(pady = 10)

entry_url = ctk.CTkEntry(app, placeholder_text='cole a url aqui', width = 400, border_color = '#1f6aa5')
entry_url.pack(pady = 10)

label_caminho_arquivo = ctk.CTkLabel(app, text = 'Caminho onde os arquivos devem ser salvos')
label_caminho_arquivo.pack(pady = 10)

entry_caminho_arquivo = ctk.CTkEntry(app, placeholder_text = 'cole o caminho do arquivo aqui', width = 400, border_color = '#1f6aa5')
entry_caminho_arquivo.pack(pady = 10)

button_baixar = ctk.CTkButton(app, text = 'Download', command = baixarVideo(entry_url.get(), entry_caminho_arquivo.get()))
button_baixar.pack(pady = 15)

app.mainloop()