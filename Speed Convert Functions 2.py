# This program shows how to use a function
# it will convert km/hr to miles / hr

conversion= float(0.621371)


# first we need to define the function
def convert_to_miles(speed):
    miles_per_hour=speed * conversion
    return(miles_per_hour)

def convert_to_km(speed):
    km_per_hour=speed/ conversion
    return(km_per_hour)

def get_speed():
    speed = int(input('Speed to convert ? : '))
    return(speed)

def get_direction():
    direction = input('Convert km to mph (press m) or mph to km (press k) ? ')
    if direction == 'm':
        return('m')
    elif direction == 'k':
        return('k')
    else:
        return('x')


#now we make our main program
speed = get_speed()
direction = get_direction()               
if direction == 'm':
    mph_speed = convert_to_miles(speed)
    print(f'The converted speed is {mph_speed} miles per hour.')
elif direction == 'k':
    kph_speed = convert_to_km(speed)
    print(f'The converted speed is {kph_speed} km per hour.')
else:
    print('incorrect response')