import discord
from discord.ext import commands
from funcion import clasf

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            image_extensions = ('.jpg', '.png', '.jpeg')

            if file_name.endswith(image_extensions):
               await attachment.save(f"./images/{file_name}")
               await ctx.send(clasf(f".image/{file_name}"))

            else:
                await ctx.send("no se a adjuntado ningun archivo")



bot.run("token")
