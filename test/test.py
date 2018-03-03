
import pytest
from devices.performance_object import Klapan, Pompa


def test_klapan():
    kl = Klapan(5, 2)
    kl.on
    assert kl.state == 'on'
    kl.off
    assert kl.state == 'off'
    assert kl.add(1, 2) == 3

def test_Pompa():
    pm = Pompa(1, 3)
    pm.on
    assert pm.state == 'on'
    pm.off
    assert pm.state == 'off'
