# This program is to allow a username and password to be entered, to allow access to something


# set up a dictionary to hold the data.
logindict = {'Dan':'123', 'Kiri':'456','Rob':'678','Tama':'234','Kahu':'789'}

# setup a list to hold a user and password pair
user = ''
password = ''
login=[user,password]
accessallowed = False

# This function should ask the user for a username, and password, and pass those back to the program
def getlogin():


# this function should receive a username and password pair, in a list (called 'login')

def checklogin(login):
# Then it needs to say 'Checking login details...'

# next it needs to get the username out of the list (login) that it got handed as an argument, and store it.
        username = login[0]

# next, it needs to through the dictionary called 'logindict', and get the password paired with that username
        password = logindict[user]
# next it compares the looked up username to the one from the list it got handed to see if they match 
        if .........  == login[1]:
            
# if they do, print 'Access allowed! '

# otherwise, print 'Access DENIED! '


# Main program - uses a WHILE function to keep going until accessallowed = True
# program just calls the two funtions to get a login, then check the login
while accessallowed == False
    login=getlogin()
    checklogin(login)
