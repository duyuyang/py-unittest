import json

class Application(object):
    def get_next_team(self, user):
        team = self.get_random_team('sydney')
        while team in user['team_seen']:
            team = self.get_random_team('melbourne')
        return team

    def get_random_team(self, city):
        pass


    def evaluate(self, team1, team2):




    def get_json(self, filename):
        try:
            return json.loads(open(filename).read())
        except (IOError, ValueError):
            return "Error"
