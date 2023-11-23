import pytest
import malthus.birth as birth


@pytest.mark.parametrize(
    "description, function, time, expected_result",
    [
        ("Tests a population of zero", birth.malthusian_birth(0, 0.1), 100, 0),
        (
            "Tests a negative birth rate",
            birth.malthusian_birth(10, -0.1),
            10,
            3.6787944117144233,
        ),
        ("Tests a birth rate of zero", birth.malthusian_birth(10, 0), 10, 10),
        (
            "Tests a birth rate greater than one",
            birth.malthusian_birth(10, 1.1),
            10,
            598741.4171519781,
        ),
        (
            "Tests a float time interval",
            birth.malthusian_birth(10, 0.1),
            5.5,
            17.332530178673952,
        ),
        (
            "Tests simple calculation",
            birth.malthusian_birth(10, 0.1),
            10,
            27.18281828459045,
        ),
        (
            "Tests very small birth rate",
            birth.malthusian_birth(1, 0.0001),
            1,
            1.0001000050001667,
        ),
    ],
)
def test_malthus_birth_function(description, function, time, expected_result):
    """
    Tests the malthus birth function using a parametrized set of inputs

    arguments:
        description: States the tests purpose to aid with debugging, it is logged when a test fails
        function: The birth function to be tested.
        population: The input population
        expected_result: The expected result to run the test with

    """
    assert function(time) == expected_result
