from .config import SIZE

def step_diffusion(brain, alpha):
    g = brain.grid
    neighbors = brain.neighbors
    next_grid = [[[0.0 for _ in range(SIZE)] for _ in range(SIZE)] for _ in range(SIZE)]

    for z, layer in enumerate(brain.grid):
        for y, row in enumerate(layer):
            for x, cell in enumerate(row):
                total_strength = 0
                count = 0
                for n in neighbors[(z,y,x)]:
                    nz, ny, nx = n
                    total_strength += g[nz][ny][nx]
                    count += 1
                strength = (1-alpha) * g[z][y][x] + alpha * (total_strength / count)
                next_grid[z][y][x] = strength
    brain.grid = next_grid