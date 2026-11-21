import pytest
from collections.abc import Iterable
from malthus.models import PopulationDynamicsModel
import malthus.birth as birth
import malthus.death as death

BASE_POPULATION = 100
BIRTH_RATE = 0.2
DEATH_RATE = 0.1


@pytest.fixture
def malthus_model():
    return PopulationDynamicsModel(
        BASE_POPULATION,
        death.malthusian_death(DEATH_RATE),
        birth.malthusian_birth(BIRTH_RATE),
    )


def test_model_is_iterable(malthus_model):
    assert isinstance(malthus_model, Iterable)


def test_next(malthus_model):
    assert next(malthus_model) == pytest.approx((10, 20, 110))
    assert malthus_model.population == pytest.approx(110)


def test_compute_matches_analytic_solution(malthus_model):
    """Discrete Malthusian model: P_t = P_0 * (1 + b - d) ** t."""
    steps = 50
    _, _, population = malthus_model.compute(steps)
    expected = [
        BASE_POPULATION * (1 + BIRTH_RATE - DEATH_RATE) ** t
        for t in range(1, steps + 1)
    ]
    assert population == pytest.approx(expected)


def test_equal_rates_give_stable_population():
    model = PopulationDynamicsModel(
        100, death.malthusian_death(0.1), birth.malthusian_birth(0.1)
    )
    assert model.compute(20)[2] == pytest.approx([100] * 20)


def test_logistic_reaches_equilibrium():
    """With logistic births and Malthusian deaths, P* = K * (1 - d / r_max)."""
    model = PopulationDynamicsModel(
        10, death.malthusian_death(0.1), birth.logistic_birth(0.5, 1000)
    )
    assert model.compute(500)[2][-1] == pytest.approx(800)


def test_compute_does_not_change_state(malthus_model):
    next(malthus_model)
    malthus_model.compute(10)
    assert malthus_model.step == 1
    assert malthus_model.population == pytest.approx(110)


def test_compute_restarts_from_initial_population(malthus_model):
    next(malthus_model)
    _, _, population = malthus_model.compute(1)
    assert population == pytest.approx([110])


def test_compute_zero_steps(malthus_model):
    assert malthus_model.compute(0) == ([], [], [])
