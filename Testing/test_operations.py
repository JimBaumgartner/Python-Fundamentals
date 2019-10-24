# 10.09.2019
# car = 'go' , stop
#light = red , yellow , green
# return = move or Stop
from operations import traffic_light_choice

# need to test every option
def test_light_choice_moving_red():
    assert traffic_light_choice('moving', 'red') == 'stop'
def test_light_choice_moving_yellow():
    assert traffic_light_choice('moving','yellow') == 'stop'
def test_light_choice_moving_green():
    assert  traffic_light_choice('moving','green') == 'go'
def test_light_choice_stop_red():
    assert  traffic_light_choice('stop','red') == 'stop'
def test_light_choice_stop_yellow():
    assert  traffic_light_choice('stop','yellow') == 'stop'
def test_light_choice_stop_green():
    assert  traffic_light_choice('stop','green') == 'go'

    