#contactbook
def addContact():
    # get the last key from the contacts and add 1 to it
    contact_order = list(contacts.keys())[-1] + 1
# get input from the user to be saved as a new contact
    while True:
        try:
            name = str(input("Enter contact name: "))
            number = int(input("Enter contact number: "))
            address = str(input("Enter contact address: "))
            # add data to contacts
            contacts[contact_order] = {
                "name" : "{}". format(name),
                "number" : number,
                "address" : "{}".format(address)
            }
            print("Data " + name + " added succesfully!\n")
            break
        except ValueError:
            print("Wrong input. Please enter a correct format.\n")
            break
elif option == 3:
print("\n===========")
print("Add Contact")
print("===========")
addContact() 
showMenu()

