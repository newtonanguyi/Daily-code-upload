class Athlete:
    def __init__(self, name, sport, ranking):
        self.name = name
        self.sport = sport
        self.ranking = ranking

class Competition:
    def __init__(self, competition_name, date):
        self.competition_name = competition_name
        self.date = date
        self.athletes = []

    def register_athlete(self, athlete):
        if athlete.name in self.athletes:
            print(f"The athlete {athlete.name} is already in the competition.")
        else:
            self.athletes.append(athlete)
            print(f"The athlete {athlete.name} has been added to the competition.")

    def remove_athlete(self, athlete):
        if athlete.name in self.athletes:
            print(f"Cannot remove the athlete {athlete.name} because they are not part of the competition.")
        else:
            self.athletes.remove(athlete)
            print(f"The athlete {athlete.name} has been removed from the competition.")

    def display_competition_details(self):
        print(f"Competition Name: {self.competition_name}\nCompetition Date: {self.date}")
        
        for i in self.athletes:
            print(f"Participants: {i.name}")  
                

ath1 = Athlete('John', 'Football', 5)
ath2 = Athlete('Mark', 'Basketball', 4.3)
ath3 = Athlete('Casey', 'Tennis', 3.8)

comp  = Competition('Premier League', '2024-12-2')

comp.register_athlete(ath1)
comp.register_athlete(ath3)

comp.remove_athlete(ath3)


comp.display_competition_details()
comp.register_athlete(ath3)

comp.display_competition_details()

comp.register_athlete(ath2)

comp.display_competition_details()
