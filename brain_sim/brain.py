from .config import SIZE, OFF
import random

class Brain:
    def __init__(self, size=SIZE, offsets = OFF):
        self.size = size


        self.sns = [[0.0 for _ in range(size)] for _ in range (size)]
        self.prd = [[0.0 for _ in range(size)] for _ in range (size)]

        self.connections = [[[[0.0 for _ in range(3)] for _ in range(3)] for _ in range (size)] for _ in range(size)]

        for y, row in enumerate(self.prd):
            for x, cell in enumerate(row):
                for dy in offsets:
                    for dx in offsets:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < size and 0 <= nx < size:
                            dy_i = dy + 1
                            dx_i = dx + 1
                            connections[y][x][dy_i][dx_i] = random.uniform(-0.1, 0.1)




    def set_cell(self, z, y, x, v):
            self.grid[z][y][x] = v

    def get_cell(self, z, y, x):
        return self.grid[z][y][x]