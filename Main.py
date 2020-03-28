from GameFiles.Game import Game

'''The main file which is run.'''

if __name__ == "__main__":
    game = Game("Snake GameFiles", 600, 600, "data/apple.png", "data/snakehead.png")
    # game.main_loop(True, False)
    game.game_loop()