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
def empty_model_instance():
    """
    Generates empty model

    returns:
        PopulationDynamicsModel: Empty Model
    """
    return PopulationDynamicsModel(1)

@pytest.fixture 
def malthus_model_instance():
    """
    Generates a Malthusian Demographic model

    returns:
        PopulationDynamicsModel: Malthus Population Model
    """

    malthus_model = PopulationDynamicsModel(BASE_POPULATION)
    malthus_model.death = death.malthusian_death(DEATH_RATE)
    malthus_model.birth = birth.malthusian_birth(BASE_POPULATION, BIRTH_RATE)

    return malthus_model

def test_model_iterator_initialization(empty_model_instance):
    """ 
    Tests if the model object is an iterator
    """
    assert isinstance(empty_model_instance, Iterable)

def test_next_empty_model(empty_model_instance):
    """
    Test an empty models iterator 
    """
    assert None == next(empty_model_instance)

def test_half_initialized_model(empty_model_instance):
    """
    Tests is a model works with only one of the required functions
    """
    empty_model_instance.death = death.malthusian_death(0.1)

    assert None == next(empty_model_instance)

    empty_model_instance.death = None
    empty_model_instance.birth = birth.malthusian_birth(BASE_POPULATION, BIRTH_RATE)

    assert None == next(empty_model_instance)

def test_next_malthus_model(malthus_model_instance):
    """
    Test that next of a valid malthus model returns the expected result
    """

    expected_result = (-20, 100, 180)

    assert expected_result == next(malthus_model_instance)

def test_valid_compute(malthus_model_instance):
    """
    Validates the get array function of a valid model
    """

    time_period = 5
    expected_array = ([-20.0, -21.05170918075648, -22.214027581601698, -23.498588075760033, -24.918246976412703], 
    [100.0, 110.51709180756477, 122.14027581601698, 134.9858807576003, 149.18246976412703], 
    [180.0, 189.4653826268083, 199.92624823441528, 211.48729268184027, 224.26422278771435])

    assert expected_array == malthus_model_instance.compute(time_period)

def test_compute(empty_model_instance):
    """
    Tests the behavior of compute with an invalid model
    """
    
    birth_error_msg = "Missing Birth Function \n" 
    death_error_msg = "Missing Death Function \n"


    # Test Empty Model
    with pytest.raises(ValueError) as error:
        empty_model_instance.compute(5)

    # Test Missing birth function
    empty_model_instance.birth = birth.malthusian_birth(BASE_POPULATION, BIRTH_RATE)

    with pytest.raises(ValueError) as error:
        empty_model_instance.compute(5)

    # Test Missing death function
    empty_model_instance.birth = None
    empty_model_instance.death = death.malthusian_death(DEATH_RATE)

    with pytest.raises(ValueError) as error:
        empty_model_instance.compute(5)

