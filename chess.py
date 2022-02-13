import pygame as pg
import sys
from player import Player

pg.init()

SIZE = width, height = 640,640

#Basic colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)



grid_size = 8
x, y = 50, 50
square_size = (51,51)

chess_board_img = [pg.transform.scale(pg.image.load("src/square brown light_1x.png"), square_size), 
                pg.transform.scale(pg.image.load("src/square brown dark_1x.png"), square_size)]

board_border = 120
x, y = 50, 50
screen = pg.display.set_mode(SIZE)

#Formel jag vill göra mer tillgänglig i hela projektet: 
# ( (x*j)+board_border , (y*i) + board_border)
# x = 50, i och j är grid positioner, + board_vorder vilket ser till att det blir en border runt bordet.
def get_grid_position(grid_pos):
    grid_pos[0] = max(0, min(grid_pos[0], 7))
    grid_pos[1] = max(0, min(grid_pos[1], 7))
    

    return [(x*grid_pos[0])+board_border, (y*grid_pos[1])+board_border]

player_one = Player(1)
player_two = Player(2)
    

def draw_board():

    #makes sure i get right color on right place
    color = 0
    #Draw chess board
    for i in range(grid_size):
        for j in range(grid_size):
            screen.blit(chess_board_img[color], ( (x*j)+board_border , (y*i) + board_border))       
            color = 1 if color == 0 else color == 0      
        color = 1 if color == 0 else color == 0


font = pg.font.Font('src/Oswald-VariableFont_wght.ttf', 32)

# create a text surface object,
# on which text is drawn on it.



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    
    mouse_pos = list(pg.mouse.get_pos())

    mouse_pos[0] = round( ((mouse_pos[0] +5 ) /x)-3 )
    mouse_pos[1] = round( ((mouse_pos[1] +5) /y)-3 )

    
    text = font.render(str(mouse_pos[0]) + ":" + str(mouse_pos[1]), True, white, (0,0,0))
    
    
    #Rita bordet
    draw_board()


    #Rita alla pjäser
    for i in range(16):
        screen.blit(player_one.pawns[i].surface,get_grid_position(player_one.get_grid_pos(i)))
    for i in range(16):
        screen.blit(player_two.pawns[i].surface,get_grid_position(player_two.get_grid_pos(i)))
    
    
    #Debug för att se vilken ruta som är vilken, gridmässigt
    #screen.blit(text, (0,0))
    pg.display.update()




