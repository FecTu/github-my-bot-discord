import discord
from discord.ext import commands
import json

class level(commands.Cog):
	def __init__(self, bot):
		self.bot=bot

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
			if exp > lvl:
				await message.channel.send(f'{message.author.mention} повысил свой уровень')
				users[user]['exp'] = 0
				users[user]['lvl'] = lvl + 1
		await update_data(users,str(message.author.id))
		await add_exp(users,str(message.author.id),0.1)
		await add_lvl(users,str(message.author.id))
		with open('lvl.json', 'w') as f:
			json.dump(users,f)

	@commands.command( pass_context=True )
	async def rank(ctx, user: discord.Member=None):
		if users is None:
			users = message.author.id
		with open('lvl.json', 'r') as f:
			users = json.load(f)
			lvl = users[user]['lvl']
			exp = users[user]['exp']
			rank = discord.Embed(name='Rank', colour = 0x1100ff)
			rank.add_field(name='Ваш Уровень:', value='{}'.format(lvl))
			rank.add_field(name='Очки опыта:', value='{}'.format(exp), inline=True)
			rank.set_footer(text='Спасибо за то, что вы являетесь частью сообщества!')
			rank.set_thumbnail(url=user.avatar_url)
			await ctx.send( embed=rank )

def setup(bot):
	bot.add_cog(level(bot))