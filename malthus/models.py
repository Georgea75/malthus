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
        self.initial_population = input_population
        self.death = death_function
        self.birth = birth_function
        self.step = 0

    def __next__(self) -> Tuple[float, float, float]:
        """
        Advances the model by one time step.

        Births and deaths are both calculated from the population at the start
        of the step, P_t, and the population is updated using the discrete
        balancing equation:

            P_{t+1} = P_t + B_t - D_t

        returns:
            tuple: (deaths, births, population at the end of the step)
        """

        step_births = self.birth(self.population, self.step)
        step_deaths = self.death(self.population, self.step)

        self.population = self.population + step_births - step_deaths
        self.step += 1

        return step_deaths, step_births, self.population

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
        Runs the model from the initial population for the given number of
        steps and returns the results as three lists. The iterator's current
        step and population are not modified.

        Arguments:
            int: steps, the number of steps to compute.

        Returns:
            list: death_data, deaths recorded in each step
            list: birth_data, births recorded in each step
            list: population_data, total population at the end of each step
        """

        original_step = self.step
        original_population = self.population
        self.step = 0
        self.population = self.initial_population

        try:
            results = [next(self) for _ in range(steps)]
        finally:
            self.step = original_step
            self.population = original_population

        if not results:
            return [], [], []

        death_data, birth_data, population_data = zip(*results)

        return list(death_data), list(birth_data), list(population_data)
