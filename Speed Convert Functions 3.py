# This program shows how to use a function
# it will convert km/hr to miles / hr

conversion= float(0.621371)


# first we need to define the function
#def convert_to_miles(speed):
  #  miles_per_hour=speed * conversion
   # return(miles_per_hour)

#def convert_to_km(speed):
  #  km_per_hour=speed/ conversion
  #  return(km_per_hour)

def convert(speed,direction):
    if direction == 'm':
        conv_speed = speed / conversion
        return(conv_speed)
    elif direction == 'k':
        conv_speed = speed * conversion
        return(conv_speed)
        

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
conv_speed = convert(speed, direction)
print(f'The converted speed is {conv_speed} {direction} per hour.')
