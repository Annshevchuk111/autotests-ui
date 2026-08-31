import pytest
import random



@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_reruns():
    assert random.choice([True, False])

@pytest.mark.flaky(reruns=3, reruns_delay=3)
class TestRerun:
    def test_rerun1(self):
        assert random.choice([True, False])
    def test_rerun2(self):
        assert random.choice([True, False])

PLATFORM = 'Windows'

@pytest.mark.flaky(reruns=3, reruns_delay=2,condition=PLATFORM=="Windows")
def test_reruns_with_condition():
    assert random.choice([True, False])