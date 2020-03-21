import numpy as np
import random
from turn_actions import turn_actions

class quests:
    def __init__(self,players,characters): 
        self.char = characters
        self.players_qty = players
        self.quests_details = np.array([[5,6,7,8,9,10],[2,2,2,3,3,3],[3,3,3,4,4,4],
                              [2,4,3,4,4,4],[3,3,4,5,5,5],[3,4,4,5,5,5]])
        self.quests_col = np.where(self.quests_details[0] == self.players_qty)
        
    def quest_turns(self,q_number):
        self.quest_number = q_number + 1
        self.team_size = int(self.quests_details[self.quest_number][self.quests_col])
        for t in range(5):
            end = False
            act = turn_actions(t,self.players_qty,self.char)
            self.quest_turn = act.turn_number
            group = act.build_team(self.team_size)
            ap = act.turn_voting(group)
            
            if ap:  
                break
            
            else: 
                end = True
        
        return [end, False], group
    
    def quest_votes(self,quest_group):
        quest_success = True
        for c in quest_group:
            self.char[c].quest_vote = bool(random.getrandbits(1))            
            if self.char[c].alignment:
                self.char[c].quest_vote = True
            quest_success = (quest_success and self.char[c].quest_vote)

        return quest_success