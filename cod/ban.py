from tkinter.tix import TCL_IDLE_EVENTS
from discord import Interaction
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class ban(Cog_Extension):
  @commands.Cog.listener()
  async def on_member_join(self,mem):
    with open('test.json','r',encoding='utf8') as loli:
      loli1=json.load(loli)
      if mem.id in loli1['ban']:
        await mem.ban(reason='機器人行為')   
        c=self.bot.get_channel(978708780445495328)
        await c.send(f"{mem.mention}抓到你咯 還敢亂群")
      else:
        embeds=nextcord.Embed(title="大東亞帝國", description="大明王朝Ming dynasty", color=0xe32626)
        embeds.add_field(name="新手須知", value=f"{mem.mention} 請詳閱 <#978707952640872548> 以了解伺服器規範！\n 同時可以透過 <#978708014695600188> 熟悉頻道功能，\n 如果想快速認識大家可以到 <#990553527547990046> 。 ", inline=False)
        embeds.add_field(name="身分組領取", value="並且可透過 <#978740632086523914> 開啟色色區或者是內鬼情報區哦！ ", inline=False)
        embeds.add_field(name="遊戲疑難", value="另外有任何遊戲疑問可在 <#978925411494920243>  進行詢問，\n 打不過的秘境或者BOSS也可於 <#978924406745210900>  來發布委託！", inline=False)
        embeds.set_image("https://upload.cc/i1/2022/11/10/rb6dCB.png")
        c=self.bot.get_channel(978708780445495328)
        w=self.bot.get_channel(978680659428147292)
        await c.send(f"旅行者{mem.mention}，歡迎您的到來！")
        await w.send(embed=embeds)
  
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self,ctx,*,member,reason=None):
    c_r=member.replace('<','').replace('@','').replace('>','')
    c=str(c_r).split(' ')
    for c_kick in c:
        a=ctx.guild.get_member(int(c_kick))
        await a.ban(reason=reason)

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def join_ban(self,ctx,*,member):
    with open('test.json','r',encoding='utf8') as loli:
      loli1=json.load(loli)
    c_r=member.replace('<','').replace('@','').replace('>','')
  
    c=str(c_r).split(' ')
    for c_kick in c:
        loli1['ban'].append(int(c_kick))
    with open('test.json','w',encoding='utf8') as loli:
      json.dump(loli1,loli)

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def remove_ban(self,ctx,*,member):
    with open('test.json','r',encoding='utf8') as loli:
      loli1=json.load(loli)
    c_r=member.replace('<','').replace('@','').replace('>','')
  
    c=str(c_r).split(' ')
    for c_kick in c:
        loli1['ban'].remove(int(c_kick))
    with open('test.json','w',encoding='utf8') as loli:
      json.dump(loli1,loli)







def setup(bot):
    bot.add_cog(ban(bot))
   
