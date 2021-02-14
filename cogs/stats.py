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
	def __init__(self, client):
		self.client=client

	@commands.Cog.listener()
	async def on_member_join(self, ctx, member):
		channel = self.get_channel(channel1)
		await channel.edit(name=f'All Members: {total_users}')

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		channel = self.get_channel(channel1)
		await channel.edit(name=f'All Members: {total_users}')

	@commands.group(name='stats')
	async def stats(self, ctx):
		print (f'Stats activate')

	@stats.command()
	@commands.has_permissions(administrator=True)
	async def setup(self, ctx, *, member : discord.Member=None):
		stat = await ctx.guild.create_category_channel(name= '📊Статистика сервера📊', position=1)
		total_users = str(ctx.guild.member_count)
		region = str(ctx.guild.region)
		owner = str(ctx.guild.owner)
		clients = len(self.servers)
		online = len([m for m in ctx.guild.members if m.status != discord.Status.offline])
		channel1 = await ctx.guild.create_voice_channel(name=f'All Members: {total_users}', category = stat)
		await channel1.set_permissions(ctx.guild.default_role, connect = False)
		#channel2 = await ctx.guild.create_voice_channel(name=f'Online: {online}', category = stat)
		#await channel2.set_permissions(ctx.guild.default_role, connect = False)
		channel3 = await ctx.guild.create_voice_channel(name=f'Region: {region}', category = stat)
		await channel3.set_permissions(ctx.guild.default_role, connect = False)
		def check(a,b,c):
			return len(total_users,online)
		print(f'Успешно загружена статистика сервера')

def setup(client):
	client.add_cog(stats(client))
