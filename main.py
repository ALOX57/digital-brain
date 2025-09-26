import time

# initialise neurons
brain = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]]
]

neighbors = {}

SIZE = 3
OFF = [-1, 0, 1]

# map neighbors
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

connections = {}

# initiate dictionary of dictionary
for z, layer in enumerate(brain):
    for y, row in enumerate(layer):
        for x, cell in enumerate(row):
            connections[(z,y,x)] = {}

# map connection weights of neighbors
for z, layer in enumerate(brain):
    for y, row in enumerate(layer):
        for x, cell in enumerate(row):
            for n in neighbors[(z,y,x)]:
                connections[(z,y,x)][n] = 0.0
                connections[n][(z,y,x)] = 0.0


def step(alpha = 0.2):
    global brain

    next_brain = [
        [[0,0,0],[0,0,0],[0,0,0]],
        [[0,0,0],[0,0,0],[0,0,0]],
        [[0,0,0],[0,0,0],[0,0,0]]
    ]

    for z, layer in enumerate(brain):
        for y, row in enumerate(layer):
            for x, cell in enumerate(row):
                total_strength = 0
                count = 0
                for n in neighbors[(z,y,x)]:
                    nz, ny, nx = n
                    total_strength += brain[nz][ny][nx]
                    count += 1
                strength = (1-alpha) * brain[z][y][x] + alpha * (total_strength / count)
                next_brain[z][y][x] = strength
    brain = next_brain

brain[1][1][1] = 1.0
print(brain[0][0][0])


steps = 20
tick_s = 0.100  # 100 ms

compute_ms_total = 0.0
loop_start = time.perf_counter()
next_deadline = loop_start + tick_s

for i in range(steps):
    tick_start = time.perf_counter()

    # compute
    t0 = time.perf_counter()
    step(alpha=0.01)
    t1 = time.perf_counter()

    compute_ms = (t1 - t0) * 1000.0
    compute_ms_total += compute_ms
    print(f"After step {i+1}, center = {brain[1][1][1]}")

    # sleep until deadline
    now = time.perf_counter()
    sleep_s = next_deadline - now
    if sleep_s > 0:
        time.sleep(sleep_s)
        overrun_ms = 0.0
    else:
        overrun_ms = (-sleep_s) * 1000.0  # missed deadline

    # schedule next tick
    next_deadline += tick_s
    while next_deadline <= time.perf_counter():
        next_deadline += tick_s

loop_end = time.perf_counter()

wall_ms_total = (loop_end - loop_start) * 1000.0
avg_compute_ms = compute_ms_total / steps
avg_wall_ms = wall_ms_total / steps

print(f"Total wall: {wall_ms_total:.4f} ms")
print(f"Avg compute per step: {avg_compute_ms:.4f} ms")
print(f"Avg wall per step (incl. sleep): {avg_wall_ms:.4f} ms")
print(f"Budget used: {avg_compute_ms/(tick_s*1000):.4%} of {tick_s*1000:.0f} ms")


