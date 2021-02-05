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
bad_words = [ "нахуй", "бунт", "лох", "пидр", "долбаеб", "пидар", "пидарас", "пидор", "пидорас" ]

bot = commands.Bot( command_prefix = PREFIX )
bot.remove_command( "help" )

initial_extensions = ["cogs.voice"]

if __name__ == '__main__':
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
    print("""
               ░██████╗████████╗░█████╗░██████╗░████████╗  ░██████╗██╗░░██╗██╗███████╗██╗░░░██╗██╗░░██╗██╗
               ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝  ██╔════╝██║░░██║██║╚════██║██║░░░██║██║░██╔╝██║
               ╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░  ╚█████╗░███████║██║░░███╔═╝██║░░░██║█████═╝░██║
               ░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░  ░╚═══██╗██╔══██║██║██╔══╝░░██║░░░██║██╔═██╗░██║
               ██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░  ██████╔╝██║░░██║██║███████╗╚██████╔╝██║░╚██╗██║
               ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝
""")
    print("""
    
            ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ░██████╗░█████╗░██████╗░░█████╗░
            ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ██╔════╝██╔══██╗██╔══██╗██╔══██╗
            ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ╚█████╗░██║░░██║██████╔╝███████║
            ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░╚═══██╗██║░░██║██╔══██╗██╔══██║
            ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ██████╔╝╚█████╔╝██║░░██║██║░░██║
            ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

        """)
    await bot.change_presence( status= discord.Status.online, activity= Activity( name= "за Team Inlors", type=ActivityType.watching))

#Rank
@bot.event
async def on_message(message):
    with open("lvl.json", "r") as f:
        users = json.load(f)
    await update_data(users,message.author)
    await add_exp(users,message.author),0.1
    await add_lvl(users,message.author)
    with open("lvl.json", "w") as f:
        json.dump(users,f)
    async def update_data(users,user):
        if not user in users:
            users[user] = {}
            users[user]["exp"] = 0
            users[user]["lvl"] = 1
    async def add_exp(users, user, exp):
        users[user]["exp"] += exp
    async def add_lvl(users,user):
        exp = users[user]["exp"]
        lvl = users[user]["lvl"]
        if exp > lvl:
            await message.channel.send(f"{message.author.mention} повысил свой уровень!")
            users[user]["exp"] = 0
            users[user]["lvl"] = lvl + 1

@bot.command( pass_context=True )
async def rank(ctx, user : discord.Member=None):
    if user is None:
        user = message.author.id
    with open('lvl.json', 'r') as f:
        users = json.load(f)
        lvl = users[user]['lvl']
        exp = users[user]['exp']
        rank = discord.Embed(name="Rank", colour = 0x1100ff)
        rank.add_field(name="Ваш Уровень:", value="{}".format(lvl))
        rank.add_field(name="Общее количество очков опыта:", value="{}".format(exp), inline=True)
        rank.set_footer(text="Спасибо за то, что вы являетесь частью сообщества!")
        rank.set_thumbnail(url=user.avatar_url)
        await ctx.send( embed=rank )

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
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_bots, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"Bot подключился к голосовому каналу {channel}\n")
        await ctx.send(f"Присоединился {channel}")

@bot.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_bots, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"Бот покинул {channel}")
        await ctx.send(f"Покинул {channel}")
    else:
        print("Bot покинул голосовой канал, ему так ")
        await ctx.send("Покинул голосовой канал")

@bot.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("Getting everything ready now")

    voice = get(bot.voice_bots, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Проигрывается: {nname[0]}")
    print("playing\n")

#EmojiRole
@bot.event
async def EmojiRole(ctx):
    emb = discord.Embed( title= "Ваш пол", color=0x1100ff)
    emb.add_field( name = payload.emoji.name, value= "Мужской", inline= True )
    emb.add_field( name = payload.emoji.name, value= "Женский", inline= True )
    await ctx.send(embed = emb)

#Private rooms v2
class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.Cog.listener()
async def on_voice_state_update(self, member, before, after):
    conn = sqlite3.connect("voice.db")
    c = conn.cursor()
    guildID = member.guild.id
    c.execute("SELECT voiceChannelID FROM guild WHERE guildID = ?", (guildID,))
    voice=c.fetchone()
    if voice is None:
        pass
    else:
        voiceID = voice[0]
        try:
            if after.channel.id == voiceID:
                c.execute("SELECT * FROM voiceChannel WHERE userID = ?", (member.id,))
                cooldown=c.fetchone()
                if cooldown is None:
                    pass
                else:
                    await member.send("Создание каналов слишком быстро вы были поставлены на 15-секундный заморожены!")
                    await asyncio.sleep(15)
                c.execute("SELECT voiceCategoryID FROM guild WHERE guildID = ?", (guildID,))
                voice=c.fetchone()
                c.execute("SELECT channelName, channelLimit FROM userSettings WHERE userID = ?", (member.id,))
                setting=c.fetchone()
                c.execute("SELECT channelLimit FROM guildSettings WHERE guildID = ?", (guildID,))
                guildSetting=c.fetchone()
                if setting is None:
                    name = f"{member.name}'s channel"
                    if guildSetting is None:
                        limit = 0
                    else:
                        limit = guildSetting[0]
                else:
                    if guildSetting is None:
                        name = setting[0]
                        limit = setting[1]
                    elif guildSetting is not None and setting[1] == 0:
                        name = setting[0]
                        limit = guildSetting[0]
                    else:
                        name = setting[0]
                        limit = setting[1]
                categoryID = voice[0]
                id = member.id
                category = self.bot.get.channel(categoryID)
                channel2 = await member.guild.create_voice_channel(name,category=category)
                channelID = channel2.id
                await member.move_to(channel2)
                await channel2.set_permissions(self.bot.user, connect = True, mute_members = True, move_members = True, manage_channels = True)
                await channel2.edit(name= name, user_limit = limit)
                cc.execute("INSERT INTO voiceChannel VALUES (?, ?)", (id,channelID))
                conn.commit()
                def check(a,b,c):
                    return len(channel2.member) == 0
                await self.bot.wait_for("voice_state_update", check=check)
                await channel2.delete()
                await asyncio.sleep(3)
                c.execute('DELETE FROM voiceChannel WHERE userID=?', (id,))
        except:
            pass
    conn.commit()
    conn.close()


@commands.group()
async def voice(self, ctx):
        pass

#Code
@voice.command()
async def setup(self, ctx):
    conn = sqlite3.connect("voice.db")
    c = conn.cursor()
    guildID = ctx.guild.id
    id = ctx.author.id
    if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 338651606637608960:
        def check(m):
            return m.author.id == ctx.author.id
        try:
            category = await self.bot.await_for("message", check=check, timeout = 60.0)
        except asyncio.TimeoutError:
            await ctx.channel.send("Слишком долго не отвечал!")
        else:
            new_cat = await ctx.guild.create_category_channel(category.content)
            await ctx.channel.send("**Напишите название канала!**")
            try:
                channel = await self.bot.wait_for("message", check=check, timeout= 60.0)
            except asyncio.TimeoutError:
                await ctx.channel.send("Слишком долго не отвечал!")
            else:
                try:
                    channel = await ctx.guild.create_voice_channel(channel.content, category=new_cat)
                    c.execute("SELECT * FROM guild WHERE guildID = ? AND ownerID=?", (guildID, id))
                    voice=c.fetchone()
                    if voice is None:
                        c.execute ("INSERT INTO guild VALUES (?, ?, ?, ?)",(guildID,id,channel.id,new_cat.id))
                    else:
                        c.execute ("UPDATE guild SET guildID = ?, ownerID = ?, voiceChannelID = ?, voiceCategoryID = ? WHERE guildID = ?",(guildID,id,channel.id,new_cat.id, guildID))
                    await ctx.channel.send("**Вы все настроили и готово к работе!")
                except:
                    await ctx.channel.send("Вы неправильно вписали имена..\nИспользуйте `.voice setup` снова!")
    else:
        await ctx.channel.send(f"{ctx.author.mention} только владелец сервера может установить бота!")
    conn.commit()
    conn.close()

@voice.command()
async def lock(self, ctx):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    id = ctx.author.id
    c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
    voice=c.fetchone()
    if voice is None:
        await ctx.channel.send(f"{ctx.author.mention} Вы не владелец голосового чата.")
    else:
        channelID = voice[0]
        role = discord.utils.get(ctx.guild.roles, name='@everyone')
        channel = self.bot.get_channel(channelID)
        await channel.set_permissions(role, connect=False,read_messages=True)
        await ctx.channel.send(f'{ctx.author.mention} Голосовой чат закрыт! 🔒')
    conn.commit()
    conn.close()

@voice.command()
async def unlock(self, ctx):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    id = ctx.author.id
    c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
    voice=c.fetchone()
    if voice is None:
        await ctx.channel.send(f"{ctx.author.mention} Вы не Владелец голосового чата.")
    else:
        channelID = voice[0]
        role = discord.utils.get(ctx.guild.roles, name='@everyone')
        channel = self.bot.get_channel(channelID)
        await channel.set_permissions(role, connect=True,read_messages=True)
        await ctx.channel.send(f'{ctx.author.mention} Голосовой чат открыт! 🔓')
    conn.commit()
    conn.close()

@voice.command(aliases=["allow"])
async def permit(self, ctx, member : discord.Member):
    conn = sqlite3.connect("voice.db")
    c = conn.cursor()
    id = ctx.author.id
    c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
    voice=c.fetchone()
    if voice is None:
        await ctx.channel.send(f"{ctx.author.mention} Вы не владелец голосового чата.")
    else:
        channelID = voice[0]
        channel = self.bot.get_channel(channelID)
        await channel.set_permissions(member, connect=True)
        await ctx.channel.send(f"{ctx.author.mention} Вы разрешили {member.name} иметь доступ к каналу. ✅")
    conn.commit()
    conn.close()

@voice.command(aliases=["deny"])
async def reject(self, ctx, member : discord.Member):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    id = ctx.author.id
    guildID = ctx.guild.id
    c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
    voice=c.fetchone()
    if voice is None:
        await ctx.channel.send(f"{ctx.author.mention} Вы не владелец голосового чата.")
    else:
        channelID = voice[0]
        channel = self.bot.get_channel(channelID)
        for members in channel.members:
            if members.id == member.id:
                c.execute("SELECT voiceChannelID FROM guild WHERE guildID = ?", (guildID,))
                voice=c.fetchone()
                channel2 = self.bot.get_channel(voice[0])
                await member.move_to(channel2)
        await channel.set_permissions(member, connect=False,read_messages=True)
        await ctx.channel.send(f'{ctx.author.mention} Вы запретили {member.name} иметь доступ к каналу. ❌')
    conn.commit()
    conn.close()

@voice.command()
async def limit(self, ctx, limit):
    conn = sqlite3.connect("voice.db")
    c = conn.cursor()
    id = ctx.author.id
    c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
    voice=c.fetchone()
    if voice is None:
        await ctx.channel.send(f"{ctx.author.mention} Вы не владелец голосового чата")
    else:
        channelID = voice[0]
        channel = self.bot.get_channel(channelID)
        await channel.edit(user_limit = limit)
        await ctx.channel.send(f"{ctx.author.mention} Вы установили ограничение канала равным "+ "{}!".format(limit))
        c.execute("SELECT channelName FROM userSettings WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            c.execute("INSERT INTO userSettings VALUES (?, ?, ?)", (id,f'{ctx.author.name}',limit))
        else:
            c.execute("UPDATE userSettings SET channelLimit = ? WHERE userID = ?", (limit, id))
    conn.commit()
    conn.close()

@voice.command()
async def claim(self, ctx):
    x = False
    conn = sqlite3.connect("voice.db")
    c = conn.cursor()
    channel = ctx.author.voice.channel
    if channel == None:
        await ctx.channel.send(f"{ctx.author.mention} Вы не в голосовом канале.")
    else:
        id = ctx.author.id
        c.execute("SELECT userID FROM voiceChannel WHERE voiceID = ?", (channel.id,))
        voice=c.fetchone()
        if voice is None:
            await ctx.channel.send(f"{ctx.author.mention} Вы не владелец этого канала!")
        else:
            for data in channel.members:
                if data.id == voice[0]:
                    owner = ctx.guild.get_member(voice [0])
                    await ctx.channel.send(f"{ctx.author.mention} Этот канал уже принадлежит {owner.mention}!")
                    x = True
            if x == False:
                await ctx.channel.send(f"{ctx.author.mention} Теперь вы владелец канала!")
                c.execute("UPDATE voiceChannel SET userID = ? WHERE voiceID = ?", (id, channel.id))
        conn.commit()
        conn.close()

#Autorole join
@bot.event
async def on_member_join( member):
    role = discord.utils.get(member.server.roles, name= "Участники")
    await bot.add_roles(member, role)

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
    emb.add_field( name = "Аккаунт был создан:", value= member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    emb.set_thumbnail( url = member.avatar_url)
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    emb.set_author( name = ctx.message.author, url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

#Filter
@bot.event
async def on_message( message ):
    await bot.process_commands( message )

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

client.run(os.getenv('BOT_TOKEN'))
