import curses

from util import MIN_SCREEN_HEIGHT, MIN_SCREEN_WIDTH, GameState
from tiles import Tiles

class Game:
    def __init__(self):
        self.tiles = Tiles()
        self.tiles.add_tile()
        self.gamescreen_before = self.tiles.get_game_screen()
        self.gamescreen_after = self.tiles.get_game_screen()
        self.screen = None
    
    def _refresh_screen(self):
        if self.screen is not None:
            self.screen.erase()
            for (y, line) in enumerate(self.tiles.get_game_screen()):
                self.screen.addstr(y, 0, line)
    
    def _interact(self):
        key = self.screen.getkey()

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

    def __call__(self, stdscr):
        assert curses.LINES >= MIN_SCREEN_HEIGHT, "Screen not high enough"
        assert curses.COLS >= MIN_SCREEN_WIDTH, "Screen not wide enough"
        
        self.screen = stdscr

        while self.tiles.state == GameState.RUNNING:
            if self.gamescreen_before != self.gamescreen_after:
                self.tiles.add_tile()

            self.gamescreen_before = self.tiles.get_game_screen()
            self._refresh_screen()
            self._interact()
            self.tiles.check_finished()
            self.gamescreen_after = self.tiles.get_game_screen()
        
        return self.tiles.get_score()


if __name__ == "__main__":
    game = Game()
    score = curses.wrapper(game)
    print(f"Final Score: {score}")
    