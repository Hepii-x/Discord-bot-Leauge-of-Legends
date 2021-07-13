import random
import json

import requests

adc = ['aphelios','ashe','caitlyn','draven','ezreal',
       'jhin','jinx',"kai'sa",'kalista',"kog'maw",
       'lucian','miss fortune','samira','sivir',
       'tristana','twitch','varus','vayne','xayah']

jg = ['amumu','diana','ekko','elise','evelynn',
      'fiddlesticks','gragas','graves','hecarim',
      'jarvan IV','karthus','kayn',"kha'zix",'kindred',
      'lee sin','lillia','master yi','nidalee',
      'nocturne','nunu & willump','olaf','rammus',
      "rek'sai",'rengar','sejuani','shaco','shyvana',
      'trundle','udyr','vi','viego','volibear','warwick',
      'xin zhao','zac','skarner','ivern']

top = ['aatrox','camille',"cho'gath",'darius','dr. mundo',
       'fiora','gangplank','garen','gnar','irelia','jax',
       'jayce','kayle','kennen','kled','malphite','maokai',
       'mordekaiser','nasus','ornn','poppy','quinn','sett',
       'shen','singed','sion','teemo','tryndamere','urgot',
       'vladimir','volibear','wukong','yasuo','yone','gwen',
       'illaoi','riven','yorick','rumble','renekton']

mid = ['ahri','akali','anivia','annie','brand','cassiopeia',
       'corki','diana','ekko','galio','heimerdinger','karma',
       'malzahar','orianna','qiyana','ryze','swain','sylas',
       'syndra','talon','twisted fate','veigar',"vel'koz",
       'viktor','vladimir','xerath','yasuo','yone','zed',
       'ziggs','zoe','neeko','taliyah','aurelion sol',
       'azir','lissandra','fizz']

supp = ['alistar','bard','blitzcrank','brand','braum','galio',
        'janna','karma','leona','lulu','lux','morgana','nami',
        'nautilus','pantheon','pyke','rakan','senna','sona',
        'soraka','tahm kench','taric','thresh','zilean','zyra',
        'rell','seraphine','yuumi']

champions_id = {}

class ChampsR():
    def __init__(self, message):
        self.message = message

    async def r_mid(self, message):
        champ = random.choice(mid)

        if champ == "vel'koz":
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Velkoz_0.jpg')

        elif champ == 'twisted fate':
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/TwistedFate_0.jpg')

        elif champ == 'aurelion sol':
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/AurelionSol_0.jpg')

        else:
            await message.channel.send(champ.title())
            await message.channel.send(
                f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champ.title()}_0.jpg')

    async def r_supp(self, message):
        champ = random.choice(supp)

        if champ == 'tahm kench':
            await message.channel.send(champ.title())
            await message.channel.send(
                'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/TahmKench_0.jpg')

        else:
            await message.channel.send(champ.title())
            await message.channel.send(
                f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champ.title()}_0.jpg')

    async def r_jg(self, message):
        champ = random.choice(jg)

        if champ == "kha'zix":
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Khazix_0.jpg')

        elif champ == "rek'sai":
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/RekSai_0.jpg')

        elif champ == 'jarvan IV':
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/JarvanIV_0.jpg')

        elif champ == 'lee sin':
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/LeeSin_0.jpg')

        elif champ == 'master yi':
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MasterYi_0.jpg')

        elif champ == 'nunu & willump':
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nunu_0.jpg')

        elif champ == 'xin zhao':
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/XinZhao_0.jpg')

        else:
            await message.channel.send(champ.title())
            await message.channel.send(
                f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champ.title()}_0.jpg')

    async def r_top(self, message):
        champ = random.choice(top)

        if champ == "cho'gath":
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Chogath_0.jpg')

        elif champ == 'dr. mundo':
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/DrMundo_0.jpg')

        else:
            await message.channel.send(champ.title())
            await message.channel.send(
                f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champ.title()}_0.jpg')

    async def r_adc(self, message):
        champ = random.choice(adc)

        if champ == "kog'maw":
            await message.channel.send(champ.title())
            await message.channel.send(f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/KogMaw_0.jpg')

        elif champ == "kai'sa":
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kaisa_0.jpg')

        elif champ == 'miss fortune':
            await message.channel.send(champ.title())
            await message.channel.send('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MissFortune_0.jpg')

        else:
            await message.channel.send(champ.title())
            await message.channel.send(
                f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champ.title()}_0.jpg')

    async def all_champs(self, message):
        champions = ''
        all_champs = adc + mid + top + jg + supp
        all_champs_sort = sorted(all_champs)

        for champ in all_champs_sort:
            champions += f'- {champ.title()}\n'

        await message.channel.send(champions)

    def champs_id(self):
        self.ver = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
        self.ver = self.ver.json()
        self.ver = self.ver[0]
        self.champ_id_api = requests.get(f'https://ddragon.leagueoflegends.com/cdn/{self.ver}/data/en_US/champion.json')
        self.champ_id_json = self.champ_id_api.json()
        for value in self.champ_id_json['data'].items():
            valu = value[1]
            self.champ_id = valu['key']
            self.champ_id_name = valu['id']
            champions_id[self.champ_id] = self.champ_id_name









