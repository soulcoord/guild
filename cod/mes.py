import asyncio
from discord import Embed, slash_command
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class mes (Cog_Extension):
  @nextcord.slash_command(name='深淵',description='深淵代打申請(僅幫代打9~12層)')
  async def 深淵(self,interaction:nextcord.Interaction,name:str,uid:int=nextcord.SlashOption(name='uid'),help=nextcord.SlashOption(name='需要幫忙的項目')):
    emb=nextcord.Embed(title="溫迪深淵代打", description="★ 提供代打深境螺旋或是需要角色健檢及隊伍建議的 ★", color=0xffd6d6)
    emb.set_author(name="Colombina#7304", url="https://discord.com/channels/@me/988654327990214656", icon_url="https://cdn.discordapp.com/avatars/537846086749126657/c3ae37775b12e038a1d0c57528ea9e6a.webp?size=80")
    emb.set_thumbnail(url=interaction.user.display_avatar.url)
    emb.add_field(name="資訊", value=f"遊戲名稱:{name}\n UID:{uid}\n 需要幫忙的項目:{help}\n", inline=False)
    emb.add_field(name="已完成代打申請", value="請先將遊戲帳號密碼私訊温迪，若方便也可附上你的角色圖鑑+練度**[Colombina#7304](https://discord.com/channels/@me/988654327990214656)**", inline=False)
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
      if interaction.user.id not in [537846086749126657,560450371491725313]:
        await interaction.response.send_message('非溫迪本人按這個的話沒用喔',ephemeral=True)
      else:  
        await interaction.response.edit_message(embed=emb,view=notview)
    hi.callback=hi_callback1
    await interaction.response.send_message(f'<@{interaction.user.id}>',embed=emb,view=myview)
  @commands.Cog.listener()
  async def on_message(self,mes:nextcord.Message):
    if mes.channel.id == 992008416140734574 or mes.channel.id == 978924406745210900:
      if mes.type != (nextcord.MessageType.chat_input_command)and mes.author.id not in  [972137604470407168,537846086749126657,992351373280690206]:
        try:
          await mes.delete()
          await mes.author.send(f'在<#{mes.channel.id}>請使用斜線指令喔(詳細說明請看頻道訂選訊息)')
        except:
          no_dm=self.bot.get_channel(978708780445495328)
          time_out=await no_dm.send(f"<@{mes.author.id}>無法私訊給您，請先確認是否將：隱私設定>允許私人訊息選項開啟(訊息30秒自動刪除)")
          await time_out.delete(delay=30)
        
    elif mes.channel.id == 990553527547990046:
      with open('uid.json','r',encoding='utf8') as uid:
        user_uid=json.load(uid)
      user_uid[str(mes.author.id)]={}
      user_uid[str(mes.author.id)]["content"]=mes.content
      user_uid[str(mes.author.id)]["id"]=mes.id
      with open('uid.json','w',encoding='utf8') as uid:
        json.dump(user_uid,uid)
def setup(bot):
    bot.add_cog(mes(bot))