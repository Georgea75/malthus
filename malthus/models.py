"""
Population Dynamics Model

Represents a population dynamics model.

"""
from typing import Tuple, List, Iterator, Callable
import logging


class PopulationDynamicsModel:
    def __init__(
        self, input_population: int, death_function: Callable, birth_function: Callable
    ):
        """
        Constructor of a basic model
        """

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.population = input_population
        self.death = death_function
        self.birth = birth_function
        self.step = 0

    def __next__(self) -> Tuple[float, float, float]:
        """
        Generates the next value of the population model.

        Advances the model by one step and calculates the deaths, births, and total population.
        It does this by first calculating the number of births in the step, it then calculates
        the total number of deaths using the last steps population combined with the new births.
        Lastly the new total population is summed by adding the deaths to the population with the
        current steps birth.

        returns:
            tuple: A tuple containing the number of deaths and births, and the total population
        """

        step_births = self.birth(self.step)
        population_with_step_births = self.population + step_births

        step_deaths = self.death(population_with_step_births)
        step_population = population_with_step_births + step_deaths

        self.step += 1

        return step_deaths, step_births, step_population

    def __iter__(self) -> Iterator:
        """
        Return an iterator object.

        Returns:
            Iterator: An iterator object for this class.
        """
        return self

    def describe(self, steps: int):
        """
        Describes the population at the provided step. The step of the iterator is not modified.

        Arguments:
            int: steps, the step to calculate the results for.
        """
        death, birth, population = self.compute(steps)

        self.logger.info("-----------------------")
        self.logger.info(f"Step: {steps}")
        self.logger.info("-----------------------")
        self.logger.info(f"Population: {population[-1]}")
        self.logger.info(f"Number of Births: {birth[-1]}")
        self.logger.info(f"Number of Deaths: {death[-1]}")
        self.logger.info("-----------------------")

    def compute(self, steps: int) -> Tuple[List[float], List[float], List[float]]:
        """
        Retrieves the next n steps of the modelled data and returns it as three arrays. The step of the iterator
        is not modified.

        Arguments:
            int: steps, the maximum step to compute the results for.

        Returns:
            list: death_data, deaths recorded in each step
            list: birth_data, births recorded in each step
            list: population_data, total population in each step
        """

        original_step = self.step
        self.step = 0

        death_data, birth_data, population_data = zip(
            *[(next(self)) for _ in range(steps)]
        )

        self.step = original_step

        return list(death_data), list(birth_data), list(population_data)
