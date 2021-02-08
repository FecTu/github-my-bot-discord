import discord
import asyncio
import random
from random import randint , choice
from discord import Activity, ActivityType
from discord.ext import commands
from discord.ext.commands import Bot
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

bot = commands.Bot( command_prefix = PREFIX )
bot.remove_command( "help" )

initial_extensions = [
"",
"cogs.stats",
"cogs.lvl"
]

for extension in initial_extensions:
    try:
        bot.load_extension(extension)
    except Exception as e:
        print(f'Не удалось загрузить расширение {extension}.')
        traceback.print_exc()

@bot.event
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
    await bot.change_presence( status= discord.Status.online, activity= Activity( name= "за сервером", type=ActivityType.watching))

#NSFW
def is_nsfw():
    async def predicate(ctx):
        return ctx.channel.is_nsfw()
    return commands.check(predicate)

@bot.command()
@is_nsfw()
async def neko(ctx):
    emb = discord.Embed( title ="Neko", color = 0x1100ff )
    emb.set_image(url=nekos.img("nsfw_neko_gif"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def yuri(ctx):
    emb = discord.Embed( title = "Yuri", color = 0x1100ff )
    emb.set_image(url=nekos.img("les"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def hentai(ctx):
    emb = discord.Embed( title = "Hentai", color = 0x1100ff )
    emb.set_image(url=nekos.img("Random_hentai_gif"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def cum(ctx):
    emb = discord.Embed( title = "Cum", color = 0x1100ff )
    emb.set_image(url=nekos.img("cum"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def pussy(ctx):
    emb = discord.Embed( title = "Pussy", color = 0x1100ff )
    emb.set_image(url=nekos.img("pwankg"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def feet(ctx):
    emb = discord.Embed( title = "Feet", color = 0x1100ff )
    emb.set_image(url=nekos.img("feetg"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def cuddle(ctx):
    emb = discord.Embed( title = "Cuddle", color = 0x1100ff )
    emb.set_image(url=nekos.img("cuddle"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def solo(ctx):
    emb = discord.Embed( title = "Solo", color = 0x1100ff )
    emb.set_image(url=nekos.img("solog"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def kemo(ctx):
    emb = discord.Embed( title = "Kemo", color = 0x1100ff )
    emb.set_image(url=nekos.img("erokemo"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def kuni(ctx):
    emb = discord.Embed( title = "Kuni", color = 0x1100ff )
    emb.set_image(url=nekos.img("kuni"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def loli(ctx):
    emb = discord.Embed( title = "Loli", color = 0x1100ff )
    emb.set_image(url=nekos.img("smallboobs"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def blowjob(ctx):
    emb = discord.Embed( title = "Blowjob", color = 0x1100ff )
    emb.set_image(url=nekos.img("blowjob"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def anal(ctx):
    emb = discord.Embed( title = "Anal", color = 0x1100ff )
    emb.set_image(url=nekos.img("anal"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@is_nsfw()
async def nsfw(ctx):
    emb = discord.Embed( title= "Команды NSFW", color = 0x1100ff )
    emb.add_field( name= "{}neko".format( PREFIX ), value= "Кошки-девочки", inline= True)
    emb.add_field( name= "{}yuri".format( PREFIX ), value= "Лезбиянки", inline= True)
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
@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    print(f"The bot has connected to {channel}\n")

@bot.command(pass_context=True, aliases=['l', 'lea', "d", "disconnect"])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_bots, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"Бот покинул {channel}")
    else:
        print("Бот покинул голосовой канал, ему так ")

@bot.command()
async def play(ctx, url: str, aliases=["p"]):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild = ctx.guild)

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

    voice = get(bot.voice_clients, guild = ctx.guild)

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

@bot.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Music paused")
    else:
        print("Music not playing failed pause")
        await ctx.send("Music not playing failed pause")

@bot.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Resumed music")
    else:
        print("Music is not paused")
        await ctx.send("Music is not paused")

@bot.command(pass_context=True, aliases=['n', 'nex'])
async def skip(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Playing Next Song")
        voice.stop()
        await ctx.send("Next Song")
    else:
        print("No music playing")
        await ctx.send("No music playing failed")

#EmojiRole
@bot.event
async def EmojiRole(ctx):
    emb = discord.Embed( title= "Ваш пол", color=0x1100ff)
    emb.add_field( name = payload.emoji.name, value= "Мужской", inline= True )
    emb.add_field( name = payload.emoji.name, value= "Женский", inline= True )
    await ctx.send(embed = emb)

#Statistic

#Private rooms v2
#@bot.group()
#async def voice(ctx):
#   print(f'voice activate')

@bot.command()
@commands.has_permissions(administrator=True)
async def rooms(ctx):
    rooms_cat = await ctx.guild.create_category_channel(name= 'Приватные комнаты')
    rooms_voi = await ctx.guild.create_voice_channel(name= 'Создать комнату', category= rooms_cat)
    print (f'Приватные комнаты были созданы')

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel.id == 808293037519142923:
        for guild in bot.guilds:
            maincategory = get(guild.categories, id = 808293036832063498)
            channel2 = await guild.create_voice_channel( name=f'Канал {member.display_name}', category = maincategory )
            await channel2.set_permissions(member, connect = True, mute_members = True, move_members = True, manage_channels = True)
            await channel2.edit(user_limit = 2)
            await member.move_to(channel2)
            def check(x,y,z):
                return len(channel2.members) == 0
            await bot.wait_for( 'voice_state_update', check=check )
            await channel2.delete()

#Autorole join
@bot.event
async def on_member_join(member):
    role = discord.utils.get(ctx.member.guild.roles, name= Участники )
    await member.add.roles(role)

@bot.event
async def on_command_error( ctx, error ):
    pass

#InfoMember
@bot.command( pass_context = True )
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
@bot.event
async def on_message( message ):
    await bot.process_commands( message )

    bad_words = [ "нахуй", "бунт", "лох", "пидр", "долбаеб", "пидар", "пидарас", "пидор", "пидорас" ]
    msg = message.content.lower()

    if msg in bad_words:
        await message.delete()
        await message.author.send( f"{ message.author.mention }, Братик Бяка не матюкайся(")


#Clear channel
@bot.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear( ctx, amount : int ):
    await ctx.channel.purge(limit = amount)
    channel = ctx.message.channel
    message = {}

#Mute
@bot.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def mute(ctx, member:discord.Member ,time:int, reason = None):
    channel = bot.get_channel(789716555449368606)
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
@bot.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def unmute(ctx, member:discord.Member):
    channel = bot.get_channel(789716555449368606)
    muterole = discord.utils.get(ctx.guild.roles,id=789710455693246476)
    emb = discord.Embed( title= "Unmute", color=0x1100ff )
    emb.add_field( name = "Администратор", value = ctx.message.author.mention, inline=False )
    emb.add_field( name = "Нарушитель", value = member.mention, inline=False )
    emb.set_thumbnail(url = member.avatar_url)
    await channel.send(embed = emb)
    await member.remove_roles(muterole)

#Kick
@bot.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def kick( ctx, member: discord.Member, *, reason = None ):
    channel = bot.get_channel(789716555449368606)
    emb = discord.Embed( title= "Kick", color=0x1100ff )
    emb.add_field( name ="Администратор", value= ctx.message.author.mention, inline= False )
    emb.add_field( name = "Нарушитель", value = member.mention, inline= False)
    emb.add_field( name = "Причина", value= reason, inline=False)
    emb.set_thumbnail( url = member.avatar_url)
    await member.kick()
    await channel.send(embed = emb)

#Ban
@bot.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def ban( ctx, member: discord.Member,time:int, reason = None ):
    channel = bot.get_channel(789716555449368606)
    emb = discord.Embed( title= "Ban", color=0x1100ff )
    emb.add_field( name = "Администратор", value = ctx.message.author.mention, inline= False )
    emb.add_field( name = "Нарушитель", value = member.mention, inline= False)
    emb.add_field( name = "Причина", value = reason, inline= False)
    emb.add_field( name = "Время", value= time, inline= False)
    emb.set_thumbnail( url = member.avatar_url)
    await member.ban()
    await channel.send(embed = emb)

#Help bot
@bot.command( pass_context = True )
async def helpbot( ctx ):
    emb = discord.Embed( title = "Команды к ботам", color=0x1100ff )

    emb.add_field( name = "{}Rythm".format( PREFIX ), value = "Основные команды Rythm", )
    await ctx.send( embed=emb )

#Rythm
@bot.command( pass_context = True )
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
def setup(bot):
    bot.add_cog(voice(bot))

#token = open( "token.txt", "r").readline()

bot.run(os.getenv('BOT_TOKEN'))
