#coding:utf-8

import discord
from discord import Game
from discord.ext import commands
import json
import os, sys
import math
import random
import os

compte = {}

with open('bddlea.json') as f:
    compte = json.load(f)


client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:", client.user.name)
    print("ID:", client.user.id)


    await client.change_presence(game=Game(name="/aide"))

@client.event
async def on_message(message):



####################
    

    if message.content.startswith("/aide"):
        try :
            commande = message.content.split("/aide ")[1]
            if commande == "fdj":
                await client.send_message(message.channel, "Oh ! tu as besoin d'aide avec la commande `fdj` ? Je vais t'expliquer ça ^^\n\nLa commande `fdj` simule le grattage d'un tiket à gratter.\nutilise la syntaxe `/fdj [tiket]` pour gratter le tiket correspondant. voici la liste des tikets actuellement disponibles :\n-numero_fetiche")
        except :
            await client.send_message(message.channel, "Bonjour " + message.author.name +" voici la liste des commandes disponibles :\n`/fdj` : simule le grattage du ticket choisi\n`/info`: quelques infos sur moi :3\n`/ping` : suis-je en ligne ?")

    elif message.content.startswith("/fdj"):
        try :
            ticket = message.content.split("/fdj ")[1]
            if ticket == "numero_fetiche":
                resultat = int(random.randint(1, 1499940))
                if resultat >= 1 and resultat <= 3 :
                    await client.send_message(message.channel, "Tiens ? `" + message.author.name + "` vient de gratter un **numéro fétiche** ! Et... OMG !!! IL VIENT DE GAGNER **1000€** !\nFélicitations `" + message.author.name + "` ! Tu avais **0.0002%** de chances  d'obtenir ce resultat ! Tu fais partager les copains ? :joy:")
                elif resultat >= 4 and resultat <= 50 :
                    await client.send_message(message.channel, "Tiens ? `" + message.author.name + "` vient de gratter un **numéro fétiche** ! Et... WAHOU !! IL VIENT DE GAGNER **100€** !\nFélicitations `" + message.author.name + "` ! Tu avais **0.0034%** de chances  d'obtenir ce resultat !")
                elif resultat >= 51 and resultat <= 150 :
                    await client.send_message(message.channel, "Tiens ? `" + message.author.name + "` vient de gratter un **numéro fétiche** ! Et... COOL ! Il vient de gagner **25€** !\nFélicitations `" + message.author.name + "` ! Tu avais **0.01%** de chances  d'obtenir ce resultat ! Tu peux m'inviter au restaurant si tu veux :smirk:")
                elif resultat >= 151 and resultat <= 800 :
                    await client.send_message(message.channel, "Tiens ? `" + message.author.name + "` vient de gratter un **numéro fétiche** ! Et... Oh ! Il vient de gagner **15€** !\nFélicitations `" + message.author.name + "` ! Tu avais **0.05%** de chances  d'obtenir ce resultat !")
                elif resultat >= 801 and resultat <= 22000 :
                    await client.send_message(message.channel, "Tiens ? `" + message.author.name + "` vient de gratter un **numéro fétiche** ! Et... Eh ! il vient de gagner **10€** !\nFélicitations `" + message.author.name + "` ! Tu avais **1.46%** de chances  d'obtenir ce resultat ! Tu peux m'inviter au Kebab si tu veux :smirk:")
                elif resultat >= 22001 and resultat <= 54680 :
                    await client.send_message(message.channel, "Tiens ? `" + message.author.name + "` vient de gratter un **numéro fétiche** ! Et... tiens ? Il vient de gagner **4€** !\nFélicitations `" + message.author.name + "` ! Tu avais **3.64%** de chances  d'obtenir ce resultat !")
                elif resultat >= 54681 and resultat <= 157500 :
                    await client.send_message(message.channel, "Tiens ? `" + message.author.name + "` vient de gratter un **numéro fétiche** ! Et... super ! Il vient de gagner **2€** !\nFélicitations `" + message.author.name + "` ! Tu avais **10.5%** de chances  d'obtenir ce resultat !")
                elif resultat >= 157501 and resultat <= 190050 :
                    await client.send_message(message.channel, "Tiens ? `" + message.author.name + "` vient de gratter un **numéro fétiche** ! Et... Ahah ! Il vient de gagner **1€**, il peut rembourser son ticket !\nFélicitations `" + message.author.name + "` ! Tu avais 12.67% de chances  d'obtenir ce resultat !")
                else :
                    await client.send_message(message.channel, "Tiens ? `" + message.author.name + "` vient de gratter un **numéro fétiche** ! Et... Ooooh, Il a **perdu** :( \nDommage pour toi, `"+message.author.name+"` tu avais **71.64%** de chances d'obtenir ce resultat :shrug:")
        except :
            await client.send_message(message.channel, "Oups ! il faut indiquer le nom du ticket à gratter avant ça :3\nFais `/aide fdj` pour mieux comprendre le fonctionnement de la commande !")


    elif message.content == "/ping":
        await client.send_message(message.channel, "**PONG !** :ping_pong:")

    elif message.content == "/info":
        await client.send_message(message.channel,"**Quelques informations sur moi** :3\n\nPour m'inviter sur votre serveur :\nhttps://discordapp.com/oauth2/authorize?client_id=486582772647854101&scope=bot&permissions=8\n\nPour rejoindre le serveur officiel :\nhttps://discord.gg/WjeKDHu\n\nBot developpé intégralement par **P4C0** grâce à l'API **discord.py**.")
        

###################

client.run("NDg2NTgyNzcyNjQ3ODU0MTAx.DnBNKA.DQbLORPpU-LZFOGsPKk4Xwf_Oq4")
