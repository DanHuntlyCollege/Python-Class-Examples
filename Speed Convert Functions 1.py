# This program shows how to use a function
# it will convert km/hr to miles / hr

conversion= float(0.621371)


# first we need to define the function
def convert_to_miles(km_speed):
    miles_per_hour=km_speed * conversion
    return(miles_per_hour)

#now we make our main program
km_speed = int(input('Speed to convert (in km/hr) ? : '))

mph_speed = convert_to_miles(km_speed)

print(f'The converted speed is {mph_speed} miles per hour.')