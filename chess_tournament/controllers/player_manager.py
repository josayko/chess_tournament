"""Player Manager

"""

from controllers import App
from models import Player


class PlayerManager:
    def select_player_error(index):
        """Checks user input when player selection"""
        try:
            index = int(index) - 1
            if index < -1 or index >= len(App.players):
                return True
        except ValueError:
            return True
        return False

    def no_players():
        """Checks if players list is empty"""
        if not App.players:
            return True
        return False

    def create_error(surname, name, rank):
        """Checks user input errors when create new player"""
        if len(surname) < 2:
            return "surname input must be more than 1 character"
        elif len(name) < 2:
            return "name input must be more than 1 character"
        try:
            rank = int(rank)
            if rank <= 0:
                return "rank input is invalid"
        except ValueError:
            return "rank input is invalid"
        return None

    def create_player(input, dirname):
        """Create a new local player and save to db"""
        new_player = Player(
            0,
            input['surname'],
            input['name'],
            input['birthdate'],
            input['gender'],
            input['rank'],
        )
        new_player.id = new_player.save_player_to_db(dirname)
        App.players.append(new_player)
        return
