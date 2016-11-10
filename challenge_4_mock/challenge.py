import json
import requests

class Buyahouse(object):
    def get_next_house(self, user):
        house = self.get_random_house('sydney')
        while house in user['house_seen']:
            house = self.get_random_house('melbourne')
        return house


    def evaluate(self, houses, budget):
        if len(houses) == 0:
            raise Exception("Nothing Available!")
        for house in houses:
            try:
                r = requests.get('http://realestate.com/%s' % house)
            except ConnectionError:
                return 'Boom!'
            info = self.get_house_info(r.text)
            if self.house_is_undervalued(info):
                if self.get_price(info) < budget:
                    self.send_email(house, info)
                else:
                    self.add_to_watch_list(house)



    def get_json(self, filename):
        try:
            return json.loads(open(filename).read())
        except (IOError, ValueError):
            return "Error"


    def get_house_info(self, text):
        pass

    def house_is_undervalued(self, info):
        pass

    def get_price(self, info):
        pass

    def send_email(self, house, info):
        pass

    def add_to_watch_list(self, house):
        pass

    def get_random_house(self, city):
        pass
