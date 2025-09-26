from .config import SIZE

class Synapses:
    def __init__(self, brain, neighbors):
        self.weights = {}

        # intialise dictionary of dictionary
        for z, layer in enumerate(brain.grid):
            for y, row in enumerate(layer):
                for x, cell in enumerate(row):
                    self.weights[(z, y, x)] = {}

        # map symmetric connection weights of neighbors
        for z, layer in enumerate(brain.grid):
            for y, row in enumerate(layer):
                for x, cell in enumerate(row):
                    for n in neighbors[(z, y, x)]:
                        self.weights[(z, y, x)][n] = 0.0
                        self.weights[n][(z, y, x)] = 0.0

