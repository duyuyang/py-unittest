import json
import requests

class Buyahouse(object):
    def get_next_house(self, user):
        house = self.get_random_house('sydney')
        while house in user['house_seen']:
            house = self.get_random_house('melbourne')
        return house

    def get_random_house(self, city):
        pass


    def evaluate(self, houses):
        for house in houses:
            r = requests.get('http://realestate.com/%s' % house)
            info = self.get_house_info(r.text)
            if house_is_undervalued(info):
                if under_budget(info):
                    self.send_email(house, info)
                else:
                    self.add_to_watch_list(house)




    def get_json(self, filename):
        try:
            return json.loads(open(filename).read())
        except (IOError, ValueError):
            return "Error"
