import discord
import os
import random
from datetime import datetime
from typing import Optional

from discord import Embed, Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands
# from discord.ext.commands import Bot
from dotenv import load_dotenv


load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)
# bot = Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.command(name="userinfo", aliases=["memberinfo", "ui", "mi"])
async def user_info(self, ctx, target: Optional[Member]):
	target = target or ctx.author

	embed = Embed(title="User information",
					  colour=target.colour,
					  timestamp=datetime.utcnow())

	embed.set_thumbnail(url=target.avatar_url)

	fields = [("Name", str(target), True),
				  ("ID", target.id, True),
				  ("Bot?", target.bot, True),
				  ("Top role", target.top_role.mention, True),
				  ("Status", str(target.status).title(), True),
				  ("Activity", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
				  ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
				  ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
				  ("Boosted", bool(target.premium_since), True)]

	for name, value, inline in fields:
		embed.add_field(name=name, value=value, inline=inline)

	await ctx.send(embed=embed)

@client.command(name="serverinfo", aliases=["guildinfo", "si", "gi"])
async def server_info(self, ctx):
	embed = Embed(title="Server information",
					colour=ctx.guild.owner.colour,
					timestamp=datetime.utcnow())

	embed.set_thumbnail(url=ctx.guild.icon_url)

	statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

	fields = [("ID", ctx.guild.id, True),
				  ("Owner", ctx.guild.owner, True),
				  ("Region", ctx.guild.region, True),
				  ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
				  ("Members", len(ctx.guild.members), True),
				  ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
				  ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
				  ("Banned members", len(await ctx.guild.bans()), True),
				  ("Statuses", f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}", True),
				  ("Text channels", len(ctx.guild.text_channels), True),
				  ("Voice channels", len(ctx.guild.voice_channels), True),
				  ("Categories", len(ctx.guild.categories), True),
				  ("Roles", len(ctx.guild.roles), True),
				  ("Invites", len(await ctx.guild.invites()), True),
				  ("\u200b", "\u200b", True)]

	for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

	await ctx.send(embed=embed)

# @client.command(name="whois")
# async def whois(ctx,user:discord.Member=None):

#     if user==None:
#         user=ctx.author

#     rlist = []
#     for role in user.roles:
#       if role.name != "@everyone":
#         rlist.append(role.mention)

#     b = ", ".join(rlist)


#     embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)

#     embed.set_author(name=f"User Info - {user}"),
#     embed.set_thumbnail(url=user.avatar_url),
#     embed.set_footer(text=f'Requested by - {ctx.author}',
#   icon_url=ctx.author.avatar_url)

#     embed.add_field(name='ID:',value=user.id,inline=False)
#     embed.add_field(name='Name:',value=user.display_name,inline=False)

#     embed.add_field(name='Created at:',value=user.created_at,inline=False)
#     embed.add_field(name='Joined at:',value=user.joined_at,inline=False)

  
 
#     embed.add_field(name='Bot?',value=user.bot,inline=False)

#     embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
#     embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)

#     await ctx.send(embed=embed)



# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     guild = client.get_guild(897657564446212156)
#     brooklyn_99_quotes = [
#         f'Ya Hayukkkk, {message.author.mention}',
#     ]
#     # deskripsi = [
#     #     f'{message.author.mention} adalah orang paling keren di {guild.name}'
#     # ]


#     if message.content == 'hayuk!':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)

#     if message.content == '!hellobot':
#         embedVar = discord.Embed(title="Hello Tampan", description=f"{message.author.mention} adalah orang paling keren di {guild.name}", color=0xD80004)
#         # embedVar.add_field(name="Field1", value="hi", inline=False)
#         # embedVar.add_field(name="Field2", value="hi2", inline=False)
#         await message.channel.send(embed=embedVar)

#     if 'happy birthday' in message.content.lower():
#         await message.channel.send('Happy Birthday! 🎈🎉')
 

@client.event
async def on_member_join(member):
    guild = client.get_guild(897657564446212156)
    channel = client.get_channel(897784840680783893)
    embedVar = discord.Embed(title="Welcome! :star_struck: :partying_face: ", description=f"Selamat Datang {member.mention}! :partying_face: ", color=0x0055FF)
    embedVar2 = discord.Embed(title="Welcome! :star_struck: :partying_face: ", description=f"Selamat Datang di {guild.name}, {member.name}! :partying_face: ", color=0xD80004)
    await channel.send(embed=embedVar)
    await member.send(embed=embedVar2)

client.run(TOKEN)