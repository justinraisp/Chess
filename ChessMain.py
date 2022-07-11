from chess import piece_name
import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

#Global dictionary of images, called only once
def loadImages():
    pieces = ["wP","wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK",]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE,SQ_SIZE))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    

    