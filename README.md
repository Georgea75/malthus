# Malthus

Malthus is a Python library for building and running population models. 

## Installation

## Usage

### Generating birth and death functions

To instantiate a model death and birth function needs to be declared. 

```
from malthus import death, birth

death = death.linearDeath(0.01)
birth = birth.MalthusianBirth(0.01, 100)

```

The linear death model takes one argument:
- death rate (float): A rate between 0 and 1 used to calculate the number of deaths

The malthusian birth model takes two arguments:
- birth rate (float): A rate between 0 and 1 used to calculate the number of births.
- initial population (int): The size of the initial population. 

### Instantiating a model

The model constructor takes three arguments: 
- initial_population (Int): this is the size of the population at step 0 in the model. 
- death (Callable): A function that will be used to calculate the number of deaths for each period.
- birth (Callable): A function that will be used to calculate the number of births for each period.

```
from malthus import models

model = models.PopulationDynamicsModel(100, death, birth)
```

### Obtaining results

Malthus currently provides three ways to run the model.

#### Iterator

All models in the malthus library are iterators. It is therefore possible to retrieve values using the following methods.

Using a for loop
```
for step in model:
    # YOUR CODE GOES HERE
    print(step)
```

Using the next() function

```

result = next(model) 

```

In both cases a tuple that contains, the deaths, births, and total population for the step is returned. 

For more information about python iterators please refer to the [documentation](https://wiki.python.org/moin/Iterator)

#### Describe

Models can utilize the describe function to return information about a specific time step. 

The describe function takes one parameter step, the step is the time step that the results will reported for. The output of this function is a report that will be logged. The use of describe does not change the current step of the iterator. 

```

model.describe(10)

```


#### Compute

The compute function returns the births, deaths, and total population from the current time step to the step provided to the function.

Compute takes two arguments:

- step (int): The time step that the model should calculate up to and included the provided step. 

- reset (boolean): If this is set to true the model with reset the iterators step to zero. This has a default value of true. 

```

model.compute(10,false)

```

## Documentation

### Models

#### Class: PopulationDynamics Model

The `PopulationDynamicsModel` class represents a basic population dynamics model. It simulates the changes in population over successive steps, considering births and deaths. The model is designed to be iterated over, allowing users to generate and analyze population data for different steps.

##### Attributes
- `population` (int): The current population size.
- `death` (Callable): The death function, which calculates the number of deaths based on the current population.
- `birth` (Callable): The birth function, which calculates the number of births based on the current step.
- `step` (int): The current step of the population model.

##### Methods

- **`describe(self, steps: int) -> None`**
  Describes the population at the provided step without modifying the iterator's step.

  Parameters:
  - `steps` (int): The step to calculate the results for.

- **`compute(self, steps: int) -> Tuple[List[float], List[float], List[float]]`**
  Retrieves the next n steps of the modeled data and returns it as three lists.

  Parameters:
  - `steps` (int): The maximum step to compute the results for.
  
  Returns:
  - `death_data` (List[float]): Deaths recorded in each step.
  - `birth_data` (List[float]): Births recorded in each step.
  - `population_data` (List[float]): Total population in each step.

### Death Functions

The "Death Functions" module provides a collection of death rate functions suitable for population dynamics models.

- **Function: `malthusian_death`**
  
  **Parameters**
  - `d` (float): Death rate constant.

  **Returns**
  - `malthusian_death_function` (Callable): A function that takes the population size (`P`) as input and returns the Malthusian death rate at that population size.

### Birth Functions

The "Birth Functions" module provides a collection of birth rate functions suitable for population dynamics models.

- **Function: `malthusian_birth`**
  
  **Parameters**
  - `P0` (float): Initial population size.
  - `r` (float): Population growth rate.

  **Returns**
  - `malthusian_birth_function` (Callable): A function that takes the time (`t`) as input and returns the population size at that time using the Malthusian growth model.
  
## Name

This library is named after the scholar Thomas Malthus. Malthus was an influential economist mainly known for his work on population dynamics, and the development of the Malthusian growth model. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

The project uses black as a formatter.

## License

Malthus is available under the [MIT](https://opensource.org/license/mit/) license.

# things to deal with
- Clean up docs
- Release
