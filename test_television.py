import pytest
from television import *

@pytest.fixture
def television():
    return Television()

def test_initial_state(television):
    assert not television._status
    assert not television._muted
    assert television._volume == min_volume
    assert television._channel == min_channel

def test_power(television):
    television.power()
    assert television._status
    television.power()
    assert not television._status

def test_mute(television):
    television.power()
    television.mute()
    assert television._muted
    television.mute()
    assert not television._muted

def test_channel_up(television):
    television.power()
    television.channel_up()
    assert television._channel == min_channel + 1
    television._channel = max_channel
    television.channel_up()
    assert television._channel == min_channel

def test_volume_up(television):
    television.power()
    television.volume_up()
    assert television._volume == min_volume + 1
    television._volume = max_volume
    television.volume_up()
    assert television._volume == max_volume

def test_volume_down(television):
    television.power()
    television._volume = max_volume
    television.volume_down()
    assert television._volume == max_volume - 1
    television.volume_down()
    television.volume_down()
    assert television._volume == min_volume
