from cgi import test
from core.classes import Cog_Extension
import nextcord
import json
from modal import quest as qu
from nextcord.ext import commands
class quest (Cog_Extension):
  @nextcord.slash_command(name='求助',description='發送求助')
  async def 委託(self,interaction:nextcord.interactions):
    await interaction.response.send_modal(qu())



def setup(bot):
    bot.add_cog(quest(bot))