import re
from unicodedata import name
from core.classes import Cog_Extension
import nextcord
import json
from modal import quest as qu
from nextcord.ext import commands
class quest (Cog_Extension):
  @nextcord.slash_command(name='求助',description='發送求助')
  async def 委託(self,interaction:nextcord.interactions):
    with open('uid.json','r',encoding='utf8') as uid:
        user_uid=json.load(uid)
    find_uid = re.compile(r'(?<=\D)[0-9]{9}(?=\D)')
    uid=user_uid[str(interaction.user.id)]["content"]
    find_name = re.compile(r'[^名字:：\s]\w{1,}')
    name=user_uid[str(interaction.user.id)]["content"]
    my_uid = re.findall(find_uid, uid)
    my_name=re.findall(find_name,name)
    await interaction.response.send_modal(qu(my_uid[0],my_name[0]))



def setup(bot):
    bot.add_cog(quest(bot))