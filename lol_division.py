import json
import discord
import requests
import tokenn
import lol_champs
import imagegenerator


class LolDiv():
    def __init__(self, message):
        self.message = message
        self.gen_div = imagegenerator.DivisionGenerator()
        self.lol_champs = lol_champs.ChampsR(message)
        self.unranked_sq = False
        self.unranked_flex = False
        self.user_exist = True

    def get_user_id(self, summoner_name, server):
        self.user_api = requests.get(f'https://{server}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={tokenn.riot_api}')
        self.user_id_json = self.user_api.json()
        self.server = server
        try:
            self.user_id = self.user_id_json['id']

        except KeyError:
            self.user_exist = False

        else:
            self.user_name = self.user_id_json['name']
            print(self.user_id_json)

    def get_user_div_soloq(self):
        self.div_api_sq = requests.get(f'https://{self.server}.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.user_id}?api_key={tokenn.riot_api}')
        self.div_json_sq = self.div_api_sq.json()

        try:
            self.div_list_sq = self.div_json_sq[0]

        except IndexError:
            self.unranked_sq = True

        else:
            self.variables_sq()
            self._winratio_sq()

    def get_user_div_flex(self):
        self.div_api_flex = requests.get(f'https://{self.server}.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.user_id}?api_key={tokenn.riot_api}')
        self.div_json_flex = self.div_api_flex.json()

        try:
            self.div_list_flex = self.div_json_flex[1]

        except IndexError:
            self.unranked_flex = True

        else:
            self.variables_flex()
            self._winratio_flex()

    def get_user_mastery(self):
        self.mastery_api = requests.get(f'https://{self.server}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{self.user_id}?api_key={tokenn.riot_api}')
        self.mastery_json = self.mastery_api.json()
        self.mastery_1 = self.mastery_json[0]
        self.mastery_2 = self.mastery_json[1]
        self.mastery_3 = self.mastery_json[2]

    def variables_sq(self):
        self.div_win_sq = self.div_list_sq['wins']
        self.div_lose_sq = self.div_list_sq['losses']
        self.div_lp_sq = self.div_list_sq['leaguePoints']
        self.div_tier_sq = self.div_list_sq['tier']
        self.div_rank_sq = self.div_list_sq['rank']

    def variables_flex(self):
        self.div_win_flex = self.div_list_flex['wins']
        self.div_lose_flex = self.div_list_flex['losses']
        self.div_lp_flex = str(self.div_list_flex['leaguePoints'])
        self.div_tier_flex = self.div_list_flex['tier']
        self.div_rank_flex = self.div_list_flex['rank']

    def _winratio_sq(self):
        # Winratio
        self.all_games_sq = self.div_lose_sq + self.div_win_sq
        self.winratio_float_sq = (self.div_win_sq / self.all_games_sq) * 100
        self.winratio_round_sq = round(self.winratio_float_sq, 0)
        self.winratio_str_sq = str(self.winratio_round_sq)
        self.winratio_list_sq = self.winratio_str_sq.split('.')
        self.winratio_sq = self.winratio_list_sq[0]

    def _winratio_flex(self):
        # Winratio
        self.all_games_flex = self.div_lose_flex + self.div_win_flex
        self.winratio_float_flex = (self.div_win_flex / self.all_games_flex) * 100
        self.winratio_round_flex = round(self.winratio_float_flex, 0)
        self.winratio_str_flex = str(self.winratio_round_flex)
        self.winratio_list_flex = self.winratio_str_flex.split('.')
        self.winratio_flex = self.winratio_list_flex[0]

    async def send_rank(self, message):
        if self.unranked_sq == True and self.unranked_flex == True:
            self.gen_div.generator('Unranked', '0', '', '0',
                                   'Unranked', '0', '', '0',
                                   self.user_name)

            await message.channel.send(file=discord.File('data1/ready.png'))

        elif self.user_exist == False:
            await message.channel.send(f'Nie znaleziono podanego użytkownika!')

        elif self.unranked_sq == True:
            self.gen_div.generator('Unranked', '0', '', '0',
                                   self.div_tier_flex, self.div_lp_flex,self.div_rank_flex, self.winratio_flex,
                                   self.user_name)

            await message.channel.send(file=discord.File('data1/ready.png'))

        elif self.unranked_flex == True:
            self.gen_div.generator(self.div_tier_sq, self.div_lp_sq,self.div_rank_sq, self.winratio_sq,
                                   'Unranked', '0','', '0',
                                   self.user_name)

            await message.channel.send(file=discord.File('data1/ready.png'))

        else:
            self.gen_div.generator(self.div_tier_sq, self.div_lp_sq,self.div_rank_sq, self.winratio_sq,
                                   self.div_tier_flex, self.div_lp_flex,self.div_rank_flex, self.winratio_flex,
                                   self.user_name)

            await message.channel.send(file=discord.File('data1/ready.png'))



