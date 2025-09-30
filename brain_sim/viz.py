from brain_sim.brain import Brain
from brain_sim.config import SEEDS, SIZE
import matplotlib.pyplot as plt

# brain = Brain()
#
# for (z, y, x), v in SEEDS:
#     brain.set_cell(z, y, x, v)
#
# def project_brain(brain, mode="mean"):
#     g=brain.grid
#
#     projection = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
#
#     if mode == "mean":
#         for z, layer in enumerate(brain.grid):
#             for y, row in enumerate(layer):
#                 for i in range(len(projection)):
#                     projection[y][i] += g[z][y][i]
#
#         for y, row in enumerate(projection):
#             for x, cell in enumerate(row):
#                 projection[y][x] /= SIZE
#
#     if mode == "max":
#         for z, layer in enumerate(brain.grid):
#             for y, row in enumerate(layer):
#                 for i in range(len(projection)):
#                     val = g[z][y][i]
#                     if projection[y][i] < val:
#                         projection[y][i] = val
#
#     return projection


def plot_heatmap(grid, vmin=0.0, vmax=1.0, cmap="hot"):
    plt.imshow(grid, vmin=vmin, vmax=vmax, cmap=cmap, origin="lower", interpolation="nearest")
    plt.colorbar()
    plt.show()
