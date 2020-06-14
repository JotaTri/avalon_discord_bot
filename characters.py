import random
class characters:
    def __init__(self,align,player_id,player_name,lead = False):    
        self.alignment = align
        self.leader = lead
        self.player_id = player_id
        self.player_name = player_name
        self.team_vote = False
        self.quest_vote = True
        self.assassin = False
        self.merlin = False

    def assassinate(self,assassin,players_qty):
        assassinated_player = random.sample(range(players_qty), 1)
        
        return assassinated_player