import discord
import os
import random
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


@client.command()
async def status(ctx, member : discord.Member=None):
  if member is None:
    member = ctx.author
  embed=discord.Embed(title=f"{member.name} your current status is", description= f'{member.activities[0].name}', color=0xcd32a7)
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