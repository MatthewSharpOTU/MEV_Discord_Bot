import os
import random
import discord
import re
import asyncio
import json
import time
import logging
import threading 
from replit import db
from keep_alive import keep_alive


try:
    import discum
except:
    os.system("pip install git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum")
    import discum

client = discord.Client()

agents = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Fade","Jett", "KAY/O",
          "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye",
          "Sova", "Viper", "Yoru"]

maps = ["Ascent", "Bind", "Breeze", "Fracture", "Haven", "Icebox", "Split", "Pearl"]

emotes = ["<:astra:958420104490663986>","<:breach:958420500839804938>","<:brimstone:958420774736252948>","<:chamber:958421177422983239>","<:cypher:958425821578682378>", "<:fade:993989578455261244>",
"<:jett:958426375168073809>","<:kayo:958426726822727711>","<:killjoy:958427157539983440>","<:neon:958427417528131624>","<:omen:958427990029660230>","<:phoenix:958428146330374164>","<:raze:958428251485782046>","<:reyna:958428346428059648>","<:sage:958428493211902003>","<:skye:958428627517730876>","<:sova:958429598989811812>","<:viper:958429995989086238>","<:yoru:958430128977895504>", "<:atk:960403431837802496>","<:def:960367760574128151>"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('```Hello {}```'.format(message.author.name))
  if message.content.startswith('$emote'):
    await message.channel.send("<:sussy:935624408855363666>")

  if message.content.startswith('$startnew'):
    new_user = False
    for k in db.keys():
      if str(message.author) == k:
        new_user = True
        break
      
    if new_user == True:
      await message.channel.send('```This user has an account associated with MEV Bot```')
    else:
      await message.channel.send('```Welcome to MEV Bot, this is a bot that will allow you to collect different valorant abilities, charms, skins and agents. Since this is your first time you have one free lootbox for an agent and their abilities, 2 charms and a skin. Take part in the casino, complete daily and weekly tasks, random pop questions, and many more to earn more currency to collect them all. If you roll a duplicate use $claim to earn currency. Good luck and enjoy MEV Bot```')
  
  if message.content.startswith('$reset'):
    del db[str(message.author)]
    print(db.keys())

  if message.content.startswith('$randomval'):
    l = len(message.content)
    if l>10:
      if message.content[11] == "c":
        print("Custom Game")
        attside = int(message.content[13])
        defside = int(message.content[15])
        attnum = []
        defnum = []
        emotesatt = []
        emotesdef = []
        response = emotes[19] + "   " + emotes[20] + "\n"
        i = 0
        while i < attside or i < defside:
          num = random.randint(0,18)
          res1 = ""
          res2 = ""
          if i < attside:
            repeat = True
            while repeat:
              if num in attnum:
                num = random.randint(0,18)
              else:
                break
            emotesatt.append(emotes[num])
            attnum.append(num)
            res1 = emotesatt[i] + "   "
          else:
            res1 = "                "
          if i < defside:
            repeat = True
            num = random.randint(0,18)
            while repeat:
              if num in defnum:
               num = random.randint(0,18)
              else: 
               break
            emotesdef.append(emotes[num])
            defnum.append(num)
            res2 = emotesdef[i]
          res3 = "\n"
          joined = [res1,res2,res3]
          row = "".join(joined)
          joined = [response,row]
          response = "".join(joined)
          i = i+1
        num = random.randint(0,7)
        map = "Map: " + maps[num]
        await message.channel.send(response)
        await message.channel.send(map)
        

      elif message.content[11] != "c":
        players = int(message.content[11])
        response = ""
        currentplay = []
        repeat = True
        if players>=2 and players<=5:
          for i in range(players):
            num = random.randint(0,18)
            while repeat:
              if num in currentplay:
                num = random.randint(0,18)
              else:
                break
            res = emotes[num] + "\n"
            joined = [response,res]
            response = "".join(joined)
            currentplay.append(num)
          await message.channel.send(response)
        else:
          print("Error")
      else:
        print("Error")
    else:
      print("Random Agent")
      response = emotes[random.randint(0,18)]
      await message.channel.send(response)

  if message.content.startswith('$randomteam'):
    team1Len = 0
    team2Len = 0
    if len(message.content)>12:
      print('hello')
      names = message.content.split()
      names.pop(0)
      teamOne = []
      teamTwo = []
      res_t1 = "Team 1\n"
      res_t2 = "Team 2\n"
      l = len(names)
      for i in range(l):
        if len(names) == 1:
          num = random.randint(1,10)
          if num%2==0:
            teamOne.append(names[0])
            res1 = "- "+names[0] + "\n"
            joined = [res_t1,res1]
            res_t1 = "".join(joined)
          else:
            teamTwo.append(names[0])
            res2 = "- "+names[0] + "\n"
            joined = [res_t2,res2]
            res_t2 = "".join(joined)
          team1Len=len(teamOne)
          team2Len=len(teamTwo)
          break
        num = random.randint(0,len(names)-1)
        teamOne.append(names[num])
        res1 = "- "+names[num] + "\n"
        joined = [res_t1,res1]
        res_t1 = "".join(joined)
        names.pop(num)
        num = random.randint(0,len(names)-1)
        teamTwo.append(names[num])
        res2 = "- "+names[num] + "\n"
        joined = [res_t2,res2]
        res_t2 = "".join(joined)
        names.pop(num)
        if len(names) == 0:
          team1Len=len(teamOne)
          team2Len=len(teamTwo)
          break
      joined = [res_t1,res_t2]
      response = "\n".join(joined)
      await message.channel.send(response)
      
    else:
      print('Error')
    response = '```Use this command to randomize valorant agents: $randomval c ' + str(team1Len) + "v" + str(team2Len) + "```" 
    await message.channel.send(response)

    
  if message.content.startswith('$embed'):
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.add_field(name="Field1", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    embedVar.set_image(url="https://www.looper.com/img/gallery/valorant-release-date-platforms-trailer-and-gameplay/intro-1591383833.jpg")
    await message.channel.send(embed=embedVar)
  
keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
