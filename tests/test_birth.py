import pytest
import malthus.birth as birth


@pytest.mark.parametrize(
    "b, population, expected",
    [
        pytest.param(0.1, 0, 0, id="zero population"),
        pytest.param(0.0, 100, 0, id="zero birth rate"),
        pytest.param(0.1, 100, 10, id="simple calculation"),
        pytest.param(1.5, 100, 150, id="birth rate above one"),
        pytest.param(0.0001, 1, 0.0001, id="very small birth rate"),
    ],
)
def test_malthusian_birth(b, population, expected):
    assert birth.malthusian_birth(b)(population, 0) == pytest.approx(expected)


@pytest.mark.parametrize(
    "population, expected",
    [
        pytest.param(0, 0, id="zero population"),
        pytest.param(500, 125, id="half capacity: 0.5 * 500 * 0.5"),
        pytest.param(1000, 0, id="at capacity"),
        pytest.param(1500, 0, id="above capacity is floored at zero"),
    ],
)
def test_logistic_birth(population, expected):
    f = birth.logistic_birth(r_max=0.5, carrying_capacity=1000)
    assert f(population, 0) == pytest.approx(expected)
