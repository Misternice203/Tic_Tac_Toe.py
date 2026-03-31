WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6),
]

class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def display(self):
        b = [str(i+1) if c == " " else c for i, c in enumerate(self.cells)]
        print()
        print(f" {b[0]} | {b[1]} | {b[2]} ")
        print("---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]} ")
        print("---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]} ")

    def place(self, position: int, mark: str) -> bool:
        if not 1 <= position <= 9:
            raise ValueError("Position must be between 1 and 9.")
        i = position - 1
        if self.cells[i] != " ":
            return False
        self.cells[i] = mark
        return True

    def check_winner(self, mark: str) -> bool:
        return any(all(self.cells[i] == mark for i in line) for line in WIN_LINES)

    def check_draw(self) -> bool:
        return all(c != " " for c in self.cells)
