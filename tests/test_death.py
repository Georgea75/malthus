import pytest
import malthus.death as death


@pytest.fixture
def malthus_death_function_valid():
    """
    Generates a valid malthus death function

    Returns: 
        function: Malthus death function
    """

    return death.malthusian_death(0.01)

@pytest.fixture
def malthus_death_function_zero():
    """
    Generates a malthus death function with a death rate of zero

    returns:
        function: Malthus death function
    """
    return death.malthusian_death(0.0)

@pytest.fixture
def malthus_death_function_negative():
    """
    Generates a malthus death function with a negative death rate

    returns:
        function: Malthus death function
    """
    return death.malthusian_death(-0.01)

def test_malthus_death_zero_population(malthus_death_function_valid):
    """
    Test malthus death function with a population of zero
    """
    assert malthus_death_function_valid(0) == 0

def test_malthus_death_negative_population(malthus_death_function_valid):
    """
    Test malthus death function with a negative population
    """
    assert malthus_death_function_valid(-100) == 1

def test_malthus_death_zero_death_rate(malthus_death_function_zero):
    """
    Test malthus death function with a death rate of zero
    """
    assert malthus_death_function_zero(100) == 0

@pytest.mark.parametrize("function, population, expected_result", [
    (death.malthusian_death(0.01), 100, -1),
    (death.malthusian_death(0.03), 2152.24364,-64.5673092),
    (death.malthusian_death(0.01), 999999999999999, -9999999999999.99),
    (death.malthusian_death(0.00001), 436534563456, -4365345.63456)
])
def test_malthus_death_valid(function, population, expected_result):
    """
    Validates the malthus function against expected values
    """

    assert function(population) ==  expected_result

