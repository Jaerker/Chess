class Piece():

    alive = True
    move_rules = []
    #Grunden till alla pjäser. 
    #Alla pjäser har namn, x och y position och levande eller död.
    def __init__(self, name, grid_position, surface):
        self.name = name
        self.grid_position = grid_position
        self.surface = surface




    def test(self):
        print("This works!")
    