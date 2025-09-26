from .config import SIZE, OFF

class Brain:
    def __init__(self, size=SIZE, offsets = OFF):
        self.size = size

        self.grid = [[[0.0 for _ in range(SIZE)] for _ in range(SIZE)] for _ in range(SIZE)]

        self.neighbors = {}

        # map Moore neighbors for each neuron
        for z, layer in enumerate(self.grid):
            for y, row in enumerate(layer):
                for x, cell in enumerate(row):
                    N = []

                    for dz in offsets:
                        for dy in offsets:
                            for dx in offsets:
                                if dz == 0 and dy == 0 and dx == 0:
                                    continue
                                nz, ny, nx = z + dz, y + dy, x + dx
                                if 0 <= nz < SIZE and 0 <= ny < SIZE and 0 <= nx < SIZE:
                                    N.append((nz, ny, nx))
                    self.neighbors[(z, y, x)] = N

    def set_cell(self, z, y, x, v):
            self.grid[z][y][x] = v

    def get_cell(self, z, y, x):
        return self.grid[z][y][x]