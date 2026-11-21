from typing import Callable


def malthusian_death(d: float) -> Callable[[float, int], float]:
    """
    Create a Malthusian (density-independent) death function.

    Deaths per step are proportional to the population at the start of the
    step: D_t = d * P_t.

    Args:
    d (float): Per-capita death rate per time step (0 <= d <= 1).

    Returns:
    Callable: f(P, t) returning the number of deaths in the step.
    """

    def malthusian_death_function(P: float, t: int) -> float:
        return d * P

    return malthusian_death_function
