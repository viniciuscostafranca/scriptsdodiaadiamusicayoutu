
from __future__ import unicode_literals
import os
import subprocess
 
import youtube_dl
 
 
class Playlist():
   def __init__(self, playListUrl,diretorioPrinciapl):
       
       self.diretorio_principal=diretorioPrinciapl;
       self._playListUrl = playListUrl
       self.ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True,})
       self.video = ""
 
       with self.ydl:
           result = self.ydl.extract_info \
           (self._playListUrl,
           download=False) 
 
           if 'entries' in result:
               
               video = result['entries']
 
              
               for i, item in enumerate(video):
                   video = result['entries'][i]['webpage_url']
                   print(video)
                   ydl_opts = {
                       'format': 'bestaudio/best',
                       'postprocessors': [{
                           'key': 'FFmpegExtractAudio',
                           'preferredcodec': 'mp3',
                           'preferredquality': '192',
                       }],
                   }
                   with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                       print(' -ok-')
                       ydl.download([video])

 
 
def runMusica():
   diretorio_principal=input('Caminho completo da pasta onde vocë quer fazer o download das musicas:')
   
   ydl_opts = {
       'format': 'bestaudio/best',
       'postprocessors': [{
           'key': 'FFmpegExtractAudio',
           'preferredcodec': 'mp3',
           'preferredquality': '192',
       }],
   }
   #download de uma unica musica
   #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       #ydl.download([''])
 
   url=input('Cole aqui a url da playlist do you:')
   objPlaylist =Playlist(url,diretorio_principal);
   
 
if __name__ == "__main__":
    runMusica()  

