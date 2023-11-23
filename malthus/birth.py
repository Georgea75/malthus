"""
Birth functions

A collection of birth rate functions suitable for population dynamics models. 
"""
from typing import Callable
import math


def malthusian_birth(P0: float, r: float) -> Callable:
    """
    Calculate the population size at time t using the Malthusian growth model.

    Arguments:
    P0 (float): Initial population size.
    r (float): Population growth rate.

    Returns:
    Callable: A malthusian (exponential) birth rate function.
    """

    def malthusian_birth_function(t: int):
        return P0 * math.exp(r * t)

    return malthusian_birth_function
