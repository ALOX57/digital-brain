from .config import SIZE

def step_predictive(brain, alpha, size = SIZE):
    sensors     = brain.sns
    predictions = brain.prd
    connections = brain.connections

    for y, row in enumerate(predictions):
        for x, cell in enumerate(row):
            weights = connections[y][x]
            sum     = 0
            for dy_i in range(3):
                for dx_i in range(3):
                    dy = dy_i - 1
                    dx = dx_i - 1
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < size and 0 <= nx < size:
                        activation = sensors[ny][nx]
                        weight     = connections[y][x][dy_i][dx_i]
                        sum       += activation * weight

            predictions[y][x] = sum



#=======================================================================================================================



def step_diffusion_legacy(brain, alpha):
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



