
from piece import Piece
import pygame as pg

class Player():

    square_size = (51, 51)


    def __init__(self, player):
        self.player = player
        self.pawns = []
        self.number_holder = 0

        #setup för alla pjäser

        if self.player == 1:
            self.pawn_position = 6
            self.rest_position = 7
            self.pawn_url = 'src/w_pawn_1x.png' 
            self.rook_url = 'src/w_rook_1x.png' 
            self.knight_url = 'src/w_knight_1x.png' 
            self.bishop_url = 'src/w_bishop_1x.png' 
            self.king_url = 'src/w_king_1x.png' 
            self.queen_url = 'src/w_queen_1x.png'
        else:
            self.pawn_position = 1
            self.rest_position = 0
            self.pawn_url = 'src/b_pawn_1x.png' 
            self.rook_url = 'src/b_rook_1x.png' 
            self.knight_url = 'src/b_knight_1x.png' 
            self.bishop_url = 'src/b_bishop_1x.png' 
            self.king_url = 'src/b_king_1x.png' 
            self.queen_url = 'src/b_queen_1x.png'





        for i in range(8):
            self.pawns.append(Piece("Bonde", [i,self.pawn_position], pg.transform.scale(pg.image.load(self.pawn_url), self.square_size)))
        for i in range(2):
            self.pawns.append(Piece("Vakttorn", [i*7,self.rest_position], pg.transform.scale(pg.image.load(self.rook_url), self.square_size)))
        number_holder = 1
        for i in range(2):
            self.pawns.append(Piece("Ryttare", [number_holder,self.rest_position], pg.transform.scale(pg.image.load(self.knight_url), self.square_size)))
            number_holder = 6
        number_holder = 2
        for i in range(2):
            self.pawns.append(Piece("Biskop", [number_holder, self.rest_position], pg.transform.scale(pg.image.load(self.bishop_url), self.square_size)))
            number_holder = 5
        self.pawns.append(Piece("Kung", [3, self.rest_position], pg.transform.scale(pg.image.load(self.king_url), self.square_size)))
        self.pawns.append(Piece("Drottning", [4, self.rest_position], pg.transform.scale(pg.image.load(self.queen_url), self.square_size)))        

    def get_grid_pos(self, number):
        return self.pawns[number].grid_position
    def get_surface(self, number):
        return self.pawns[number].surface
