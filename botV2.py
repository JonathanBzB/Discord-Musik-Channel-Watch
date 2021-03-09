#bot.py

#Klassenimport
import discord
import time

client = discord.Client()
Musikkanal = "----Music-Channel----"

@client.event
async def on_message(message):
    #Wenn die Nachricht in den Musikkanal gesendet wird wird diese Nachricht ignoriert 
    if message.channel.name == Musikkanal:
        return()#Weiter ohne was zu tuhen
    #Wenn die Nachricht in einen anderen Kanal als den Musikkanal gesendet wird, werden die Letzten zwei geschriebenen Nachrichten gelöscht
    else:
        if message.content.startswith('-'):
            print('Befehl erkannt') #Konsolenausgabe

            if message.content.startswith('-play') or message.content.startswith('-skip'):
                print('es werden 2 Nachrichten gelöscht') #Konsolenausgabe
                time.sleep(2) #2 Sekunden pause
                await message.channel.purge(limit=2)#Löschung der letzten beiden geschriebenen Zeilen

            else:
                if not message.content.startswith('-play') or not message.content.startswith('-skip'):
                    print('falscher channel') #Konsolenausgabe
                    time.sleep(2) #2 Sekunden pause
                    await message.channel.purge(limit=1)#Löschung der letzten beiden geschriebenen Zeilen


        

#Discort App Token
print("Bot ist Aktiviert")
client.run('----Bot-Token----')