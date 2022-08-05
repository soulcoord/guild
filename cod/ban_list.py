from cod.ban import ban
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
with open('test.json','r',encoding='utf-8') as ban_list:
  banlast=json.load(ban_list)
print(banlast)
class voice (Cog_Extension):
  @commands.command()
  @commands.has_any_role("社長","工程師")
  async def ban_list(self,ctx):
    em=nextcord.Embed(title="ban人名單", color=0xffe380)
    for a in banlast['ban']:
      u_name=self.bot.get_user(a)
      em.add_field(name=f"{u_name}", value="​", inline=False)
    await ctx.send(embed=em)





def setup(bot):
    bot.add_cog(voice(bot))