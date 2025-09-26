import time

class FixedRateLoop:
    def __init__(self, tick_s: float):
        self.tick_s = tick_s

    def run(self, steps, do_step):
        compute_ms_total = 0.0
        loop_start = time.perf_counter()
        next_deadline = loop_start + self.tick_s

        for i in range(steps):
            tick_start = time.perf_counter()
            # compute
            t0 = time.perf_counter()
            do_step(i)
            t1 = time.perf_counter()

            compute_ms = (t1 - t0) * 1000.0
            compute_ms_total += compute_ms

            # sleep until deadline
            now = time.perf_counter()
            sleep_s = next_deadline - now
            if sleep_s > 0:
                time.sleep(sleep_s)
                overrun_ms = 0.0
            else:
                overrun_ms = (-sleep_s) * 1000.0  # missed deadline
                print(f"Step {i + 1} deadline overrun: {overrun_ms:.4f} ms")

            # schedule next tick
            next_deadline += self.tick_s
            # catch up if still behind
            while next_deadline <= time.perf_counter():
                next_deadline += tick_s

        loop_end = time.perf_counter()
        wall_ms_total = (loop_end - loop_start) * 1000.0
        avg_compute_ms = compute_ms_total / steps
        avg_wall_ms = wall_ms_total / steps
        return wall_ms_total, avg_compute_ms, avg_wall_ms