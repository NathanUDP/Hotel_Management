from classes import Staff
from classes import Hotel
from classes import Amenitieis
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
        tenure = float(tenure)
        salary = float(salary)
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
    room_count = input('Room count: ')
    ameneities = list(input('Ameneties(separated by commas): '))
    staff_count = input("Staff Count: ")
    staff_names = list(input('Staff names(separated by commas):'))

    staff_count = int(staff_count)
    room_count = int(room_count)

    response_code = create_hotel(name, room_count, ameneities, staff_count, staff_names)

    if response_code == 0:
        print("Perfect. The Hotel information has been obtained")
    else:
        print('There has been an error. Program will close.')
        quit()
    
    #Staff creation
    
    i = 0
    #INPUT VALIDATION#
    while i < len(staff_names):
        name = staff_names[i]
        print(f'What is the position of {name}?')
        position = input(">")
        print(f'What is the tenure(in years) for {name}?')
        tenure = input('>')
        print(f'What is the salary for {name}?')
        salary = input('>')

        tenure = float(tenure)
        salary = float(salary)

        response_code = create_staff(name, position, tenure, salary)

        if response_code == 0:
            print("""
************************************************
Employee '{name}' has been successfully created
************************************************
                  """)
            i += 1
        else:
            print("!!!!There has been an error. Program will automatically close.")
            quit()
    print("""
********************
    All Employees
Have Been Created!!!
********************
          """)
    
    print("Next we will create the available amenities for your hotel.")
    print("*" * 25)

    #Create Amneities
    #Input validation will be added

    while i < len(ameneities):
        name = ameneities[i]
        print(f'Is it include in basic room & board?')
        included = input('>')
        print(f'Which staff members work in this amenetity?(separated by commas)')
        managed_staff = list(input('>'))
        for staff in managed_staff:
            while staff not in Staff.all():
                print(f'{name} is not in the current staff list. Please correct the staff list. (separated by commas)')
                managed_staff = list(input('>'))
        
        response_code = create_amenetity(name, included, managed_staff)

        if response_code == 0:
            continue
        else:
            print('!!!!An error has occured. Closing program automatically.')
            quit()
    try:
        with open('init_complete_file', 'w') as init_comp:
            init_comp.write('Initial completed ******')
    except FileExistsError:
        print('ERROR CODE: 4888 init_complete_file already exists. Bug in init_welcome function')

def create_staff(name, position, tenure, salary):
    try:
        name = Staff(name, position, tenure, salary)
        return 0
    except TypeError:
        print("ERROR CODE: 8899 --- create_staff function")
        quit()

def create_hotel(name, room_count, ameneities, staff_count, staff_names):
    try:
        name = Hotel(name, room_count, ameneities, staff_count, staff_names)
        return 0
    except TypeError:
        print("ERROR CODE: 8901 --- create_hotel function")
        quit()

def create_amenetity(name, included, staff_names):
    try:
        name = Amenitieis(name, included, staff_names)
        return 0
    except TypeError:
        print('ERROR CODE: 8902 --- create_amenetity function')
