from core.classes import Cog_Extension
from modal import EmbedModal
import nextcord
import json
from nextcord.ext import commands
import time
import datetime
class test (Cog_Extension):

    @commands.is_owner()
    @commands.command(name='support')
    async def support(self,ctx):
        hi=nextcord.ui.Button(label='click me', style=nextcord.ButtonStyle.blurple)
        hi2=nextcord.ui.Button(label='click me', style=nextcord.ButtonStyle.green)
        myview=nextcord.ui.View(timeout=180)
        myview.add_item(hi2)
        myview.add_item(hi)
        notview=nextcord.ui.View(timeout=180)

        async def hi_callback(interaction):
            await interaction.response.send_message('hello',ephemeral=True)
        async def hi_callback1(interaction):
            await interaction.response.edit_message(content="hello",view=notview)
            

        hi.callback=hi_callback
        hi2.callback=hi_callback1

        a=await ctx.send("hi",view=myview)
    
    @nextcord.slash_command(name="test",description="Interdfs")
    async def test(self,interaction:nextcord.Integration,message:str=nextcord.SlashOption(name="test",choices={'loli':'loli3','fuck':'fuck5'})):
        await interaction.response.send_message(f'{message}')
    
    @commands.command(name="embed")
    async def embed(self,ctx):
        hi3=nextcord.ui.Button(label='click me', style=nextcord.ButtonStyle.blurple)
        myview2=nextcord.ui.View(timeout=20)
        myview2.add_item(hi3)

        async def hi_callback(interaction):
            await interaction.response.send_modal(EmbedModal())
        hi3.callback=hi_callback
        await ctx.send("hi",view=myview2)

    @commands.command(name='hi')
    async def sendmenu(self,ctx):
        async def callback1(interaction):
            if dropdown.values[0] == "gif":
                await ctx.send("hello")
            if dropdown.values[0] == "gif1":
                await ctx.send("hi")
            if dropdown.values[0] == "gif2":
                await ctx.send("hie")

        ts1=nextcord.SelectOption(label="hello",value="gif",description="test")
        ts2=nextcord.SelectOption(label="hello1",value="gif1",description="test1")
        ts3=nextcord.SelectOption(label="hello2",value="gif2",description="test2")
        dropdown=nextcord.ui.Select(placeholder="test",options=[ts1,ts2,ts3])
        dropdown.callback=callback1
        value1=nextcord.ui.View(timeout=180)
        value1.add_item(dropdown)
        await ctx.send("hello",view=value1)






def setup(bot):
    bot.add_cog(test(bot))