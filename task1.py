
import requests

TOKEN = 2619421814940190

class SuperHero():
    def __init__(self, token):
        self.base_url = f'https://superheroapi.com/api/{token}'

    def get_character_id(self, charecter):
        charecter_url = f'{self.base_url}/search/{charecter}'
        response = requests.get(charecter_url, timeout = 5).json()
        if response["response"] == "success":
            return response['results'][0]['id']
        else:
            return '0'

    def get_powerstats(self, id):
        powerstats_url = f'{self.base_url}/{id}/powerstats'
        response = requests.get(powerstats_url, timeout=5)
        return response.json()

    def compare_intelligence(self, *charecters):
        intelligence_charecters = {'0': []}
        for charecter in charecters:
            charecter_id = self.get_character_id(str(charecter))
            charecter_powerstats = self.get_powerstats(charecter_id)
            if charecter_powerstats["response"] == "error":
                print(charecter_powerstats["error"], charecter_id)
                continue
            for max_intelligence in intelligence_charecters:
                if int(max_intelligence) < int(charecter_powerstats["intelligence"]):
                    intelligence_charecters = {charecter_powerstats["intelligence"]: charecter_powerstats["name"]}
                elif int(max_intelligence) == int(charecter_powerstats["intelligence"]):
                    intelligence_charecters[charecter_powerstats["intelligence"]].append(charecter_powerstats["name"])
        return intelligence_charecters


if __name__ == '__main__':
    sh = SuperHero(TOKEN)
    intelligence_hero = sh.compare_intelligence('Hulk', 'Captain America', 'Thanos')
    intelligence = [intelligence for intelligence in intelligence_hero.keys()][0]
    print(f'Самый умный герой {intelligence_hero[intelligence]}, его интелект равен {intelligence}')
