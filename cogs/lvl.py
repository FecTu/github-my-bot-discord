import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from discord.utils import get
import sys
import os
import requests
import io
import json

class level(commands.Cog):
	def __init__(self, client):
		self.client=client

	@commands.Cog.listener()
	async def on_message(self, message):
		with open('lvl.json', 'r') as f:
			users = json.load(f)
		async def update_data(users,user):
			if not user in users:
				users[user] = {}
				users[user]['exp'] = 0
				users[user]['lvl'] = 1
		async def add_exp(users,user,exp):
			users[user]['exp'] += exp
		async def add_lvl(users,user):
			exp = users[user]['exp']
			lvl = users[user]['lvl']
			lvl_end = int(exp ** (1/4))
			if exp > lvl:
				await message.channel.send(f'{message.author.mention} повысил свой уровень')
				users[user]['exp'] = 0
				users[user]['lvl'] = lvl + 1
		await update_data(users,str(message.author.id))
		await add_exp(users,str(message.author.id),0.1)
		await add_lvl(users,str(message.author.id))
		with open('lvl.json', 'w') as f:
			json.dump(users,f)

	@commands.command(aliases = ['я', 'карта'])
	@commands.has_permissions(administrator=True)
	async def card_user(self, ctx, amount = 1):
		await ctx.channel.purge( limit = amount )
		with open('lvl.json', 'r') as f:
			users = json.load(f)

		img = Image.new('RGBA', (400, 200), '#232529')
		url = str(ctx.author.avatar_url)[:-10]
	
		responce = requests.get(url, stream = True)
		responce = Image.open(io.BytesIO(responce.content))
		responce = responce.convert('RGBA')
		responce = responce.resize((100, 100), Image.ANTIALIAS)
	
		img.paste(responce, (15, 15, 115, 115))
	
		idraw = ImageDraw.Draw(img)
		name = ctx.author.name # Sora
		tag = ctx.author.discriminator # 3700

		headline = ImageFont.truetype('arial.ttf', size = 20)
		undertext = ImageFont.truetype('arial.ttf', size = 12)
		headlene = ImageFont.truetype('arial.ttf', size = 15)

		idraw.text((145, 15), f'{name}#{tag}', font = headline) # Sora#3700
		idraw.text((145, 50), f'ID: {ctx.author.id}', font =undertext)

		img.save('rank_card.png')

		await ctx.send(file = discord.File(fp = 'rank_card.png'))

def setup(client):
	client.add_cog(level(client))