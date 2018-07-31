#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = ["Hamburger", "Hot Dog", "Salad", "Chicken", "Fish", "Soup", "Pancakes", "Spaghetti", "Pizza"]
dList = ["Ice Cream", "Brownies", "Cookies", "Mochi Ice Cream", "Strawberry Shortcake", "Pie", "Shaved Ice", "Soft Serve"]
fList = ["Apple", "Banana", "Mango", "Grapes", "Watermelon", "Pineapple", "Strawberry", "Pear"]
#Generates a random integer.

response = input("Would you like to eat today? (Y/N)")
while response != "N" :
    if response == "Y" :
        aRandomIndex = randint(0, len(aList)-1)
        dRI = randint(0, len(dList)-1)
        fLI = randint(0, len(fList)-1)
        print("{}, {}, {}.".format(aList[aRandomIndex], dList[dRI], fList[fLI]))
    else :
        print("{} is an invalid input.".format(response))
    response = input("Would you like to eat today? (Y/N)")
