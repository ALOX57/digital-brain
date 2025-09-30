from .config import SIZE

def step_predictive(brain, alpha, size = SIZE):
    alpha = alpha
    sensors     = brain.sns
    predictions = brain.prd
    connections = brain.connections

    sens_hat = [[0.0 for _ in range(size)] for _ in range (size)]

    for y, row in enumerate(predictions):
        for x, cell in enumerate(row):
            for dy_i in range(3):
                for dx_i in range(3):
                    dy = dy_i - 1
                    dx = dx_i - 1
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < size and 0 <= nx < size:
                        sens_hat[ny][nx] += predictions[y][x] * connections[y][x][dy_i][dx_i]

    errors = [[0.0 for _ in range(size)] for _ in range(size)]

    for y in range(size):
        for x in range(size):
            errors[y][x] = sensors[y][z] - sens_hat[y][z]

    for y, row in enumerate(predictions):
        for x, cell in enumerate(row):
            for dy_i in range(3):
                for dx_i in range(3):
                    dy = dy_i - 1
                    dx = dx_i - 1
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < size and 0 <= nx < size:
                        error    = errors[ny][nx]
                        weight = connections[y][x][dy_i][dx_i]
                        connections[y][x][dy_i][dx_i] = weight + alpha * error * predictions[x][y]


    for y, row in enumerate(predictions):
        for x, cell in enumerate(row):
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



