import discord
from discord.ext import commands

class KeywordListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"已成功載入 KeywordListener")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        keywords = ["keyword1", "keyword2"]  # 這裡放置你要偵測的關鍵字
        target_channel_id = 1234567890  # 這裡放置目標頻道的 ID

        if any(keyword in message.content for keyword in keywords):
            target_channel = self.bot.get_channel(target_channel_id)
            if target_channel:
                await target_channel.send(f"重新整理後的訊息: {message.content}")

async def setup(bot):
    await bot.add_cog(KeywordListener(bot))