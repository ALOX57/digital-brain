from brain_sim.config import SIZE, SEEDS, ALPHA, STEPS, TICK_S
from brain_sim.brain import Brain
from brain_sim.synapses import Synapses
from brain_sim.update import step_diffusion
from brain_sim.timing import FixedRateLoop


def main():
    brain = Brain()
    syn = Synapses(brain, brain.neighbors)

    for (z, y, x), v in SEEDS:
        brain.set_cell(z, y, x, v)

    loop = FixedRateLoop(TICK_S)

    def do_step(i):
        step_diffusion(brain, ALPHA)
        print(f"After step {i + 1}, center = {brain.get_cell(1, 1, 1)}")

    wall_ms_total, avg_compute_ms, avg_wall_ms = loop.run(STEPS, do_step)

    print(f"Total wall: {wall_ms_total:.4f} ms")
    print(f"Avg compute per step: {avg_compute_ms:.4f} ms")
    print(f"Avg wall per step (incl. sleep): {avg_wall_ms:.4f} ms")
    print(f"Budget used: {avg_compute_ms / (TICK_S * 1000):.4%} of {TICK_S * 1000:.0f} ms")


if __name__ == "__main__":
    main()