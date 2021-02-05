import discord
import asyncio
from discord.ext import commands
import traceback
import sqlite3
import validators

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
					await member.send("Creating channels too quickly you've been put on a 15 second cooldown!")
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

def setup(bot):
    bot.add_cog(voice(bot))