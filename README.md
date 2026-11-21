# Malthus

Malthus is a Python library for building and running population models. 

## Installation

Malthus is available through [PyPI](https://pypi.org/project/malthus/)

```
pip install malthus
```

## Usage

### Generating birth and death functions

A model needs a birth function and a death function. Each one takes the
population at the start of a step `P` and the step number `t`, and returns
the number of births or deaths in that step.

```
from malthus import death, birth

death_function = death.malthusian_death(0.1)
birth_function = birth.malthusian_birth(0.2)
```

The Malthusian death function takes one argument:
- d (float): Per-capita death rate per step (0 to 1). Deaths per step = d × P.

The Malthusian birth function takes one argument:
- b (float): Per-capita birth rate per step. Births per step = b × P.

The logistic birth function takes two arguments:
- r_max (float): Maximum per-capita birth rate per step.
- carrying_capacity (float): The population K at which births fall to zero.
  Births per step = r_max × P × (1 − P/K).

### Instantiating a model

The model constructor takes three arguments: 
- initial_population (Int): this is the size of the population at step 0 in the model. 
- death (Callable): A function that will be used to calculate the number of deaths for each period.
- birth (Callable): A function that will be used to calculate the number of births for each period.

```
from malthus import models

model = models.PopulationDynamicsModel(100, death_function, birth_function)
```

Each step, the population is updated using the discrete balancing equation
P(t+1) = P(t) + B(t) − D(t), where births and deaths are both calculated from
P(t). With Malthusian births and deaths this gives P(t) = P(0) × (1 + b − d)^t.

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

The compute function runs the model from the initial population and returns the deaths, births, and total population at the end of each step, up to and including the step provided. The use of compute does not change the current step or population of the iterator.

Compute takes one argument:

- step (int): The time step that the model should calculate up to and included the provided step. 

```
model.compute(10)
```

## Documentation

### Models

#### Class: PopulationDynamicsModel

The `PopulationDynamicsModel` class represents a basic population dynamics model. It simulates the changes in population over successive steps, considering births and deaths. The model is designed to be iterated over, allowing users to generate and analyze population data for different steps.

##### Attributes
- `population` (int): The current population size.
- `death` (Callable): `f(P, t)`, the number of deaths in a step, given the population at the start of the step and the step number.
- `birth` (Callable): `f(P, t)`, the number of births in a step, given the population at the start of the step and the step number.
- `step` (int): The current step of the population model.

##### Methods

- **`describe(self, steps: int) -> None`**
  Describes the population at the provided step without modifying the iterator's step.

  Parameters:
  - `steps` (int): The step to calculate the results for.

- **`compute(self, steps: int) -> Tuple[List[float], List[float], List[float]]`**
  Runs the model from the initial population for n steps and returns the results as three lists. The iterator's current step and population are not modified.

  Parameters:
  - `steps` (int): The maximum step to compute the results for.
  
  Returns:
  - `death_data` (List[float]): Deaths recorded in each step.
  - `birth_data` (List[float]): Births recorded in each step.
  - `population_data` (List[float]): Total population at the end of each step.

### Death Functions

The "Death Functions" module provides a collection of death rate functions suitable for population dynamics models.

- **Function: `malthusian_death`**
  
  **Parameters**
  - `d` (float): Per-capita death rate per step (0 to 1).

  **Returns**
  - `malthusian_death_function` (Callable): A function `f(P, t)` that returns the number of deaths in a step, `d × P`.

### Birth Functions

The "Birth Functions" module provides a collection of birth rate functions suitable for population dynamics models.

- **Function: `malthusian_birth`**
  
  **Parameters**
  - `b` (float): Per-capita birth rate per step.

  **Returns**
  - `malthusian_birth_function` (Callable): A function `f(P, t)` that returns the number of births in a step, `b × P`.

- **Function: `logistic_birth`**
  
  **Parameters**
  - `r_max` (float): Maximum per-capita birth rate per step.
  - `carrying_capacity` (float): The population size `K` at which births fall to zero.

  **Returns**
  - `logistic_birth_function` (Callable): A function `f(P, t)` that returns the number of births in a step, `r_max × P × (1 − P/K)`, floored at zero. Combined with a Malthusian death rate `d`, the population settles at `K × (1 − d/r_max)`.
  
## Name

This library is named after the scholar Thomas Malthus. Malthus was an influential economist mainly known for his work on population dynamics, and the development of the Malthusian growth model. 

## License

Malthus is available under the [MIT](https://opensource.org/license/mit/) license.
