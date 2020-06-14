import random


class characters:
    def __init__(self, align, player_list, lead=False):
        self.alignment = align
        self.leader = lead
        self.player_number = player_list[0]
        self.player_id = player_list[1]
        self.player_name = player_list[2]
        self.team_vote = False
        self.quest_vote = True
        self.assassin = False
        self.merlin = False

    def assassinate(self, assassin, players_qty):
        assassinated_player = random.sample(range(players_qty), 1)

        return assassinated_player
