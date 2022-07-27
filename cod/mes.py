from discord import Embed, slash_command
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class mes (Cog_Extension):
  @nextcord.slash_command(name='深淵',description='深淵代打申請(僅幫代打9~12層)')
  async def 深淵(self,interaction:nextcord.Interaction,name:str,uid:int=nextcord.SlashOption(name='uid'),help=nextcord.SlashOption(name='需要幫忙的項目')):
    emb=nextcord.Embed(title="溫迪深淵代打", description="★ 提供代打深境螺旋或是需要角色健檢及隊伍建議的 ★", color=0xffd6d6)
    emb.set_author(name="温迪#7304", url="https://discord.com/channels/@me/988654327990214656", icon_url="https://cdn.discordapp.com/avatars/537846086749126657/c3ae37775b12e038a1d0c57528ea9e6a.webp?size=80")
    emb.set_thumbnail(url=interaction.user.avatar.url)
    emb.add_field(name="資訊", value=f"遊戲名稱:{name}\n UID:{uid}\n 需要幫忙的項目:{help}\n", inline=False)
    emb.add_field(name="已完成代打申請", value="請先將遊戲帳號密碼私訊温迪，若方便也可附上你的角色圖鑑+練度**[温迪#7304](https://discord.com/channels/@me/988654327990214656)**", inline=False)
    emb.add_field(name="★重要★ 代打結束後，請你登入遊戲後到深境螺自行領取獎勵。", value="​", inline=False)
    emb.add_field(name="""★ 代打期間，我會開啟直播，請你前來觀看~ ★ 不論你是否曾經找過我代打深淵，"每一期"深淵都可以留言讓我來代打 ★ """, value="​", inline=False)
    emb.add_field(name="影片", value="[這是我的單通影片](https://youtu.be/_yxkdqhN5FY)", inline=False)
    emb.set_image("https://truth.bahamut.com.tw/s01/202106/ba34cbb83d148bc50eda6aa0939c8d1b.JPG")

    hi=nextcord.ui.Button(label='未完成', style=nextcord.ButtonStyle.blurple)
    hi1=nextcord.ui.Button(label='已完成',style=nextcord.ButtonStyle.red,disabled=True)
    notview=nextcord.ui.View(timeout=1)
    myview=nextcord.ui.View(timeout=None)
    myview.add_item(hi)
    notview.add_item(hi1)
    async def hi_callback1(interaction):
      if interaction.user.id != 537846086749126657:
        await interaction.response.send_message('非溫迪本人按這個的話沒用喔',ephemeral=True)
      else:  
        await interaction.response.edit_message(embed=emb,view=notview)
    hi.callback=hi_callback1
    await interaction.response.send_message(embed=emb,view=myview)
def setup(bot):
    bot.add_cog(mes(bot))