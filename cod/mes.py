from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class mes (Cog_Extension):
  @commands.Cog.listener()
  async def on_message(self,mea):
    if mea.channel.id == 992008416140734574 and ('id') in mea.content or mea.channel.id == 992008416140734574 and ('ID') in mea.content:
        embed=nextcord.Embed(title="溫迪深淵代打", description="★ 提供代打深境螺旋或是需要角色健檢及隊伍建議的 ★", color=0xc4e1ff)
        embed.set_author(name="温迪#7304", url="https://discord.com/channels/@me/988654327990214656", icon_url="https://cdn.discordapp.com/avatars/537846086749126657/c3ae37775b12e038a1d0c57528ea9e6a.webp?size=80")
        embed.add_field(name="1.在此頻道中留言，留言請參考下面的範例↓↓↓", value="遊戲ID : （自己的）\n 遊戲UID：（自己的）", inline=False)
        embed.add_field(name="2.先把你的角色圖鑑+練度私信我", value="​", inline=False)
        embed.add_field(name="3. 請在discord私訊我你要被幫忙的時間以及你的遊戲帳號密碼。", value="​", inline=False)
        embed.add_field(name="4. 打完后請你登入遊戲後到深境螺自行領取獎勵 (★重要★)。", value="​", inline=False)
        embed.add_field(name="""★ 代打期間，我會開啟直播，請你前來觀看~ ★ 不論你是否曾經找過我代打深淵，"每一期"深淵都可以留言讓我來代打 ★ 代打深境螺旋僅限9~12層""", value="​", inline=False)
        embed.add_field(name="影片", value="[這是我的單通影片](https://youtu.be/_yxkdqhN5FY)", inline=False)
        embed.set_image("https://truth.bahamut.com.tw/s01/202106/ba34cbb83d148bc50eda6aa0939c8d1b.JPG")
        await mea.author.send(embed=embed)
def setup(bot):
    bot.add_cog(mes(bot))