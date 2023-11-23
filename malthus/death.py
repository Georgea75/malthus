"""
Death functions

A collection of death rate functions suitable for population dynamics models. 
"""
from typing import Callable


def malthusian_death(d: float) -> Callable:
    """
    Calculate the Malthusian death rate at a given population size.

    Args:
    P (float): Population size.
    d (float): Death rate constant.

    Returns:
    Callable: Death rate at the population size P.
    """

    def malthusian_death_function(P: float) -> float:
        return -d * P

    return malthusian_death_function
