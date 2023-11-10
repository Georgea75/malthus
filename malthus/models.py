"""
Population Dynamics Model

Represents a population dynamics model.

"""
from typing import Tuple, Iterator

class PopulationDynamicsModel():

    def __init__(self, input_population: int): 
        """
        Constructor of a basic model

        Arguments:
            int: input_population, the starting population size
        """
        self.population = input_population
        self.death = None
        self.birth = None
        self._step = 0

    def __next__(self) -> Tuple[float, float, float]:
        """
        Generates the next value of the population model.

        Advances the model by one step and calculates the deaths, births, and total population

        returns: 
            tuple: A tuple containing the number of deaths and births, and the total population
        """

        if self.birth != None:
            birth = self.birth(self._step)
        else:
            return
        
        if self.death != None:
            population = self.population + birth

        else: 
            return
        
        death = self.death(population)

        self._step += 1
        return death, birth, population + death
    
    def __iter__(self) -> Iterator:
        """
        Return an iterator object.

        Returns:
            Iterator: An iterator object for this class.
        """
        return self
    
    def __validate__(self):
        """
        Validates the model and raise an exception if
        required.
        """
        error_msg = ""

        if self.birth == None:
            error_msg = "Missing Birth Function \n"
        if self.death == None:
            error_msg += "Missing Death Function \n"

        if len(error_msg) > 0:
            raise ValueError(error_msg)

    def describe(self, steps: int):
        """
        Describes the population at the provided step

        Arguments:
            int: steps, the step to calculate the results for. 
        """
        death, birth, population = self.compute(steps, reset=True)

        print("\n-----------------------")
        print(f"Step: {steps}")
        print("-----------------------")
        print(f"Population: {population[-1]}")
        print(f"Number of Births: {birth[-1]}")
        print(f"Number of Deaths: {death[-1]}")
        print("-----------------------\n")
        
    def compute(self, steps: int, reset: bool = False) -> Tuple[list,list,list]:
        """
        Retrieves the next n steps of the modelled data
        and returns it as three arrays.

        Arguments:
            int: steps, the maximum step to compute the results for.
            bool: reset (Default: False), resets the generator to step 0. 

        Returns: 
            list: death_data, deaths recorded in each step
            list: birth_data, births recorded in each step
            list: population_data, total population in each step
        """

        self.__validate__()

        death_data = []
        birth_data = []
        population_data = []

        for _ in range(steps):
            death, birth, population = next(self)
            death_data.append(death)
            birth_data.append(birth)
            population_data.append(population)

        if reset == True:
            self._step = 0

        return (death_data, birth_data, population_data)