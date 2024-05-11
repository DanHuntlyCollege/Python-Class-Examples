# Dictionary Validation checker


pricedict={'Cheese':9.90,'Eggs':4.50,'Bread':3.40,'Milk':3.00}
item='.'

# unvalidated example - this will error and crash if you enter anything that's not in the dictionary
while item != '':
    item=input('Item ? ')
    price=pricedict[item]
    print(f'The price of {item} is ${price}')

    



# Validated (checked) example

#while item != '':
#    item=input('Item ? ')
#    if item in pricedict:
#        price=pricedict[item]
#        print(f'The price of {item} is ${price}')
#    else:
#        print(f'Sorry, we dont have {item}.')
    
