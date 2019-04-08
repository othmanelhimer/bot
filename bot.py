from __future__ import unicode_literals
import time
import telepot
import youtube_dl
from pprint import pprint
import os
import subprocess
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop
#funzione scarica musica
def scarica_mp3(link,chat):
        ydl_opts = {'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                try:
                        ydl.download([link])
                        bot.sendMessage(chat,'Download in corso...')
                        paths=[line[2:]for line in subprocess.check_output("find . -iname '*.mp3'", shell=True).splitli$                        paths=str(paths)
                        print (paths[3:len(paths)-2])
                        audio=open(paths[3:len(paths)-2],'rb')
                        bot.sendAudio(chat, audio)
                        os.system("rm "+paths[2:len(paths)-1])
                except:
                        bot.sendMessage(chat, 'Errore link')
def scarica_mp4(link,chat):
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                try:
                        ydl.download([link])
                        bot.sendMessage(chat,'Download in corso...')
                        pathsr=[line[2:]for line in subprocess.check_output("find . -iname '*.mkv'", shell=True).splitl$                        pathsr=str(pathsr)
                        print (pathsr[3:len(pathsr)-2])
                        video=open(pathsr[3:len(pathsr)-2],'rb')
                        bot.sendVideo(chat, video)
                        os.system("rm "+pathsr[2:len(pathsr)-1])
                except:
                        bot.sendMessage(chat, 'Errore link')
def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        pprint(msg)
        if content_type == 'text':
                username = msg['from']['first_name']
                mess=msg['text']
                iid = msg['message_id']
                print(mess[5:])
                aaa='/start'
                if mess == aaa:
                        bot.sendMessage(chat_id,'Hi '+username+'\nFor download use this command:\n\n/mp3 <link> for dow$
                elif mess[0:4] == '/mp3':
                        scarica_mp3(mess[5:],chat_id)
                elif mess[0:4] == '/mp4':
                        scarica_mp4(mess[5:],chat_id)
                elif mess == '/help':
                        bot.sendMessage(chat_id,'For download use this command:\n\n/mp3 <link> for download file mp3\n/$
                elif mess != '/help' and mess[0:4] != '/mp3' and mess[0:4] != '/mp4':
                        bot.sendMessage(chat_id,'Comando non valido')


TOKEN = '708166222:AAEQ_UtlGPWAjaWpu_AlnBSgrQ8937gKqPs'
bot=telepot.Bot(TOKEN)

MessageLoop(bot, {'chat':handle}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
