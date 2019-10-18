import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def r():
    r = Relation('country.csv')
    return r

def test_count(r):
    r = r.groupby(['continent']).count("name")
    data_expected = {"continent" : ["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"], "count_name" : [58,5,51,46,37,28,14]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)
    assert r.equals(r_expected)
    
def test_mean(r):
    r = r.groupby(['continent']).max("gnp")
    data_expected = {"continent" : ["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"], "max_gnp" : [116729.0,0.0,3787042.0,2133367.0,8510700.0,351182.0,776739.0]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)
    assert r.equals(r_expected)

def test_median(r):
    r = r.groupby(['continent']).median("gnp")
    data_expected = {"continent" : ["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"], "median_gnp" : [2533.5,0.0,15706.0,20401.0,2223.0,123.0,20300.5]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)
    assert r.equals(r_expected)
