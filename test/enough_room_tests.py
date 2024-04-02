from ..codewar_problems.will_there_be_enough_space_on_the_bus import enough_room

def test_bus_has_enough_room():
    assert enough_room(10, 5, 5) == 0
    assert enough_room(20, 15, 5) == 0

def test_bus_does_not_have_enough_room():
    assert enough_room(100, 60, 50) == 10 
    