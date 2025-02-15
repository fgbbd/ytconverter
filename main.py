import yt_dlp
from Flask import app

def descargar_video(url):
    opciones = {
        'outtmpl': '%(title)s.%(ext)s', 
        'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }]
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

# Ejemplo de uso
url = "https://youtu.be/TVeJyFHbUIo"
descargar_video(url)
