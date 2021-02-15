import discord
import asyncio
import random
from random import randint , choice
from discord import Activity, ActivityType
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from dotenv import load_dotenv
from tabulate import tabulate
import datetime, pyowm
import speech_recognition as sr
from discord.utils import get
import youtube_dl
import shutil
import traceback2 as traceback
import sqlite3
import validators
import nekos
import json
import sys

import os
from time import sleep
import requests

PREFIX = "."

client = commands.Bot( command_prefix = PREFIX )
client.remove_command( "help" )

initial_extensions = [
"cogs.voice",
"cogs.stats",
"cogs.lvl"
]

for extension in initial_extensions:
    try:
        client.load_extension(extension)
    except Exception as e:
        print(f'Не удалось загрузить расширение {extension}.')
        traceback.print_exc()

@client.event
async def on_ready():
    song_name='TWICE - What is love?'
    activity_type=discord.ActivityType.listening
    print('''
               ░██████╗████████╗░█████╗░██████╗░████████╗  ░██████╗██╗░░██╗██╗███████╗██╗░░░██╗██╗░░██╗██╗
               ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝  ██╔════╝██║░░██║██║╚════██║██║░░░██║██║░██╔╝██║
               ╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░  ╚█████╗░███████║██║░░███╔═╝██║░░░██║█████═╝░██║
               ░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░  ░╚═══██╗██╔══██║██║██╔══╝░░██║░░░██║██╔═██╗░██║
               ██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░  ██████╔╝██║░░██║██║███████╗╚██████╔╝██║░╚██╗██║
               ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝
''')
    print('''
    
            ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ░██████╗░█████╗░██████╗░░█████╗░
            ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ██╔════╝██╔══██╗██╔══██╗██╔══██╗
            ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ╚█████╗░██║░░██║██████╔╝███████║
            ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░╚═══██╗██║░░██║██╔══██╗██╔══██║
            ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ██████╔╝╚█████╔╝██║░░██║██║░░██║
            ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

        ''')
    await client.change_presence( status= discord.Status.online, activity= Activity( name= "за сервером", type=ActivityType.watching))

#NSFW
def is_nsfw():
    async def predicate(ctx):
        return ctx.channel.is_nsfw()
    return commands.check(predicate)

@client.command()
@is_nsfw()
async def neko(ctx):
    emb = discord.Embed( title ="Neko", color = 0x1100ff )
    emb.set_image(url=nekos.img("nsfw_neko_gif"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def yuri(ctx):
    emb = discord.Embed( title = "Yuri", color = 0x1100ff )
    emb.set_image(url=nekos.img("les"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def hentai(ctx):
    emb = discord.Embed( title = "Hentai", color = 0x1100ff )
    emb.set_image(url=nekos.img("Random_hentai_gif"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def cum(ctx):
    emb = discord.Embed( title = "Cum", color = 0x1100ff )
    emb.set_image(url=nekos.img("cum"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def pussy(ctx):
    emb = discord.Embed( title = "Pussy", color = 0x1100ff )
    emb.set_image(url=nekos.img("pwankg"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def feet(ctx):
    emb = discord.Embed( title = "Feet", color = 0x1100ff )
    emb.set_image(url=nekos.img("feetg"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def cuddle(ctx):
    emb = discord.Embed( title = "Cuddle", color = 0x1100ff )
    emb.set_image(url=nekos.img("cuddle"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def solo(ctx):
    emb = discord.Embed( title = "Solo", color = 0x1100ff )
    emb.set_image(url=nekos.img("solog"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def kemo(ctx):
    emb = discord.Embed( title = "Kemo", color = 0x1100ff )
    emb.set_image(url=nekos.img("erokemo"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def kuni(ctx):
    emb = discord.Embed( title = "Kuni", color = 0x1100ff )
    emb.set_image(url=nekos.img("kuni"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def loli(ctx):
    emb = discord.Embed( title = "Loli", color = 0x1100ff )
    emb.set_image(url=nekos.img("smallboobs"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def blowjob(ctx):
    emb = discord.Embed( title = "Blowjob", color = 0x1100ff )
    emb.set_image(url=nekos.img("blowjob"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def anal(ctx):
    emb = discord.Embed( title = "Anal", color = 0x1100ff )
    emb.set_image(url=nekos.img("anal"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def nsfw(ctx):
    emb = discord.Embed( title= "Команды NSFW", color = 0x1100ff )
    emb.add_field( name= "{}neko".format( PREFIX ), value= "Кошки-девочки", inline= True)
    emb.add_field( name= "{}yuri".formatц( PREFIX ), value= "Лезбиянки", inline= True)
    emb.add_field( name= "{}loli".format( PREFIX ), value= "Лоликон", inline= True)
    emb.add_field( name= "{}blowjob".format( PREFIX ), value= "Работает ротиком", inline= True)
    emb.add_field( name= "{}kuni".format( PREFIX ), value= "Лизать киску", inline= True)
    emb.add_field( name= "{}kemo".format( PREFIX ), value= "Няшки", inline= True)
    emb.add_field( name= "{}solo".format( PREFIX ), value= "Соло", inline= True)
    emb.add_field( name= "{}pussy".format( PREFIX ), value= "Киски", inline= True)
    emb.add_field( name= "{}feet".format( PREFIX ), value= "Красивые ношки", inline= True)
    emb.add_field( name= "{}hentai".format( PREFIX ), value= "Хентай", inline= True)
    emb.add_field( name= "{}anal".format( PREFIX ), value= "анал", inline= True)
    emb.add_field( name= "{}cum".format( PREFIX ), value= "Кончают", inline= True)
    emb.set_image( url = "https://danbooru.donmai.us/data/e71dc6de8c5c153e56ee179e5dc5d58f.gif")
    await ctx.send(embed = emb)

#Music
@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    print(f"The bot has connected to {channel}\n")

@client.command(pass_context=True, aliases=['l', 'lea', "d", "disconnect"])
async def leave(ctx):
    channel = ctx.message.author.voice.channel

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()

@client.command(pass_context=True, aliases=['p'])
async def play(ctx, url: str,):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        song_there = os.path.isfile('song.mp3')

    try:
        if song_there:
            os.remove('song.mp3')
            print('[log] Старый файл удалён')

    except PermissionError:
        print('[log] Не удалось удалить страый файл')

    await ctx.send('Пожалуйста ожидайте: 5 - 10 сек')

    voice = get(client.voice_clients, guild = ctx.guild)

    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
        'key' : 'FFmpegExtractAudio',
        'preferredcodec' : 'mp3',
        'preferredquality' : '192'
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('[log] Загружаю музыку')
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'[log] Переменовываю файл: {file}')
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[log] {name}, музыка закончила своё проигрывание'))
    voice.sourse.volume = 0.07

    song_name = name.rsplit('-', 2)
    await ctx.send(f'Сейчас проигрывает музыка: {song[0]}')

@client.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Музыка приостановлена.")


@client.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Музыка продолжается.")

@client.command(pass_context=True, aliases=['n', 'next'])
async def skip(ctx):
    voice = discord.utils.get(client.voice_client, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Проигрывается следующая музыку")
        voice.stop()
        await ctx.send("Проигрывается следующая музыку")
    else:
        await ctx.send('Нет никакой музыки в очереди!')

#Reaction Role
@client.event
async def on_raw_reaction_add(payload):

    if payload.member.client:
        pass

    else:

        with open('reactionrole1.json') as react_file:

            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])

                    await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):

    if payload.member.client:
        pass

    else:

        with open('reactionrole1.json') as react_file:

            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])

                    await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

@client.command()
@commands.has_permissions( administrator = True )
async def reactrole(ctx, emoji, role: discord.Role,*,message):

    gen = discord.Embed(description=message)
    msg = await ctx.send(embed = gen)
    await msg.add_reaction(emoji)

    with open('reactionrole1.json') as json_file:
        data = json.load(json_file)

        new_react_role = {
            'role_name':role.name,
            'role_id':role.id,
            'emoji':emoji,
            'message_id':msg.id
        }

        data.append(new_react_role)


    with open('reactionrole1.json', 'w') as j:
        json.dump(data,j,indent=4)

@client.command()
async def virus(ctx, virus=None, *, user: discord.Member = None):
    virus = virus or 'discord'
    user = user or ctx.author
    with open('data/virus.txt') as f:
        animation = f.read().splitlines()
    base = await ctx.send(animation[0])
    for line in animation[1:]:
        await base.edit(content=line.format(virus=virus, user=user))
        await asyncio.sleep(random.randint(1, 4))

#EmojiRole
@client.event
async def EmojiRole(ctx):
    emb = discord.Embed( title= "Ваш пол", color=0x1100ff)
    emb.add_field( name = payload.emoji.name, value= "Мужской", inline= True )
    emb.add_field( name = payload.emoji.name, value= "Женский", inline= True )
    await ctx.send(embed = emb)

#Statistic

#Private rooms v2

#Autorole join
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name= 'Участники' )
    await member.add.roles(role)

@client.event
async def on_command_error( ctx, error ):
    pass

#InfoMember
@client.command( pass_context = True )
async def info( ctx, member:discord.Member):
    emb= discord.Embed(title = "Информация о пользователе", color=0x1100ff)
    emb.add_field( name = "Когда присоединился:", value = member.joined_at, inline=False)
    emb.add_field( name = "Имя:", value = member.display_name, inline=False)
    emb.add_field( name = "Айди:", value= member.id, inline=False)
    emb.add_field( name = "Аккаунт был создан:", value= member.created_at.strftime("%a, %d %B %Y, %H:%M:%S UTC"), inline=False)
    emb.set_thumbnail( url = member.avatar_url)
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    emb.set_author( name = ctx.message.author, url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

#Filter
@client.event
async def on_message( message ):
    await client.process_commands( message )

    bad_words = [ "нахуй", "бунт", "лох", "пидр", "долбаеб", "пидар", "пидарас", "пидор", "пидорас" ]
    msg = message.content.lower()

    if msg in bad_words:
        await message.delete()
        await message.author.send( f"{ message.author.mention }, Братик Бяка не матюкайся(")


#Clear channel
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear( ctx, amount : int ):
    await ctx.channel.purge(limit = amount)
    channel = ctx.message.channel
    message = {}

#Mute
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def mute(ctx, member:discord.Member ,time:int, reason = None):
    channel = client.get_channel(789716555449368606)
    muterole = discord.utils.get(ctx.guild.roles,id=789710455693246476)
    emb = discord.Embed( title= "Mute", color=0x1100ff )
    emb.add_field( name = "Администратор", value = ctx.message.author.mention, inline=False )
    emb.add_field( name = "Нарушитель", value = member.mention, inline=False )
    emb.add_field( name = "Причина", value = reason, inline=False )
    emb.add_field( name = "Время", value = time, inline=False)
    emb.set_thumbnail(url = member.avatar_url)
    await member.add_roles(muterole)
    await channel.send(embed = emb)
    await asyncio.sleep(time)
    await member.remove_roles(muterole)

#Unmute
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def unmute(ctx, member:discord.Member):
    channel = client.get_channel(789716555449368606)
    muterole = discord.utils.get(ctx.guild.roles,id=789710455693246476)
    emb = discord.Embed( title= "Unmute", color=0x1100ff )
    emb.add_field( name = "Администратор", value = ctx.message.author.mention, inline=False )
    emb.add_field( name = "Нарушитель", value = member.mention, inline=False )
    emb.set_thumbnail(url = member.avatar_url)
    await channel.send(embed = emb)
    await member.remove_roles(muterole)

#Kick
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def kick( ctx, member: discord.Member, *, reason = None ):
    channel = client.get_channel(789716555449368606)
    emb = discord.Embed( title= "Kick", color=0x1100ff )
    emb.add_field( name ="Администратор", value= ctx.message.author.mention, inline= False )
    emb.add_field( name = "Нарушитель", value = member.mention, inline= False)
    emb.add_field( name = "Причина", value= reason, inline=False)
    emb.set_thumbnail( url = member.avatar_url)
    await member.kick()
    await channel.send(embed = emb)

#Ban
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def ban( ctx, member: discord.Member,time:int, reason = None ):
    channel = client.get_channel(789716555449368606)
    emb = discord.Embed( title= "Ban", color=0x1100ff )
    emb.add_field( name = "Администратор", value = ctx.message.author.mention, inline= False )
    emb.add_field( name = "Нарушитель", value = member.mention, inline= False)
    emb.add_field( name = "Причина", value = reason, inline= False)
    emb.add_field( name = "Время", value= time, inline= False)
    emb.set_thumbnail( url = member.avatar_url)
    await member.ban()
    await channel.send(embed = emb)

#Help client
@client.command( pass_context = True )
async def helpbot( ctx ):
    emb = discord.Embed( title = "Команды к ботам", color=0x1100ff )

    emb.add_field( name = "{}Rythm".format( PREFIX ), value = "Основные команды Rythm", )
    await ctx.send( embed=emb )

#Rythm
@client.command( pass_context = True )
async def Rythm( ctx ):
    emb=discord.Embed( title = "Список команды Rythm", color=0x1100ff )
    
    emb.add_field( name = "?play (ссылка)".format( PREFIX ), value="включить музыку (надо находится в голосовом канале)", inline=False )
    emb.add_field( name = "?disconnect".format( PREFIX ), value="убрать бота с голосового канала", inline=False )
    emb.add_field( name = "?skip".format( PREFIX ), value="пропустить музыку", inline=True )
    emb.set_thumbnail( url = "https://tbib.org/images/7431/e9764a47ea99c9b457fdb856061a2155648c76d8.jpg?8183652" )
    await ctx.send( embed=emb )

@clear.error
async def clear_error( ctx, error ):

    if isinstance( error, commands.MissingPermissions ):
        await message.author.send( f"{ message.author.mention }, у вас не достаточно прав!" )

# Get token
def setup(client):
    client.add_cog(level(client), stats(client), voice(client))

#token = open( "token.txt", "r").readline()

client.run(os.getenv('BOT_TOKEN'))
