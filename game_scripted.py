import curses

from game import Game
from util import GameState

class GameScripted(Game):
    def __init__(self, strategy):
        super().__init__()
        self.strategy = strategy
        self.counter = 0

    def _interact(self):
        assert self.counter < len(self.strategy), "Strategy finished"
        key = self.strategy[self.counter]
        self.counter += 1

        if key in ["a", "KEY_LEFT"]:
            self.tiles.left()
        
        if key in ["d", "KEY_RIGHT"]:
            self.tiles.right()

        if key in ["w", "KEY_UP"]:
            self.tiles.up()
        
        if key in ["s", "KEY_DOWN"]:
            self.tiles.down()
        
        if key == "q":
            self.tiles.state = GameState.FINISHED
    
    def _refresh_screen(self):
        pass


if __name__ == "__main__":
    strategy = ["KEY_LEFT","KEY_DOWN","KEY_RIGHT","KEY_UP"] * 10000 + ["q"]
    scores = []
    for _ in range(100):
        game = GameScripted(strategy)
        score = curses.wrapper(game)
        scores += [score]
    print(f"Max Score:  {max(scores):>5}")
    print(f"Mean Score: {round(sum(scores)/len(scores)):>5}")