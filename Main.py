from Game import Game


if __name__ == "__main__":
    game = Game("Snake Game", 600, 600, "data/apple.png", "data/snakehead.png")
    game.main_loop()