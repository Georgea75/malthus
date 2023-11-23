import pytest
from malthus.models import PopulationDynamicsModel
import malthus.birth as birth
import malthus.death as death
from collections.abc import Iterable
import sys

# Test constants
BASE_POPULATION = 100
DEATH_RATE = 0.1
BIRTH_RATE = 0.1


@pytest.fixture
def malthus_model_instance():
    """
    Generates a Malthusian Demographic model

    returns:
        PopulationDynamicsModel: Malthus Population Model
    """

    death_function = death.malthusian_death(DEATH_RATE)
    birth_function = birth.malthusian_birth(BASE_POPULATION, BIRTH_RATE)

    malthus_model = PopulationDynamicsModel(
        BASE_POPULATION, death_function, birth_function
    )

    return malthus_model


def test_model_iterator_initialization(malthus_model_instance):
    """
    Tests if the model object is an iterator
    """
    assert isinstance(malthus_model_instance, Iterable)


def test_next_malthus_model(malthus_model_instance):
    """
    Test that next of a valid malthus model returns the expected result
    """

    expected_result = (-20, 100, 180)

    assert expected_result == next(malthus_model_instance)


def test_compute(malthus_model_instance):
    """
    Validates the get array function of a valid model
    """

    time_period = 5
    expected_array = (
        [
            -20.0,
            -21.05170918075648,
            -22.214027581601698,
            -23.498588075760033,
            -24.918246976412703,
        ],
        [
            100.0,
            110.51709180756477,
            122.14027581601698,
            134.9858807576003,
            149.18246976412703,
        ],
        [
            180.0,
            189.4653826268083,
            199.92624823441528,
            211.48729268184027,
            224.26422278771435,
        ],
    )

    assert expected_array == malthus_model_instance.compute(time_period)


def test_compute_does_not_increment_step(malthus_model_instance):
    """
    Tests if the compute function does not increment the step variable
    """

    initial_step = 0
    next_step = 1

    malthus_model_instance.compute(1)
    assert malthus_model_instance.step == initial_step

    next(malthus_model_instance)
    malthus_model_instance.compute(1)
    assert malthus_model_instance.step == next_step
