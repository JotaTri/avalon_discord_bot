import numpy as np
import random
from characters import characters
from quests import quests


class game:
    def __init__(self):
        self.players_info = {}
        self.players_info["discord_id"] = []
        self.players_info["name"] = []

    def join_game(self, info):
        self.players_info["discord_id"].append(info["discord_id"])
        self.players_info["name"].append(info["discord_name"])

    def shuffle_players(self):
        self.players_qty = len(self.players_info["discord_id"])
        self.player_distribution = np.array(
            [[5, 6, 7, 8, 9, 10], [3, 4, 4, 5, 6, 6], [2, 2, 3, 3, 3, 4]]
        )
        player_col = np.where(self.player_distribution[0] == self.players_qty)
        self.good_qty = int(self.player_distribution[1][player_col])
        self.bad_qty = self.good_qty = int(self.player_distribution[2][player_col])
        players = []
        alignment_array = np.ones(self.players_qty)
        alignment_array[: self.bad_qty] = 0
        np.random.shuffle(alignment_array)
        for i in range(self.players_qty):
            players.append(
                characters(
                    bool(alignment_array[i]), [i + 1, self.players_info["discord_id"][i], self.players_info["name"][i]]
                )
            )
        roles = random.sample(range(self.players_qty), 2)
        self.merlin_player = roles[0]
        self.assassin_player = roles[1]
        players[roles[0]].assassin = True
        players[roles[1]].merlin = True
        self.char = players
        print("O Merlin é o jogador: ", self.char[roles[1]].player_number)
        print("O Assassino é o jogador: ", self.char[roles[0]].player_number)

    def get_character(self, discord_id):
        for character in self.char:
            if (character.player_id == discord_id):
                return character

        return "Player does not exist"

    def init_quests(self):
        game_quests = quests(self.players_qty, self.char)
        self.quests_results = []
        for q in range(5):
            print("Quest number: ", (q + 1))
            self.game_status, self.quest_group = game_quests.quest_turns(q)
            if not (self.game_status[0]):
                self.quests_results.append(game_quests.quest_votes(self.quest_group))
                print("Quest Result: ", self.quests_results[q])

            else:
                pass

            if sum(self.quests_results) > 2:
                self.game_status = [True, True]
                assassinated = int(
                    self.char[self.assassin_player].assassinate(
                        self.assassin_player, self.players_qty
                    )
                )
                print("Jogador assassinado: ", str(assassinated))
                if int(assassinated) == self.merlin_player:
                    self.game_status = [True, False]

            elif sum(self.quests_results) < (q - 2):
                self.game_status = [True, False]

            if self.game_status[0]:
                print(
                    "Jogo acabou no turno: ",
                    q + 1,
                    ", vencedores: ",
                    self.game_status[1],
                )
                break

            else:
                pass
