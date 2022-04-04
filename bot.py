
# -*- coding: utf-8 -*-

from asyncio.tasks import sleep
from logging import debug
from typing import Text
import discord
from discord import message
import discord
from discord.enums import Status
from discord.ext import commands
from discord.ext import tasks
import requests, asyncio, discord, json, os, shutil, sys, time, aiohttp
from discord_webhook import DiscordWebhook, DiscordEmbed
from collections import OrderedDict
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import asyncio
import os.path
import setting
import datetime
import asyncio
import discord
from discord import message
from discord.errors import InvalidArgument
import requests
import os
import json
import setting
import datetime
from datetime import timedelta
from discord_webhook import DiscordWebhook, DiscordEmbed
import discord
from discord.client import Client
from discord.ext import commands
import json
import datetime
from datetime import timedelta
from discord.ext import commands
from discord_components import DiscordComponents, Button, Select, SelectOption
from datetime import timedelta
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption, component
from discord_components.interaction import Interaction
import os
import asyncio
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
from discord.ext import commands
import discord
from discord.client import Client
from discord.ext import commands
import json
import datetime
from datetime import timedelta
from datetime import timedelta
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption, component
from discord_components.interaction import Interaction
import os
import asyncio
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests

token = setting.token

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

sta = setting.sangma


def eb(embedtype, embedtitle, description):
    if (embedtype == "error"):
        return discord.Embed(color=0x010101, title=":no_entry: " + embedtitle, description=description)
    if (embedtype == "success"):
        return discord.Embed(color=0x010101, title=":white_check_mark: " + embedtitle, description=description)
    if (embedtype == "warning"):
        return discord.Embed(color=0x010101, title=":warning: " + embedtitle, description=description)
    if (embedtype == "loading"):
        return discord.Embed(color=0x010101, title=":gear: " + embedtitle, description=description)
    if (embedtype == "primary"):
        return discord.Embed(color=0x010101, title=embedtitle, description=description)



@client.event
async def on_connect():  
    print(f"{client.user}\nInvite Link: https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot")
    print("================================================================")
    while True:
        game = discord.Game(sta)
        await client.change_presence(status=discord.Status.online, activity=game)


    

@client.event
async def on_raw_reaction_add(payload):
    if not os.path.isdir(f"./db/{payload.member.guild.id}"):
        return

    message.channel ,message.author= payload.member,payload.member

    if payload.member.bot == 1: #봇이면 패스
        return None  
    
    with open(f"./db/{payload.member.guild.id}/mid/{payload.member.guild.id}.txt",'r', encoding='utf-8') as f:
        qw=f.read()



    if str(payload.emoji) == "1️⃣" and str(qw) == str(payload.message_id):   
        c = client.get_channel(int(payload.channel_id))
        m = await c.fetch_message(int(payload.message_id))
        u = client.get_user(int(payload.member.id))
        e = payload.emoji
        await m.remove_reaction(e, u)

        if os.path.isfile(f"./db/{payload.member.guild.id}/role/{payload.member.guild.id}.txt"):
            with open(f"./db/{payload.member.guild.id}/role/{payload.member.guild.id}.txt",'r') as f:
                qq=f.read()
            embed = discord.Embed(description= qq, color=0x82ffc9)
            embed.set_author(name='자동 배너신청', icon_url=f'{payload.member.avatar_url}')
            embed.set_footer(text=f"{payload.member.guild.name} 의 배너조건")
            msg = await payload.member.send(embed=embed)
            return
        else:
            embed = discord.Embed(description= "이 서버에는 배너조건이 없습니다", color=discord.Colour.red())
            embed.set_author(name='자동 배너신청', icon_url=f'{payload.member.avatar_url}')
            embed.set_footer(text=f"{payload.member.guild.name} 의 배너조건")
            msg = await payload.member.send(embed=embed)
            return
    
    if str(payload.emoji) == "2️⃣" and str(qw) == str(payload.message_id):   
        c = client.get_channel(int(payload.channel_id))
        m = await c.fetch_message(int(payload.message_id))
        u = client.get_user(int(payload.member.id))
        e = payload.emoji
        await m.remove_reaction(e, u)
        
        await asyncio.sleep(1)
        try:
            await payload.member.send(embed=eb("primary", "배너 자동신청", "개설할 배너의 이름을 60초 안에 입력주세요").set_footer(text=payload.member.guild.name))
        except:
            return None

        def check(msg):
            return (isinstance(msg.channel, discord.channel.DMChannel) and (payload.member.id == payload.member.id)) and len(msg.content) > 1
        try:
            nacon = await client.wait_for("message", timeout=60, check=check)
        except asyncio.TimeoutError:
            try:
                await payload.member.send(embed=eb("error", "배너신청 실패", "시간 초과되었습니다."))
            except:
                pass
            return None
        if nacon.content == None:
            await payload.member.send(embed=eb("error","error","오류가 발생했습니다 처음부터 다시 시작해주세요."))
            return None
        with open(f"./db/{payload.member.guild.id}/caid/{payload.member.guild.id}.txt") as f:
            caid=f.read()
            
        cn = await payload.member.guild.create_text_channel(name='🎄ㅣ' + str(nacon.content), category=payload.member.guild.get_channel(int(caid)))
        await asyncio.sleep(1)
        ######################
        await payload.member.send(f"<#{cn}> 채널이 생성되었습니다.")
        await cn.send(payload.member.mention + "님이 생성하신 배너입니다")
        ######################
        try:
            await payload.member.send(embed=eb("primary", "배너 자동신청", f"배너를 만들 서버의 영구 초대링크를 60초 안에 입력해주세요").set_footer(text=payload.member.guild.name))
        except:
            return None

        def check(msg):
            return (isinstance(msg.channel, discord.channel.DMChannel) and (payload.member.id == payload.member.id)) and len(msg.content) > 1
        try:
            incon = await client.wait_for("message", timeout=60, check=check)
        except asyncio.TimeoutError:
            try:
                await payload.member.send(embed=eb("error", "배너신청 실패", "시간 초과되었습니다."))
                await cn.delete()
            except:
                pass
            return None
#####################################
        with open(f"./db/{payload.member.guild.id}/adname/{payload.member.guild.id}.txt") as f:
            we=f.read()
        await asyncio.sleep(1)
        try:
            await payload.member.send(embed=eb("primary", "배너 자동신청", f"자신의 서버에서 `{we}` 라는 이름의 채널을 만들고 웹훅을 입력해주세요(제한시간 5분)").set_footer(text=payload.member.guild.name))
        except:
            return None

        def check(msg):
            return (isinstance(msg.channel, discord.channel.DMChannel) and (payload.member.id == payload.member.id)) and len(msg.content) > 1
        try:
            webcon = await client.wait_for("message", timeout=300, check=check)
        except asyncio.TimeoutError:
            try:
                await payload.member.send(embed=eb("error", "배너신청 실패", "시간 초과되었습니다."))
                await cn.delete()                
            except:
                pass
            return None
        hook=webcon.content
        if "api/webhooks" in hook:
            hdr = {'User-Agent': 'Mozilla/5.0'}
          
            json = requests.get(hook, headers=hdr).json()
            try:
                temp = json.get("token")
            except:
                await payload.member.send(embed=eb("error","error","잘못된 웹훅입니다 . 처음부터 다시 시작해주세요"))
                await cn.delete()   
                return
    
            if temp is None:
                await payload.member.send(embed=eb("error","error","잘못된 웹훅입니다 . 처음부터 다시 시작해주세요"))
                await cn.delete()   
                return
        if not "api/webhooks" in hook:
            await payload.member.send(embed=eb("error","error","잘못된 웹훅입니다 . 처음부터 다시 시작해주세요"))
            await cn.delete()   
            return


        web = await cn.create_webhook(name=payload.member, reason='banner')

        embed = discord.Embed(description=f"{web.url}", color=0x82ffc9)
        embed.set_author(name=f'웹훅 생성이 완료되었습니다.', icon_url=f'{payload.member.avatar_url}')

        await payload.member.send(f"{web.url}",embed=embed)
        with open(f"./db/{payload.member.guild.id}/result/{payload.member.guild.id}.txt","r") as fd:
            re=fd.read()
        now = datetime.datetime.now()
        eqeq=discord.Embed(title=f"{payload.member} 님이 배너를 개설하였습니다",description=f"개설 유저: {payload.member.mention} ({payload.member})({payload.member.id})\n개설한 배너: <#{nacon.content}> ({nacon.content})\n서버주소: {incon.content}\n받은 웹훅: {webcon.content}\n이 서버에서 개설된 웹훅: {web.url}",color=discord.Colour.green())
        eqeq.set_footer(text=f"{now.strftime('%Y-%m-%d %H:%M:%S')}")
        
        await client.get_channel(int(re)).send(webcon.content,embed=eqeq)
        
        





@client.event
async def on_message(message):
    if message.content == "!등록":
        if not os.path.isdir(f"./db/{message.author.guild.id}"):
            os.mkdir(f"./db/{message.author.guild.id}")
            os.mkdir(f"./db/{message.author.guild.id}/mid")
            os.mkdir(f"./db/{message.author.guild.id}/role")
            os.mkdir(f"./db/{message.author.guild.id}/caid")
            os.mkdir(f"./db/{message.author.guild.id}/adname")          
            os.mkdir(f"./db/{message.author.guild.id}/result")     
            embed = discord.Embed(description="", color=0x010101)
            embed.set_author(name='서버가 성공적으로 등록되었습니다.', icon_url=f'{message.author.avatar_url}')
            msg = await message.channel.send(embed=embed)
            return
        else:
            embed = discord.Embed(description="이미 서버가 등록되어 있습니다.", color=0x010101)
            embed.set_author(name=f'error', icon_url=f'{message.author.avatar_url}')
            msg = await message.channel.send(embed=embed)
            return


    if message.content == "!카테고리아이디":
        await message.channel.send(message.channel.category.id)

    if message.content == "!명령어":
        if not os.path.isdir(f"./db/{message.author.guild.id}"):
            return
        if not message.author.guild_permissions.administrator:
            return
        embed = discord.Embed(description=f"!결과채널 : 배너를 개설한 후 정보를 출력하는 채널을 해당채널에 지정합니다\n!카테고리 (카테고리 id) : 배너채널이 개설되는 카테고리를 정합니다\n!홍보이름 (이름) : 배너를 개설할떄 상대의 서버에서 만들 채널의 이름을 정한다\n!배너조건 : 이모지 1번을 눌렀을때 나올 배너조건을 정한다\n!카테고리아이디 : 해당 채널의 카테고리의 아이디를 알려줍니다", color=0x010101)
        embed.set_author(name=f'', icon_url=f'{message.author.avatar_url}')
        msg = await message.channel.send(embed=embed)
        return

    if message.content == "!이모지배너":
        if message.author.id == 805584977198579722 or message.author.id == 791605764468637727:
            embed = discord.Embed(description='1️⃣-배너조건\n2️⃣-배너신청', color=0x010101)
            embed.set_author(name='자동 배너신청', icon_url=f'{message.author.avatar_url}')
            embed.set_footer(text="모든 작업은 DM 에서 처리됩니다")
            msg = await message.channel.send(embed=embed)
            await msg.add_reaction('1️⃣')
            await msg.add_reaction('2️⃣')
            with open(f"./db/{message.author.guild.id}/mid/{message.guild.id}.txt",'w', encoding='utf-8') as aa:
                aa.write(str(msg.id))
            await message.channel.set_permissions(message.channel.guild.default_role, add_reactions=False)    
            return      
        else:
            return 

    if message.content.startswith("!결과채널"):
        if not os.path.isdir(f"./db/{message.author.guild.id}"):
            return
        if not message.author.guild_permissions.administrator:
            return
        ch=message.channel.id
        with open(f"./db/{message.author.guild.id}/result/{message.author.guild.id}.txt","w") as f:
            f.write(f"{ch}")
        embed = discord.Embed(description=f'<#{message.channel.id}> 에 배너신청의 결과가 출력됩니다', color=0x010101)
        embed.set_author(name='자동 배너신청', icon_url=f'{message.author.avatar_url}')
        msg = await message.channel.send(embed=embed)
        

    if message.content.startswith("!카테고리 "):
        if not os.path.isdir(f"./db/{message.author.guild.id}"):
            return
        if not message.author.guild_permissions.administrator:
            return
        con=message.content[6:]
        with open(f"./db/{message.author.guild.id}/caid/{message.author.guild.id}.txt","w") as f:
            f.write(f"{con}")
        await message.channel.send(f"이제부터 <#{con}> ({con}) 에 배너채널이 생성됩니다")
        return
        
        
    
    if message.content.startswith("!배너명 "):
        if not os.path.isdir(f"./db/{message.author.guild.id}"):
            return
        if not message.author.guild_permissions.administrator:
            return
        con=message.content[6:]
        with open(f"./db/{message.author.guild.id}/adname/{message.author.guild.id}.txt","w") as f:
            f.write(f"{con}")
        await message.channel.send(f"배너를 만들때 `{message.author.guild.name}` 의 배너채널 이름으로 `{con}` 이(가) 설정되였습니다")
        return

    if message.content.startswith("!배너조건 "):
        if not os.path.isdir(f"./db/{message.author.guild.id}"):
            return
        if not message.author.guild_permissions.administrator:
            return
        con = message.content[6:]
        with open(f"./db/{message.author.guild.id}/role/{message.author.guild.id}.txt",'w') as f:
            f.write(str(con))
        embed = discord.Embed(description=str(con), color=0x010101)
        embed.set_author(name=f'{message.author.guild.name} 의 배너조건이 설정되었습니다', icon_url=f'{message.author.avatar_url}')
        msg = await message.channel.send(embed=embed)
        return


client.run(token)
