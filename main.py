brain = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]]
]

neighbors = {}

SIZE = 3
OFF = [-1, 0, 1]

for z, layer in enumerate(brain):
    for y, row in enumerate(layer):
        for x, cell in enumerate(row):
            N = []

            for dz in OFF:
                for dy in OFF:
                    for dx in OFF:
                        if dz == 0 and dy == 0 and dx == 0:
                            continue
                        nz, ny, nx = z + dz, y + dy, x + dx
                        if 0 <= nz < SIZE and 0 <= ny < SIZE and 0 <= nx < SIZE:
                            N.append((nz, ny, nx))
            neighbors[(z,y,x)] = N


print(f"Middle neighbors: {len(neighbors[(1,1,1)])}")
print(f"Corner neighbors: {len(neighbors[(0,0,0)])}")
print(f"Edge neighbors: {len(neighbors[(0,0,1)])}")
print(f"Face neighbors: {len(neighbors[(0,1,1)])}")


connections = {}

for z, layer in enumerate(brain):
    for y, row in enumerate(layer):
        for x, cell in enumerate(row):
            connections[(z,y,x)] = {}

for z, layer in enumerate(brain):
    for y, row in enumerate(layer):
        for x, cell in enumerate(row):
            for n in neighbors[(z,y,x)]:
                connections[(z,y,x)][n] = 0.0
                connections[n][(z,y,x)] = 0.0



