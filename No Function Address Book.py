#  
#  Break this program up into functions.
#

#  set up two empty lists and the option variable
namelist=[]
numberlist=[]
option = ''

# write a 'save number' funtion here


# write a 'lookup number' function here



# write the new function driven program here



# original program here - comment out this code as you set up the new function driver version


while option != 'q':  # this loops the option question till you press q
    
    option= input('Do you want to add a number (press +) or lookup numbers (press ?), or q to quit' )

    if option == '+': 								# this section adds names and numbers to the lists
        name = input('What name to add ? ')			# ask for name
        number = input('What is their number ? ')	# ask for number
        namelist.append(name)						# add the name to the name list
        numberlist.append(number)					# add the number to the number list

elif option == '?':								# this section looks up names and finds numbers
        find = input('What name to find? ')		# get what name to find, store in variable 'find'
        for x in range(len(namelist)):          # loop through the list to the end
            lookupname = namelist[x]			# get the next name from the list
            if lookupname == find:				# check if the name is the one being looked for
                lookupnumber = numberlist[x]	# if it is, get the matching number
                print(f'Name: {lookupname}, Number: {lookupnumber} ')   # print the name and number together
                break     						# when the number is found, break out of the loop, carry on. 
        






