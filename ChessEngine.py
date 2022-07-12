"""
Shranjevanje informacij glede trenutne igre in ugotavljanje moznih veljavnih potez,
shranjuje se move log.
"""

class GameState():
    def __init__(self):
        #8x8 2d list, vsaka dva znaka predstavljata figuro, prva crka
        #predstavlja barvo, druga tip figure, dve crti pa pomenita prazno 
        #mesto na sahovnici
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "bR"],            
        ]

        self.whiteToMove = True
        self.moveLog = []

