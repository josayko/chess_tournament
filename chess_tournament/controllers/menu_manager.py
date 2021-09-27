"""Menu management

"""


class MenuManager:
    @staticmethod
    def main_menu():
        """Tournament monitoring dashboard"""
        while True:
            print("+========== Dashboard ===========+\n")
            print("    [ 1 ] Create a new tournament")
            print("    [ 2 ] Create a new player")
            print("    [ 3 ] Register player to tournament")
            print()
            print("    [ 4 ] Generate round")
            print("    [ 5 ] Add results")
            print()
            print("    [ 6 ] Tournament results")
            print("    [ 7 ] Player list")
            print()
            print("    [ 0 ] Quit\n")
            print("+================================+\n")
            select = input("Select ? (0 - 5) ")
            print()
            try:
                val = int(select)
                return val
            except ValueError:
                print("*** Error: invalid input ***")
                input("Press ENTER to continue...")
                continue
