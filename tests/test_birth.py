import pytest
import sys
import malthus.birth as birth


BASE_POPULATION = 10

@pytest.fixture
def malthus_birth_function_negative_rate():
    """
    Generates a malthus birth function with a negative birth rate

    returns:
        function: Malthus birth function
    """
    return birth.malthusian_birth(BASE_POPULATION,-0.1)

@pytest.fixture
def malthus_birth_function_zero_rate():
    """
    Generates a malthus birth function with a birth rate of zero

    returns:
        function: Malthus birth function
    """
    return birth.malthusian_birth(BASE_POPULATION, 0)

@pytest.fixture
def malthus_birth_function_zero_population():
    """
    Generates a malthus birth function with a birth rate of zero

    returns:
        function: Malthus birth function
    """
    return birth.malthusian_birth(0, 0.1)

@pytest.fixture
def malthus_birth_function_greater_than_one():
    """
    Generates a malthus birth function with a birth rate greater than one

    returns:
        function: Malthus birth function
    """
    return birth.malthusian_birth(BASE_POPULATION, 1.1)

@pytest.fixture
def malthus_birth_function_valid():
    """
    Generates a valid malthus birth function

    returns:
        function: Malthus birth function
    """

    return birth.malthusian_birth(BASE_POPULATION, 0.1)

def test_malthus_birth_zero_population(malthus_birth_function_zero_population):
    """
    Tests the behavior when a population of zero is supplied
    """

    time_period = 100
    expected_result = 0
    assert malthus_birth_function_zero_population(time_period) == expected_result

def test_malthus_birth_negative_rate(malthus_birth_function_negative_rate):
    """
    Tests if a negative rate returns a valid result
    """
    time_period = 10
    expected_result = 3.6787944117144233

    assert malthus_birth_function_negative_rate(time_period) == expected_result

def test_malthus_birth_zero_rate(malthus_birth_function_zero_rate):
    """
    Tests if a zero rate returns no growth
    """

    assert malthus_birth_function_zero_rate(10) == BASE_POPULATION

def test_malthus_birth_greater_than_one_rate(malthus_birth_function_greater_than_one):
    """
    Tests if a rate greater than one returns a valid result
    """
    time_period = 10
    expected_result = 598741.4171519781

    assert malthus_birth_function_greater_than_one(time_period) == expected_result

def test_malthus_birth_float_time_period(malthus_birth_function_valid):
    """
    Tests if a float time interval returns a warning and the valid result
    """
    time_period = 5.5
    expected_result = 17.332530178673952

    assert malthus_birth_function_valid(time_period) == expected_result

@pytest.mark.parametrize("function, time, expected_result", [
    (birth.malthusian_birth(10,0.1), 10, 27.18281828459045),
    (birth.malthusian_birth(1,0.0001),1,1.0001000050001667)
])
def test_malthus_birth_function_valid(function, time, expected_result):
    """
    Tests valid birth calculations
    """
    assert function(time) ==  expected_result
