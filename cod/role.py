from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class role (Cog_Extension):

  @commands.Cog.listener()
  async def on_raw_reaction_add(self,role):
    if role.message_id == 996482471803752560 or  role.message_id == 1041245596729741352:
      not_role=[996416756086222961,996416970314489987,996417043140182097,996417097620004975,996417176099635271,996417295834423458,996417376725762089,996417493474230282]
      a_g=self.bot.get_guild(role.guild_id)
      a_role=a_g.get_member(role.user_id)
      list_2 = []

      for users_role in a_role.roles:
        list_2.append(users_role.id)
      intersection = [x for x in not_role for y in list_2 if x == y]
      if len(intersection) != 0:
        await a_role.send(f'你已領取**{a_g.get_role(intersection[0])}**，請將身分組刪除再領取新的世界等級')
        intersection.clear
      if not intersection:
          if str(role.emoji) == ("1️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996416756086222961)#世界等級1
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("2️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996416970314489987)#世界等級2
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("3️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417043140182097)#世界等級3
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("4️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417097620004975)#世界等級4
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("5️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417176099635271)#世界等級5
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("6️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417295834423458)#世界等級6
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("7️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417376725762089)#世界等級7
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("8️⃣"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996417493474230282)#世界等級8
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          intersection.clear
    elif role.message_id == 996516544274243615 or  role.message_id == 1041246891704328196:
      not_role=[996470460407627786,996470641073061939,996470572475228270,996470702880346182]
      a_g=self.bot.get_guild(role.guild_id)
      a_role=a_g.get_member(role.user_id)
      list_2 = []

      for users_role in a_role.roles:
        list_2.append(users_role.id)
      intersection1 = [x for x in not_role for y in list_2 if x == y]
      if len(intersection1) != 0:
        await a_role.send(f'你已領取**{a_g.get_role(intersection1[0])}**，請將身分組刪除再領取新的伺服器')
        intersection1.clear
      if not intersection1:
          if str(role.emoji) == ("🇦"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996470460407627786)#北美
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🇧"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996470641073061939)#歐洲
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🇨"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996470572475228270)#亞洲
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🇩"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996470702880346182)#台港澳
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          intersection1.clear
    elif role.message_id == 996519987160293486 or  role.message_id == 1041247270236078161:
      if str(role.emoji) == ("📢"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470792315490326)#重大告知
        u_role=b_g.get_member(role.user_id)
        await u_role.add_roles(r_role)
      elif str(role.emoji) == ("🎉"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996471385536860230)#活動告知
        u_role=b_g.get_member(role.user_id)
        await u_role.add_roles(r_role)
    elif role.message_id == 996521942859390976 or  role.message_id == 1041247328335560725:
      not_role=[996295323829948556,996295478541041704,996292486546857995,996294524068429905,996295031424032820,996294699793002547,996294895528587355]
      a_g=self.bot.get_guild(role.guild_id)
      a_role=a_g.get_member(role.user_id)
      list_2 = []
      for users_role in a_role.roles:
        list_2.append(users_role.id)
      intersection2 = [x for x in not_role for y in list_2 if x == y]
      if len(intersection2) != 0:
        await a_role.send(f'你已領取**{a_g.get_role(intersection2[0])}**，請將身分組刪除再領取新的神之眼')
        intersection2.clear
      if not intersection2:
          if str(role.emoji) == ("🍏"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996295323829948556)#草
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("⛈️"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996295478541041704)#雷
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🚰"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996292486546857995)#水
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🔥"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996294524068429905)#火
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🌬️"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996295031424032820)#風
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🧊"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996294699793002547)#冰
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          elif str(role.emoji) == ("🪨"):
            b_g=self.bot.get_guild(role.guild_id)
            r_role=b_g.get_role(996294895528587355)#岩
            u_role=b_g.get_member(role.user_id)
            await u_role.add_roles(r_role)
          intersection2.clear
    elif role.message_id == 996527385543450695 or  role.message_id == 1041248333777338368:
      if str(role.emoji) == ("🕶️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(978738302482010193)#紳士
        u_role=b_g.get_member(role.user_id)
        await u_role.add_roles(r_role)
      elif str(role.emoji) == ("🕵️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(978739129405833256)#內鬼
        u_role=b_g.get_member(role.user_id)
        await u_role.add_roles(r_role)
    elif role.message_id == 1040718793284001833:
      with open ('test.json','r') as sm:
        smile=json.load(sm)
      smile['idiot'][f'{role.user_id}']={}
      with open('test.json','w',encoding='utf8') as loli:
        json.dump(smile,loli,indent=2)  
      if str(role.emoji) == ("🔴"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(978732220154007613)#中文成員
        u_role=b_g.get_member(role.user_id)
        with open ('test.json','r') as sm:
          smile=json.load(sm)
        if smile['idiot'][f'{role.user_id}']!=1:

          embeds=nextcord.Embed(title="大東亞帝國", description="大明王朝Ming dynasty", color=0xe32626)
          embeds.add_field(name="新手須知", value=f"{u_role.mention} 請詳閱 <#978707952640872548> 以了解伺服器規範！\n 同時可以透過 <#978708014695600188> 熟悉頻道功能，\n 如果想快速認識大家可以到 <#990553527547990046> 。 ", inline=False)
          embeds.add_field(name="身分組領取", value="並且可透過 <#978740632086523914> 開啟色色區或者是內鬼情報區哦！ ", inline=False)
          embeds.add_field(name="遊戲疑難", value="另外有任何遊戲疑問可在 <#978925411494920243>  進行詢問，\n 打不過的秘境或者BOSS也可於 <#978924406745210900>  來發布委託！", inline=False)
          embeds.set_image("https://upload.cc/i1/2022/11/10/rb6dCB.png")
          w=self.bot.get_channel(978680659428147292) 
          await w.send(embed=embeds)   

        with open ('test.json','r') as sm:
          smile=json.load(sm)
        smile['idiot'][f'{role.user_id}']=1
        with open('test.json','w',encoding='utf8') as loli:
          json.dump(smile,loli,indent=2)
        await u_role.add_roles(r_role)
      elif str(role.emoji) == ("🔵"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(1039451196571779103)#英文成員
        u_role=b_g.get_member(role.user_id)
        with open ('test.json','r') as sm:
          smile=json.load(sm)
        if smile['idiot'][f'{role.user_id}']!=1:

          embeds=nextcord.Embed(title="大東亞帝國", description="大明王朝Ming dynasty", color=0xe32626)
          embeds.add_field(name="新手須知", value=f"{u_role.mention} Please read <#990714153025040415> to understand server specifications! \n Meanwhile, you can get to know the functions of channels through <#1040720613796491345>.\n If you want to get to know everyone quickly, you can go to <#1039436997145673788>.", inline=False)
          embeds.add_field(name="身分組領取", value="And you can access 18+ areas, or leak information through receiving roles from <#1040720680305557595>.", inline=False)
          embeds.add_field(name="遊戲疑難", value="In addition, if you have any questions about Genshin, you can ask in <#1039437188368179250>. \n If you can’t pass realm or BOSS, you can also post a request in <#1039437236627853332>.", inline=False)
          embeds.set_image("https://upload.cc/i1/2022/11/10/rb6dCB.png")
          w=self.bot.get_channel(978680659428147292) 
          await w.send(embed=embeds)

        with open ('test.json','r') as sm:
          smile=json.load(sm)
        smile['idiot'][f'{role.user_id}']=1
        with open('test.json','w',encoding='utf8') as loli:
          json.dump(smile,loli,indent=2)
        await u_role.add_roles(r_role)
      elif str(role.emoji) == ("🔶"):
        b_g=self.bot.get_guild(role.guild_id)
        cn_role=b_g.get_role(978732220154007613)#中文成員
        en_role=b_g.get_role(1039451196571779103)#英文成員
        u_role=b_g.get_member(role.user_id)
        with open ('test.json','r') as sm:
          smile=json.load(sm)
        if smile['idiot'][f'{role.user_id}']!=1:
          embeds=nextcord.Embed(title="大東亞帝國", description="大明王朝Ming dynasty", color=0xe32626)
          embeds.add_field(name="新手須知", value=f"{u_role.mention} 請詳閱 <#978707952640872548> 以了解伺服器規範！\n 同時可以透過 <#978708014695600188> 熟悉頻道功能，\n 如果想快速認識大家可以到 <#990553527547990046> 。 ", inline=False)
          embeds.add_field(name="身分組領取", value="並且可透過 <#978740632086523914> 開啟色色區或者是內鬼情報區哦！ ", inline=False)
          embeds.add_field(name="遊戲疑難", value="另外有任何遊戲疑問可在 <#978925411494920243>  進行詢問，\n 打不過的秘境或者BOSS也可於 <#978924406745210900>  來發布委託！", inline=False)
          embeds.set_image("https://upload.cc/i1/2022/11/10/rb6dCB.png")
          w=self.bot.get_channel(978680659428147292) 
          await w.send(embed=embeds)   
        b_g=self.bot.get_guild(role.guild_id)
        cn_role=b_g.get_role(978732220154007613)#中文成員
        en_role=b_g.get_role(1039451196571779103)#英文成員
        u_role=b_g.get_member(role.user_id)
        with open ('test.json','r') as sm:
          smile=json.load(sm)
        smile['idiot'][f'{role.user_id}']=1
        with open('test.json','w',encoding='utf8') as loli:
          json.dump(smile,loli,indent=2)
        await u_role.add_roles(cn_role)
        await u_role.add_roles(en_role)

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self,role):
    if role.message_id == 996482471803752560 or role.message_id == 1041245596729741352:
      if str(role.emoji) == ("1️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996416756086222961)#世界等級1
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("2️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996416970314489987)#世界等級2
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("3️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417043140182097)#世界等級3
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("4️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417097620004975)#世界等級4
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("5️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417176099635271)#世界等級5
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("6️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417295834423458)#世界等級6
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("7️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417376725762089)#世界等級7
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("8️⃣"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996417493474230282)#世界等級8
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
    elif role.message_id == 996516544274243615 or role.message_id == 1041246891704328196:
      if str(role.emoji) == ("🇦"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470460407627786)#北美
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🇧"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470641073061939)#歐洲
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🇨"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470572475228270)#亞洲
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🇩"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470702880346182)#台港澳
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
    elif role.message_id == 996519987160293486 or role.message_id == 1041247270236078161:
      if str(role.emoji) == ("📢"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996470792315490326)#重大告知
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🎉"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996471385536860230)#活動告知
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
    elif role.message_id == 996521942859390976 or role.message_id == 1041247328335560725:
      if str(role.emoji) == ("🍏"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996295323829948556)#草
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("⛈️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996295478541041704)#雷
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🚰"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996292486546857995)#水
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🔥"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996294524068429905)#火
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🌬️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996295031424032820)#風
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🧊"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996294699793002547)#冰
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🪨"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(996294895528587355)#岩
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
    elif role.message_id == 996527385543450695 or role.message_id == 1041248333777338368:
      if str(role.emoji) == ("🕶️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(978738302482010193)#紳士
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🕵️"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(978739129405833256)#內鬼
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
    elif role.message_id == 1040718793284001833:
      if str(role.emoji) == ("🔴"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(978732220154007613)#中文成員
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🔵"):
        b_g=self.bot.get_guild(role.guild_id)
        r_role=b_g.get_role(1039451196571779103)#英文成員
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(r_role)
      elif str(role.emoji) == ("🔶"):
        b_g=self.bot.get_guild(role.guild_id)
        cn_role=b_g.get_role(978732220154007613)#中文成員
        en_role=b_g.get_role(1039451196571779103)#英文成員
        u_role=b_g.get_member(role.user_id)
        await u_role.remove_roles(cn_role)
        await u_role.remove_roles(en_role)
        



def setup(bot):
    bot.add_cog(role(bot))