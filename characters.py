# import random


class Character:
    def __init__(self, align, player_info, leader=False):
        self.alignment = align
        self.leader = leader
        self.player_number = player_info['number']
        self.player_id = player_info['dicord_id']
        self.player_name = player_info['name']
        self.team_vote = None
        self.quest_vote = None
        self.assassin = False
        self.merlin = False

    # def assassinate(self, assassin, players_qty):
    #     assassinated_player = random.sample(range(players_qty), 1)
    #     return assassinated_player
