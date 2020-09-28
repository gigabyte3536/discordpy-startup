import discord
import re
import os

client = discord.Client() # 接続するクライアント
    
# Botの起動とDiscordサーバーへの接続

TOKEN = os.environ["TOKEN"]

@client.event
async def on_ready():
    print("稼働の準備が完了しました")
    

@client.event
async def on_message(message):
     if message.author.bot:
        return
    emoji = client.get_emoji(310177266011340803)
    await message.add_reaction(emoji)

client.run(TOKEN)
