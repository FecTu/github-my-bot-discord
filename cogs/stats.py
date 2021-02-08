import discord
import asyncio
import pyowm
import json
from random import randint, choice
from discord.ext import commands
from discord.utils import get
from discord import utils
import traceback
import sqlite3
import validators
import os
from time import sleep
import requests

class stats(commands.Cog):
	def __init__(self, bot):
		self.bot=bot

	@commands.Cog.listener()
	async def on_member_join(self, ctx, member):
		total_users = len(ctx.guild.members)
		online = len([m for m in ctx.guild.members if m.status != discord.Status.offline])
		pass


	@commands.group(name='stats')
	async def stats(self, ctx):
		print (f'Stats activate')

	@stats.command()
	@commands.has_permissions(administrator=True)
	async def setup(self, ctx, *, member : discord.Member=None):
		stat = await ctx.guild.create_category_channel(name= '📊Статистика сервера📊',position=reference.position+1)
		total_users = len(ctx.guild.members)
		online = len([m for m in ctx.guild.members if m.status != discord.Status.offline])
		channel = await ctx.guild.create_voice_channel(name=f'All Members: {ctx.guild.members}', category = stat)
		channel2 = await ctx.guild.create_voice_channel(name=f'Online: {online}', category = stat)
		channel3 = await ctx.guild.create_voice_channel(name=f'Region: {ctx.guild.region}', category = stat)
		def check(a,b,c):
			return len(total_users,online)
		print(f'Успешно загружена статистика сервера')

def setup(bot):
	bot.add_cog(stats(bot))