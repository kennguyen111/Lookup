"""
 Ken Nguyen
version: 1.1

This program will prompt user to choose between lookup for phone number or addresses
then the program will ask for person's name and display the person's information


Input: 1 or 2 , then person's name
Output: full phone numbers or full addresses
"""
import sys



#1 function to read data file and create address/phone dictionary
def readFile():
    dictionary = {}
    try:
        file = open("address.txt", 'r')

    except:
        print("Error: file not found")
        sys.exit(1)
    else:
        while True:
            line = file.readline()
            if line == "":  # check if end of file
                break
            value = line # copy entire line as dictionary value
            line = line.lower()
            line = line.split(",", 1)  # get the first field (first and last name) of line for Key
            key = line[0]
            dictionary[key] = value #Create dictionary

    return dictionary


# display person 's information
def display(name ,dict, userInput=1): # default input is 1,  to print just the phone number
    name = name.lower()
    key = name
    if userInput == 1:
        if key in dict:
            list =  str(dict[key])
            list =  list.split(",")
            print("{0:<10}".format("Phone: ")+ list[5]) # to get phone number
        else:
            print("error: person not found")
    if userInput == 2:
        if key in dict:
            list = str(dict[key])
            list = list.split(",")
            print("{0:<10}".format("Street: ")+ list[1])
            print("{0:<10}".format("City: ") + list[2])
            print("{0:<10}".format("State: ") + list[3])
            print("{0:<10}".format("Zip Code: ") + list[4])
        else:
            print("error: person not found")

    if userInput !=1 and userInput!=2 : #default search for phone number
        if key in dict:
            list = str(dict[key])
            list = list.split(",")
            print("{0:<10}".format("Phone: ") + list[5])  # to get phone number
        else:
            print("error: person not found")






# main function, start of the program
def main():
    readFile()
    while True:
        try:
            userInput = input("Lookup (1) phone numbers or (2) addresses: ")
            if userInput == "" or userInput == " ":
                sys.exit(1)
            userInput = int(userInput)
            while True:
                name = str(input("Enter space-separated first and last name: "))
                if name == "" or name == " ":
                    sys.exit(1)
                display(name, readFile(), userInput)
        except ValueError:
            print("Please choose 1 or 2 or enter blank to exit")

if __name__ == "__main__":
    main()
