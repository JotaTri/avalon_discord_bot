import numpy as np
import random
from random import randrange

class game:
    def __init__(self,players_qty):
        self.players_qty = players_qty        
        self.player_distribution = np.array([[5,6,7,8,9,10],[3,4,4,5,6,6],[2,2,3,3,3,4]])
        player_col = np.where(self.player_distribution[0] == players_qty)
        self.good_qty = int(self.player_distribution[1][player_col])
        self.bad_qty = self.good_qty = int(self.player_distribution[2][player_col])
        players = []
        alignment_array = np.ones(players_qty)
        alignment_array[:self.bad_qty] = 0
        np.random.shuffle(alignment_array)
        for i in range(total_players):
            players.append(characters(bool(alignment_array[i]),i+1))
        self.char = players
       
    def quests(self):
        game_quests = quests(self.players_qty,self.char)
        for q in range(5):           
            self.game_end,self.game_winner = game_quests.quest_turns(q)

class characters:
    def __init__(self,align,player,lead = False):    
        self.alignment = align
        self.leader = lead
        self.player_number = player
        self.team_vote = False

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
            turn = turn_actions(t,self.players_qty,self.char)
            self.quest_turn = turn.turn_number
    
        end = True
        return end, False

class turn_actions:
    def __init__(self,t,players,characters):
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
                    self.char[i+1].leader == True
                    self.lead_number = i+1
                    break
    
    def build_team(self,size):
        group_players = random.sample(range(6), size)
        
        
    def turn_voting(self,team):
        votes = []
        for j in range(self.players_qty):
            votes.append(self.char[j].team_vote)
        
        if np.sum(votes) >= self.players_qty:
            team_approval = True
        else:
            team_approval = False
        
        return team_approval      

total_players = 6 
jogo = game(total_players)
jogo.quests()      