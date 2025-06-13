class World:
    def __init__(self, world_map):
        self.obstacle = []
        self.doors = []
        self.bombs = []
        self.boxes = []
        self.keys = []
        self.energy = []
        self.energy_lake = []
        for i in range(len(world_map)):
            for j in range(len(world_map[i])):
                if world_map[i][j] == 0:
                    pass
                    # TODO create bomb Object and add to the specified list
                elif world_map[i][j] == 1:
                    pass
                    # TODO create energy object and add to the specified list
                elif world_map[i][j] in (2, 3, 4, 5, 7, 8):
                    pass
                    # TODO create key object and add to the specified list
                elif world_map[i][j] in (6,21):
                    pass
                    # TODO create obstacle object and add to the list
                elif world_map[i][j] == (9, 10):
                    pass
                    # TODO create energyLake object and add to the list
                elif world_map[i][j] == (11, 12, 17,22,25,26,27,28,29,30):
                    pass
                    # TODO create door object
                elif world_map[i][j] == (13, 14,15,16,23,24,31,32,33,34,35,36):
                   

