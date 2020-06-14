import numpy as np
import random


class turn_actions:
    def __init__(self, t, players, characters):
        self.char = characters
        self.players_qty = players
        self.turn_number = t + 1
        for i in range(self.players_qty):
            if self.char[i].leader == True:
                self.char[i].leader == False
                if i == (self.players_qty - 1):
                    self.char[0].leader == True
                    self.lead_number = 0
                    break
                else:
                    self.char[i + 1].leader == True
                    self.lead_number = i + 1
                    break

    def build_team(self, size):
        group_players = random.sample(range(self.players_qty), size)

        return group_players

    def turn_voting(self, team):
        print("Voting")
        votes = []
        for j in range(self.players_qty):
            self.char[j].team_vote = bool(random.getrandbits(1))
            votes.append(self.char[j].team_vote)
        if np.sum(votes) >= self.players_qty / 2:
            team_approval = True
        else:
            team_approval = False

        print("Approved: ", team_approval)
        return team_approval
