#10.09.2019  testing functions in test _operations
def traffic_light_choice(car , light): # car will have 2 
#     car_movement = ''
    if car == 'moving':
        if light == 'red':
             car_command = 'stop'      
        if light == 'yellow':
             car_command = 'stop'      
        if light == 'green':
             car_command = 'go'    
    if car == 'stop':
        if light == 'red':
             car_command = 'stop'      
        if light == 'yellow':
             car_command = 'stop'      
        if light == 'green':
             car_command = 'go'    
    return  car_command

