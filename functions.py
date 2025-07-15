from classes import Staff
from classes import Hotel
def init_welcome():
    print("""
***********************************
          WELCOME TO
          MG RESORT MANAGER
*********************************** 
          """)
    print('\n Would you like to continue with your initial setup?[y/n]')
    init_answer = input(">").lower()

    while not (init_answer == "n" or init_answer == 'y'):
        print("!!!!!!")
        print(f"Sorry. {init_answer} is not a valid entry. Please try again.")
        print('\n Would you like to continue with your initial setup?[y/n]')
        init_answer = input(">").lower()
    
    if init_answer == 'n':
        quit()
    else:
        print("*" * 25)
        print("Since you are the first employee to use this system, we will create a staff profile for you.")
        print("Please follow the following prompts:")
        #####input validation functions will be created#########
        name = input('Name: ')
        position = input('Position: ')
        tenure = input('Years worked: ')
        salary = input('Salary: ')
        return_code = create_staff(name, position, tenure, salary)
        if return_code == 0:
            print("Perfect! You have been created as an employee!")
        else:
            print('There has been an error. Program will close.')
            quit()
    
    print('*' *25)
    print("Now we will need some information about the hotel. Please follow the prompts.")
    ######input validation function will be created######
    name = input('Name: ')
    ameneities = list(input('Ameneties(separated by commas): '))
    staff_count = input("Staff Count: ")
    staff_names = list(input('Staff names'))

    response_code = create_hotel(name, ameneities, staff_count, staff_names)

    if response_code == 0:
        print("Perfect. The Hotel information has been obtained")
    else:
        print('There has been an error. Program will close.')
        quit()


def create_staff(name, position, tenure, salary):
    try:
        name = Staff(name, position, tenure, salary)
        return 0
    except TypeError:
        print("ERROR CODE: 8899 --- create_staff function")
        quit()

def create_hotel(name, ameneities, staff_count, staff_names):
    try:
        name = Hotel(name, ameneities, staff_count, staff_names)
        return 0
    except TypeError:
        print("ERROR CODE: 8901 --- create_hotel function")
        quit()
