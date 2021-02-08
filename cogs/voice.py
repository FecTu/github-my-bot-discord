import discord
import asyncio
from discord.ext import commands
import traceback
import sqlite3
import validators


class voice(commands.Cog):
	def __init__(self, bot):
		self.bot=bot

	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		if before.channel is None and after.channel.id == voice_priv:
			for guild in bot.guilds:
				maincategory = discord.utils.get(guild.categories, id = private)
				channel2 = await guild.create_voice_channel( name=f'Канал {member.display_name}', category = maincategory )
				await channel2.set_permissions(member, connect = True, mute_members = True, move_members = True, manage_channels = True)
				await channel2.edit(user_limit = 2)
				await member.move_to(channel2)
				def check(x,y,z):
					return len(channel2.members) == 0
				await bot.wait_for( 'voice_state_update', check=check )
				await channel2.delete()

	@commands.group()
	async def voice(self, ctx):
		print(f'voice activate')

	@voice.command()
	@commands.has_permissions(administrator=True)
	async def setup(self, ctx):
		voice = ctx.guild
		private = await voice.create_category_channel(name= 'Приватные комнаты')
		voice_priv = await voice.create_voice_channel(name= 'Создать приват', category= private)


def setup(bot):
    bot.add_cog(voice(bot))