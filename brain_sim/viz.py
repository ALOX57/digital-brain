from brain_sim.brain import Brain
from brain_sim.config import SEEDS, SIZE

brain = Brain()

for (z, y, x), v in SEEDS:
    brain.set_cell(z, y, x, v)

def project_brain(brain, mode="mean"):
    g=brain.grid

    projection = [[0,0,0],[0,0,0],[0,0,0]]

    if mode == "mean":
        for z, layer in enumerate(brain.grid):
            for y, row in enumerate(layer):
                for i in range(len(projection)):
                    projection[y][i] += g[z][y][i]

        for y, row in enumerate(projection):
            for x, cell in enumerate(row):
                projection[y][x] /= SIZE

    if mode == "max":
        for z, layer in enumerate(brain.grid):
            for y, row in enumerate(layer):
                for i in range(len(projection)):
                    val = g[z][y][i]
                    if projection[y][i] < val:
                        projection[y][i] = val

    return projection

print(project_brain(brain))





# def plot_heatmap(grid):