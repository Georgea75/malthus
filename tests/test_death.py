import pytest
import malthus.death as death


@pytest.mark.parametrize(
    "description, function, population, expected_result",
    [
        ("Tests a negative population", death.malthusian_death(0.01), -100, 1),
        ("Tests a zero population", death.malthusian_death(0.01), 0, 0),
        ("Tests a zero death rate", death.malthusian_death(0.0), 100, 0),
        ("Tests simple valid calculation", death.malthusian_death(0.01), 100, -1),
        (
            "Tests decimals in input population",
            death.malthusian_death(0.03),
            2152.24364,
            -64.5673092,
        ),
        (
            "Tests large population",
            death.malthusian_death(0.01),
            999999999999999,
            -9999999999999.99,
        ),
        (
            "Tests very low death rate",
            death.malthusian_death(0.00001),
            436534563456,
            -4365345.63456,
        ),
    ],
)
def test_malthus_death_function(description, function, population, expected_result):
    """
    Tests the malthus death function using a parametrized set of inputs

    arguments:
        description: States the tests purpose to aid with debugging, it is logged when a test fails
        function: The death function to be tested.
        population: The input population
        expected_result: The expected result to run the test with

    """

    assert function(population) == expected_result
