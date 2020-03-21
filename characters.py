class characters:
    def __init__(self,align,player,lead = False):    
        self.alignment = align
        self.leader = lead
        self.player_number = player
        self.team_vote = False
        self.quest_vote = True
        self.assassin = False
        self.merlin = False