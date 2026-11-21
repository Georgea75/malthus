from typing import Callable


def malthusian_birth(b: float) -> Callable[[float, int], float]:
    """
    Create a Malthusian (density-independent) birth function.

    Births per step are proportional to the population at the start of the
    step: B_t = b * P_t.

    Arguments:
    b (float): Per-capita birth rate per time step (b >= 0).

    Returns:
    Callable: f(P, t) returning the number of births in the step.
    """

    def malthusian_birth_function(P: float, t: int) -> float:
        return b * P

    return malthusian_birth_function


def logistic_birth(
    r_max: float, carrying_capacity: float
) -> Callable[[float, int], float]:
    """
    Create a logistic (density-dependent) birth function.

    Births per step fall as the population approaches the carrying capacity:
    B_t = r_max * P_t * (1 - P_t / K), floored at zero.

    Combined with a Malthusian death rate d, the population settles at
    K * (1 - d / r_max). With d = 0 this is the textbook discrete logistic
    model, which settles at K.

    Arguments:
    r_max (float): Maximum per-capita birth rate per time step.
    carrying_capacity (float): The population size K at which births fall to zero.

    Returns:
    Callable: f(P, t) returning the number of births in the step.
    """

    def logistic_birth_function(P: float, t: int) -> float:
        return max(0.0, r_max * P * (1 - P / carrying_capacity))

    return logistic_birth_function
