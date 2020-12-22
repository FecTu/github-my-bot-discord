+import discord
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
import traceback
import sqlite3
import validators
import nekos
import json

import os
from time import sleep
import requests

PREFIX = "."
bad_words = [ "нахуй", "бунт", "лох", "пидр", "долбаеб", "пидар", "пидарас", "пидор", "пидорас" ]

client = commands.Bot( command_prefix = PREFIX )
client.remove_command( "help" )

exts=['music']

@client.event
async def on_ready():
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
    await client.change_presence( status= discord.Status.online, activity= Activity( name= "за Team Inlors", type=ActivityType.watching))

#Rank
@client.event
async def on_message(message):
    with open("E:\\botdiscord\\Ember\\Ember\\lvl.json", "r") as f:
            users = json.load(f)
    await update_data(users,message.author)
    await add_exp(users,message.author),0.1
    await add_lvl(users,message.author)
    with open("E:\\botdiscord\\Ember\\Ember\\lvl.json", "w") as f:
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

@client.command( pass_context=True )
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

#EmojiRole

@client.event
async def EmojiRole(ctx):
	emb = discord.Embed( title= "Ваш пол", color=0x1100ff)
	emb.add_field( name = payload.emoji.name, value= "Мужской", inline= True )
	emb.add_field( name = payload.emoji.name, value= "Женский", inline= True )
	await ctx.send(embed = emb)

#Private rooms
@client.event
async def on_voice_state_update( member, before, after,):
        if before.channel is None and after.channel.id == 788710906380025877:
            for guild in client.guilds:
                maincategory = discord.utils.get( guild.categories, id = 788717733008244757 )
                channel2 = await guild.create_voice_channel( name=f"Канал {member.display_name}", category = maincategory )
                await channel2.set_permissions(member, connect = True, mute_members = True, move_members = True, manage_channels = True)
                await channel2.edit(user_limit = 2)
                await member.move_to(channel2)
                def check(x,y,z):
                    return len(channel2.members) == 0
                await client.wait_for( "voice_state_update", check=check )
                await channel2.delete()

#Autorole join
@client.event
async def on_member_join( member):
    with open("lvl.json", "r") as f:
        users = json.load(f)

    await update_data(users,member)

    with open("E:\\Play Alexsey\\Программирование\\Microsoft Visual Studio\\2019\\Professional\\Ember\\lvl.json", "w") as f:
        json.dump(users, f)

        channel = client.get_channel( 788051331927507025 )

    role = discord.utils.get( member.guild.roles, id = 789036534988275712 )

    await member.add_roles( role )

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
	emb.add_field( name = "Аккаунт был создан:", value= member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
	emb.set_thumbnail( url = member.avatar_url)
	emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
	emb.set_author( name = ctx.message.author, url= ctx.message.author.avatar_url)
	await ctx.send(embed = emb)

#Filter
@client.event
async def on_message( message ):
    await client.process_commands( message )

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

#Help bot
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
#token = open( "token.txt", "r").readline()

#token = os.environ.get("BOT_TOKEN")

client.run(os.getenv('BOT_TOKEN'))