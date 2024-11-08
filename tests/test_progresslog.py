import pytest

from Final2x_core.util.progressLog import PrintProgressLog


class Test_ProgressLog:
    def test_set(self) -> None:
        p = PrintProgressLog()
        p.set(10, 2)
        assert p.Total == 20
        assert p.sr_n == 2
        with pytest.raises(AssertionError):
            p.set(0, 2)
        with pytest.raises(AssertionError):
            p.set(10, 0)
        with pytest.raises(AssertionError):
            p.set(10, -1)
        with pytest.raises(AssertionError):
            p.set(-1, 2)
