# this program exercise is to look up a dictionary of items, and find the price for each.

# This section sets up the price dictionary and some variables we will use. 
# this is the list of items and prices - ALL CAPS name because its a constant
PRICEBOOK = {'Burger':6.5, 'Chips':4.8, 'Drink':2.0, 'Pie':3.5, 'Fish':5.5, 'Sausage':2.8}
# this list is a blank order, ready to add stuff to
order= []
# this is a not blank item so the input While loop will start
item = '.'
# this is a zeroed out total before anything is ordered
total = float(0)

# This function will look up any item and get its price - add code to finish it.
def findprice(item):
            # Write the dictionary lookup here to search for the itme, and give the matching price   
    return(price)  # send back the price here


# This is the main program
# first, take the order and store it in a list. 
while item:   # keep asking until there is a blank order
    
    item = input('What would you like to order ? ')   # get the name of an item
                   # if it's blank,
                   # finish the order
    
    if item in PRICEBOOK:    # check if the item is in the pricelist
                             # if it is, write a command to add it to the order
                             # next, call the 'findprice' function to get the price
                             
       print(f'One {item} is $ {price}.')  # now you tell them the item and the price
        
    else:  # what to do if the item isn't in the pricebook. 
        print(f"Sorry we don't sell {item} here.")

print(order)    # this is a check at the end of the order, to make sure that the list is good. 

# second print out the order and prices and a total
print()                                 # this leaves a blank line
print(' ********  Order *********  ')   # this is like a title 
for item in order:    #loop through all the items in the order list
                # write code to call the 'findprice' function to look up the price of each item in the order list
                # write code to add that price to the order total
    print(f'Item:  {item}    $ {price} ')    # print a receipt line, with the item and price
print( '-------------------------------')
print(f' TOTAL          $ {total}')       # print a final line to give the order total
print('   Thank you for your business!')
