class Player:
    def __init__(self, mark: str):
        self.mark = mark
        self.name = input(f"Player selecting {mark}, enter your name: ").strip() or f"Player {mark}"
