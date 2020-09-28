import discord
import re

client = discord.Client() # 接続するクライアント

TOKEN = 'NzU5Nzg2MDIxNTMyNzI5Mzc0.X3Cj3w.E3NSXQEC-fDhy5Evsm7kXunOOxg'
    
# Botの起動とDiscordサーバーへの接続

@client.event
async def on_ready():
    print("稼働の準備が完了しました")
    
@client.event
async def message_count(channel):
    matched = re.match(r'(.+)（(\d+)）',channel.name)
    if matched:
        #もし、メッセージのカウントが既に行われていたら
        base_name = matched.groups()[0] # 元のチャンネル名
        count = int(matched.groups()[1]) # メッセージ数
        await channel.edit(name=f"{base_name}（{count+1}）")
        return

    count = 0
    async for message in channel.history(limit=None):
        if not message.author.bot:
            # 人間が投稿していたらカウントを1増やす
            count += 1 

    await channel.edit(name=f"{channel.name}（{count}）")

@client.event

async def on_message(message):

 if message.author.bot:
        return
        
 await message_count(message.channel)
 print("投稿完了")

client.run(TOKEN)
