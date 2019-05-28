import discord
import translate
from discord.ext import commands


token = ''
prefix = ''
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('Logged in and ready to go!')


@bot.command()
async def server_ping(ctx):
	'''
	Gives ping time between bot and server.
	'''
	latency = bot.latency
	await ctx.send(latency)

@bot.command()
async def servers(ctx):
	'''
	List servers bot is currently running in.
	'''
	servers_on = bot.guilds
	await ctx.send(servers_on)


bot.run(token)