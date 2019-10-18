import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def r():
    r = Relation('country.csv')
    return r

"Test semijoin on self, should return same"
def test_semijoin(r):
    r = r.semijoin(Relation('country.csv'))
    assert r.equals(r)

def test_semijoin_dif(r):
    r = r.semijoin()
