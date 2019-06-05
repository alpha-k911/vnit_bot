import discord,os
from tabula import read_pdf
import json
import sys
read_pdf("cse.pdf",area=[])
global str
#import pandas as pd
#df=pd.read_csv('/root/Documents/panda/weatc.csv')
#check
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!\nOptions\n[+]!hello\n[+]!bot'.format(member, guild)
            await guild.system_channel.send(to_send)
            # await guild.system_channel.send('')


    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello Mr. {0.author.mention}'.format(message))
        elif message.content.startswith('!bot'):
            await message.channel.send('How dare you to call me a bot. Hey you {0.author.mention} I\'m not a bot.'.format(message))
        elif message.content.startswith('!cal'):
            import calendar
            '''
            hc = calendar.HTMLCalendar(calendar.THURSDAY)
            str = hc.formatmonth(2019,1)
            await message.channel.send(str)
            '''
            await message.channel.send(calendar.month(2019,5))
            await message.channel.send(os.popen('pyjoke').read())
        elif message.content.startswith("!pun"):
            # import os
            # await message.channel.send('Hello', file=discord.File('a.png'))
            await message.channel.send(os.popen('pyjoke').read())
        elif message.content.startswith('!BT17CSE0'):
            try:
                with open('cse226.template_777.json', 'r') as fp:
                    obj = json.load(fp)
                a = []
                for i in range(len(obj)):
                    p = []
                    p.append(obj[i]["y1"])
                    p.append(obj[i]["x1"])
                    p.append(obj[i]["y2"])
                    p.append(obj[i]["x2"])
                    a.append(p)
                k = int(message.content[9:11]) + 146
                print(k)
                df = read_pdf('cse.pdf',pages=k,area=a,multiple_tables=True,guess=False)
                name = df[6][2][0]
                enroll = df[6][5][0]
                await message.channel.send(name + "\n" + enroll + '\n')
                df = read_pdf('cse.pdf', pages=k, area=a[3], guess=False,pandas_options={'names': ['Code', 'Course', 'Credits', 'Grade']})
                for i in range(len(df)):
                    d = "Code: " + df['Code'][i] + "\n" + "Course: " + df['Course'][i] + '\n' + "Credits: " + str(df['Credits'][i].item()) + "\n" + "Grade: " + df['Grade'][i]
                    await message.channel.send(d+'\n')
                df = read_pdf('cse.pdf', pages=k, area=a[0], guess=False, pandas_options={'header': None})
                cg = df[6][1]
                sg = df[3][1]
                c_cre = df[7][3]
                s_cre = df[3][3]
                s_cre = s_cre[5:]
                c_cre = c_cre[5:]
                print(s_cre+c_cre+sg+cg)
                await message.channel.send("Semester Credits: "+s_cre+"\nTotal Credits"+c_cre)
                await message.channel.send('SGPA: '+sg + '\nCGPA: ' + cg)
                await message.channel.send(os.popen('pyjoke').read())
                
            except:
                await message.channel.send("I'm got bored of Mess food....")
                await message.channel.send(os.popen('pyjoke').read())
                print(sys.exc_info()[0])


        else:
            await message.channel.send('Options\n[+]!hello\n[+]!bot\n[+]!pun\n[+]!cal\n[+]!BT17CSE08** for S19 results')


client = MyClient()
client.run('NTc4ODg4NDI0OTU0NTI3NzY1.XN6LAg.k40GvlZBblXJSGZLT-L6R3DtBVU')
with open('cse226.template_777.json', 'r') as fp:
    obj = json.load(fp)
a=[]
for i in range(len(obj)):
    p=[]
    p.append(obj[i]["y1"])
    p.append(obj[i]["x1"])
    p.append(obj[i]["y2"])
    p.append(obj[i]["x2"])
    a.append(p)
