class Player:
    def __init__(self, name, team, position):
        self.name = name
        self.team = team
        self.position = position

class Game:
    def __init__(self, game_date, location):
        self.game_date = game_date
        self.location = location
        self.teams = []
        self.team_scores = {}

    def add_team(self, team_name):
        if team_name in self.teams:
            print(f"The team '{team_name}' has already been added.")
        else:
            self.team_scores[team_name] = 0
            self.teams.append(team_name)
            print(f"The team '{team_name}' has been added.")

    def record_score(self, team_name, score):
        if team_name in self.teams:         
            self.team_scores[team_name] += score 
            print(f"The team '{team_name}' has earned '{score}' points\nThe team '{team_name}' now has a total of '{self.team_scores[team_name]}' points")
        else:
            print(f"Cannot record the scores for '{team_name}' because they are not in the league.")


game = Game('2024-21-12', 'Etihad stadium')

game.add_team('Man City')
game.add_team('Aston Villa')

game.record_score('Man City', 28)
game.record_score('Aston Villa', 12)
game.record_score('Aston Villa', 20)
game.record_score('Man City', 2)
game.record_score('Man City', 10)
