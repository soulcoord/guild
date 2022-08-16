from discord import User
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class kick (Cog_Extension):
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,*,member,reason=None):
        c_r=member.replace('<','').replace('@','').replace('>','')   
        c=str(c_r).split(' ')
        for c_kick in c:
            a=ctx.guild.get_member(int(c_kick))
            await a.kick(reason=reason)
    @nextcord.slash_command(name='自我介紹')
    async def 自我介紹(self,interaction:nextcord.interactions):
        with open('uid.json','r',encoding='utf8') as uid:
            user_uid=json.load(uid)
        if str(interaction.user.id) in user_uid:
            emb=nextcord.Embed(color=0xffdbdb)
            emb.set_author(name=interaction.user.display_name,icon_url=interaction.user.display_avatar.url)
            emb.add_field(name="​", value=f'{user_uid[str(interaction.user.id)]["content"]}', inline=False)            
            await interaction.send(embed=emb)
        elif interaction.user.id not in user_uid:
            await interaction.send('請先去<#990553527547990046>輸入資料')
def setup(bot):
    bot.add_cog(kick(bot))