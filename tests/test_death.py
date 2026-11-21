import pytest
import malthus.death as death


@pytest.mark.parametrize(
    "d, population, expected",
    [
        pytest.param(0.01, 0, 0, id="zero population"),
        pytest.param(0.0, 100, 0, id="zero death rate"),
        pytest.param(0.01, 100, 1, id="simple calculation"),
        pytest.param(0.03, 2152.24364, 64.5673092, id="decimal population"),
        pytest.param(0.01, 999999999999999, 9999999999999.99, id="large population"),
        pytest.param(1.0, 100, 100, id="everyone dies"),
    ],
)
def test_malthusian_death(d, population, expected):
    assert death.malthusian_death(d)(population, 0) == pytest.approx(expected)


def test_malthusian_death_independent_of_time():
    f = death.malthusian_death(0.1)
    assert f(100, 0) == f(100, 50)
