import sys
sys.stdout.write('Ronaldinho')
import numpy as np
import random

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
       
    def init_quests(self):
        game_quests = quests(self.players_qty,self.char)
        self.quests_results = []
        for q in range(5):
            print('Quest number: ', (q + 1))
            self.game_status,self.quest_group = game_quests.quest_turns(q)            
            if not(self.game_status[0]):
                self.quests_results.append(game_quests.quest_votes(self.quest_group))
                print('Quest Result: ',self.quests_results[q])
                
            else:
                pass
            
            if sum(self.quests_results) > 2:
                self.game_status = [True,True]
            
            elif (sum(self.quests_results) < (q - 2)):
                self.game_status = [True,False]
            
            if self.game_status[0]:
                print('Jogo acabou no turno: ',q, ', vencedores: ',self.game_status[1])
                break
            
            else:
                pass

class characters:
    def __init__(self,align,player,lead = False):    
        self.alignment = align
        self.leader = lead
        self.player_number = player
        self.team_vote = False
        self.quest_vote = True
 
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
        
        return  group_players
        
        
    def turn_voting(self,team):
        print('Voting')
        votes = []
        for j in range(self.players_qty):
            self.char[j].team_vote = bool(random.getrandbits(1)) 
            votes.append(self.char[j].team_vote)
        if (np.sum(votes) >= self.players_qty/2):
            team_approval = True
        else:
            team_approval = False
            
        print('Approved: ',team_approval)
        return team_approval    
 

total_players = 6 
jogo = game(total_players)
jogo.init_quests()    