from cod.ban import ban
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands


class ban_list (Cog_Extension):
  @commands.command()
  @commands.has_any_role(978680963099942912,"工程師")
  async def ban_list(self,ctx):
    with open('test.json','r',encoding='utf-8') as ban_l:
      banlast=json.load(ban_l)
    em=nextcord.Embed(title="ban人名單", color=0xffe380)
    for a in banlast['ban']:
      u_name=self.bot.get_user(a)
      em.add_field(name=f"{u_name}", value="​", inline=False)
    await ctx.send(embed=em)





def setup(bot):
    bot.add_cog(ban_list(bot))