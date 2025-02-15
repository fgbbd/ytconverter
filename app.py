from threading import Thread

import yt_dlp
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        return 'No has insertado una URL.'

    # Crear un hilo para ejecutar la descarga sin bloquear el servidor
    thread = Thread(target=descargar_video, args=(url,))
    thread.start()
    
    return f"Descarga en progreso para: {url}."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
