# bot.py
import os
from re import M

import discord
# from discord.ext.commands import Bot
from discord import client
# from discord import Member
from discord.ext.commands.core import guild_only
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)

# Bot On
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# Send Message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    guild = client.get_guild(897657564446212156)

    # For process command
    await client.process_commands(message)

    # if message.content == "-peraturan":
    #     await message.channel.send('``` Test Peraturan ```'
    #     + '```1. Dilarang Berkata Kasar/Sara/Rasis ```'
    #     +'```2. Dilarang Mengirim foto atau video yang berunsur pornografi```'
    #     +'```3. Dilarang menyebar Link phising atau sejenisnya```')
    if message.content == "-peraturan":
        await message.channel.send('``` Test Peraturan \n'
        +'1. Dilarang Berkata Kasar/Sara/Rasis \n'
        +'2. Dilarang Mengirim foto atau video yang berunsur pornografi\n'
        +'3. Dilarang menyebar Link phising atau sejenisnya```')

    if message.content == "hellobot!":
        embedVar = discord.Embed(title="Hello Tampan", description=f"{message.author.mention} adalah orang paling keren di {guild.name}", color=0xD80004)
        await message.channel.send(embed=embedVar)

    if 'happy birthday' in message.content.lower():
        await message.channel.send('```Happy Birthday! 🎈🎉```')
        

# @client.command(name="hellobot")
# async def on_message(message:):
#     if message.content == message:
#         embedVar = discord.Embed(title="Hello Tampan", description=f"{message.author.mention} adalah orang paling keren di {guild.name}", color=0xD80004)
#         await message.channel.send(embed=embedVar)


# Member Join
@client.event
async def on_member_join(member):
    guild = client.get_guild(897657564446212156)
    channel = client.get_channel(897784840680783893)
    embedVar = discord.Embed(title="Welcome! :star_struck: :partying_face: ", description=f"Selamat Datang {member.mention}! :partying_face: ", color=0x0055FF)
    embedVar2 = discord.Embed(title="Welcome! :star_struck: :partying_face: ", description=f"Selamat Datang di {guild.name}, {member.name}! :partying_face: ", color=0xD80004)
    await channel.send(embed=embedVar)
    await member.send(embed=embedVar2)

# Member Leave
@client.event
async def on_member_remove(member):
    guild = client.get_guild(897657564446212156)
    channel = client.get_channel(897784872616214568)
    embedVar = discord.Embed(title="Goodbye! :cry: :sob: ", description=f"Selamat Tinggal {member.mention}! :cry: ", color=0xD80004)
    # embedVar2 = discord.Embed(title="Goodbye! :cry: :sob: ", description=f" {guild.name}, {member.name}! :partying_face: ", color=0xD80004)
    await channel.send(embed=embedVar)
    # await member.send(embedVar2)
    # await channel.send(f'Selamat Tinggal {member.mention} ! :cry: ')
    # await member.send(f'Ngapain Leave dari {guild.name} bro?, {member.name}! :cry:')


# Check Status Member
@client.command(name="whois")
async def whois(ctx,user:discord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Requested by - {ctx.author}',
  icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)

  
 
    embed.add_field(name='Bot?',value=user.bot,inline=False)

    embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)

    await ctx.send(embed=embed)

#Kick Member
@client.command()
async def kick(ctx, member:discord.Member, *, reason=None):
    guild = client.get_guild(897657564446212156)
    embedVar = discord.Embed(description=f"{member.mention} Telah dikeluarkan dari {guild.name}", color=0x0055FF)
    await member.kick(reason=reason)
    await ctx.send(embed=embedVar)

#Status Activity
@client.command()
async def status(ctx, member:discord.Member):
    print(member.activity)
    await ctx.send(f'>>> {member.mention} sedang {member.activity}')

#Cek Online Member
@client.command(name="cekOn")
async def status(ctx, user: discord.Member=None):
    if not user:
        user = ctx.message.author
    print(user)
    print(user.raw_status)
    if user.raw_status == 'online':
        await ctx.send(f"```diff\n+ {user} sedang {user.raw_status}```")
    if user.raw_status == 'offline':
        await ctx.send(f"```diff\n- {user} sedang {user.raw_status}```")
    if user.raw_status == 'idle':
        await ctx.send(f"```fix\n{user} sedang {user.raw_status}```")
    if user.raw_status == 'dnd':
        await ctx.send(f"```diff\n- {user} sedang {user.raw_status}```")
    # await ctx.send(f"```{user} sedang {user.raw_status}```")


client.run(TOKEN)