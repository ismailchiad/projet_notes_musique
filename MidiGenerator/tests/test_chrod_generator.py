import pytest

from chord_generator import pick_random_chord
from chord_generator import calculate_interval

from chord_generator import chords

@pytest.fixture
def get_chords_Cmin():
    return [48, 51, 55]

@pytest.fixture
def get_chords_Emaj():
    return [52, 56, 59]

def test_pick_random_chord():
    chord = pick_random_chord()
    assert chord in chords

# def test_pick_random_chord_not_in_chords():
#     chord = 

def test_pick_not_in_chord():
    not_chord = 'Cmin42'
    assert not_chord not in chords 

# test_calculate_interval.py
def test_calculate_interval_positive():
    assert calculate_interval(60, 65) == 5  # C5 à F5

def test_calculate_interval_negative():
    assert calculate_interval(65, 60) == -5  # F5 à C5

def test_calculate_interval_zero():
    assert calculate_interval(60, 60) == 0  # C5 à C5

def test_calculate_interval_large():
    assert calculate_interval(0, 127) == 127  # Plus grand intervalle possible dans MIDI

def test_calculate_interval_small():
    assert calculate_interval(127, 0) == -127  # Plus petit intervalle possible dans MIDI

def test_calculate_interval(get_chords_Cmin, get_chords_Emaj):
    interval = calculate_interval(get_chords_Cmin[0], get_chords_Emaj[0])
    assert interval == 4
    assert calculate_interval(-8, -9) == 1