from encodings import utf_8
from lib2to3.pgen2 import token
from turtle import end_fill
import nextcord
from nextcord.ext import commands
import os
import json
intents=nextcord.Intents.all()
bot = commands.Bot(command_prefix='$',intents=intents)
with open ("test.json","r",encoding='utf8') as jfile:
  jdate=json.load(jfile)

@bot.event
async def on_ready():
    print('ok')


@bot.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.errors.CommandInvokeError):
    await ctx.send("好像沒這個人喔")
  if isinstance(error,commands.errors.MissingRequiredArgument):
    await ctx.send("要輸入成員的@喔")
  if isinstance(error,commands.errors.MissingPermissions):
    await ctx.send("你的權限不足喔")


@commands.is_owner()
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cod.{extension}')
    await ctx.send(f'導入{extension}成功')


@commands.is_owner()
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cod.{extension}')
    await ctx.send(f'導出{extension}成功')


@commands.is_owner()
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cod.{extension}')
    await ctx.send(f'重製{extension}成功')


for filename in os.listdir('./cod'):
    if filename.endswith('.py'):
        bot.load_extension(f'cod.{filename[:-3]}')



if __name__ == "__main__":
    bot.run(jdate['token'])