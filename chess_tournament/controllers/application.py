"""Get tournament initialization details from User

"""

from .tournament_manager import TournamentManager
from .menu_manager import MenuManager
from .player_manager import PlayerManager
from models import Round, Tournament


class Application:
    tm = TournamentManager
    mm = MenuManager
    pm = PlayerManager

    def generate_round(players):
        new_round = Round()
        first_players = [p for i, p in enumerate(players) if i % 2 != 0]
        second_players = [p for i, p in enumerate(players) if i % 2 == 0]
        paired_players = zip(first_players, second_players)

        for p1, p2 in list(paired_players):
            new_round.create_game(p1, p2)

        print("Round created with the following games: ")
        for game in new_round.games:
            print(game)

        input("Press ENTER to continue...\n")
