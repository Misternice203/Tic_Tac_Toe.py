from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.p1 = Player("X")
        self.p2 = Player("O")
        self.current = self.p1

    def _ask_position(self) -> int:
        while True:
            raw = input(f"{self.current.name} ({self.current.mark}), choose a position (1-9): ").strip()
            if raw.isdigit() and 1 <= int(raw) <= 9:
                return int(raw)
            print("Please enter a number from 1 to 9.")

    def play_again(self) -> bool:
            while True:
                again = input("\nPlay again? (y/n): ").strip().lower()
                if again in ("y", "yes"):
                    return True
                if again in ("n", "no"):
                    return False
                print("\nPlease enter 'yes' or 'no'\n")

    def play(self):
        while True:
            self.board = Board()
            self.current = self.p1
            while True:
                self.board.display()
                pos = self._ask_position()
                if not self.board.place(pos, self.current.mark):
                    print("\nThat position is already taken.")
                    continue

                if self.board.check_winner(self.current.mark):
                    self.board.display()
                    print(f"\n{self.current.name} ({self.current.mark}) wins! 🏆\n")
                    break
                
                if self.board.check_draw():
                    self.board.display()
                    print("\nIt's a draw! 🤝\n")
                    break

                self.current = self.p2 if self.current == self.p1 else self.p1

            if not self.play_again():
                print("Thank you for playing!!")
                break
            
            
