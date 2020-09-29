import discord
import re
import os

client = discord.Client() # 接続するクライアント


TOKEN = os.environ["TOKEN"]

@client.event
async def on_ready():
    print("稼働の準備が完了しました")

@client.event
async def on_message(message):
    if message.author.bot:
        return
# 犬
    if '8508' in str(message.author):
        emoji = '\U0001f4a9'
        await message.add_reaction(emoji)
# 鴨
    if '4914' in str(message.author):
        emoji = '\U0001f986'
        await message.add_reaction(emoji)
# e
    if '8454' in str(message.author):
        emoji = '\U0001f4a9'
        await message.add_reaction(emoji)
# B
    if '6224' in str(message.author):
        emoji = '\U0001f4a9'
        await message.add_reaction(emoji)
# N
    if '9089' in str(message.author):
        emoji = '\U0001f4a9'
        await message.add_reaction(emoji)
# me
    if '4089' in str(message.author):
        emoji = '\U0001f4a9'
        await message.add_reaction(emoji)
client.run(TOKEN)
