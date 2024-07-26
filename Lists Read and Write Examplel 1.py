# Program tests opening a CSV file and showing the contents

# test methods from https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/#:~:text=You%20can%20read%20a%20CSV,writing%20data%20in%20a%20CSV.

import csv

rows=[]
add = '.'

# set up an operating loop
while add != '':
    # ask for two options, add or print data
    add = input('Type Y to add a customer, N to print data: ')
    
    # this section to add a new customer
    if add == 'Y':
    
        # collect the customer data    
        custnum= input('Customer number : ')
        fname= input('First Name : ')
        lname= input('Last Name : ')
        phone = input('Phone number : ')
        address= input('Address : ')
    
        # make it into a record list
        recordlist = [custnum,fname,lname,phone,address]
        # show the list so we can see it
        print(f'Now storing record :{recordlist}')

        # this is the code to open the file and add the list as a new row. 
        with open('customerlist.csv','a', newline='') as file:  # the 'a' mode is for append
            writeCSV = csv.writer(file)     # set the filename variable for writing
            writeCSV.writerow(recordlist)   # write the new row

    else:  # this option just prints off the csv data
        with open('customerlist.csv','r') as file:
            readCSV = csv.reader(file)   # set the filename for reading only 

            # these two lines are to get the first row as a header (if it is used)
            #header = next(readCSV)
            #print(header)
        
            #loop to go through row by row
            for currentrow in readCSV:   
                rows.append(currentrow) #adds the current row data to the 'master' rows list
    
            print(rows)  # after all the rows are read, print the full set of data
            rows = []
            print ()
            print ()




#outputWriter = csv.writer(testCSV)
# orderReader = csv.reader(testCSV)

#while orderitem != '':
 #   orderitem=input('What would you like to order? ')
 #   if orderitem=='':
 #       break
  #  ordernumber=input('how many?')
   # orderlist=[orderitem, ordernumber]
  #  print(f'Thats {ordernumber} of {orderitem}...')
  #  outputWriter.writerow(orderlist)
    
#print()
#print('Your whole order is :')
#fullorderList = list(orderReader)

#for row in range(len(fullorderList)):
#    print(fullorderList[row])

 
 


