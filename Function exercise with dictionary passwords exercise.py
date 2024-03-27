# This program is to allow a username and password to be entered, to allow access to something


# set up a dictionary to hold the data.
logindict = {'Dan':'123', 'Kiri':'456','Rob':'678','Tama':'234','Kahu':'789'}

# setup a variable to show if the user has been allowed in yet
accessallowed = False   # this is Boolean and shows if the user is allowed acces yet


def checklogin(user,password):
# Then it needs to say 'Checking login details...'

# Lookup the user name and see if they are in the list

# if they are in the list. If they are not, go back to the main program

# next, it needs to through the dictionary called 'logindict', and get the password paired with that username
    
# next it compares the looked up username to the one from the list it got handed to see if they match 
      
            
# if they do, print 'Access allowed! '

# otherwise, print 'Access DENIED! '


# Main program - uses a WHILE function to keep going until accessallowed = True
# program just calls the two funtions to get a login, then check the login
while accessallowed == False
  # first go and ask the user for a username and password
  
    checklogin(user,password) #send the username and passsword to the fuction to look up and see if its correct 
