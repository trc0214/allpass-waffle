import discord
from discord.ext import commands

class CoursesButtons(discord.ui.View):
    def __init__(self, *, timeout=180, courses):
        super().__init__(timeout=timeout)
        for course in courses:
            self.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, label=course, custom_id=f'button_{course}'))
    
    async def on_button_click(self, button, interaction):
        await interaction.response.send_message(f'You clicked {button.label}', ephemeral=True)

    
class NotesClassifier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"已成功載入 NotesClassifier")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        if '筆記上傳' not in ctx.channel.name: 
            return
        guild = ctx.guild
        categories = [category.name for category in guild.categories]
        for category in categories:
            for channel, category in category.channels:
                if channel.name == '🗒️筆記':
                    courses = category.name
        await ctx.send("Please select a course:", view=CoursesButtons(courses))

async def setup(bot):
    await bot.add_cog(NotesClassifier(bot))