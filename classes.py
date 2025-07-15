#Create parent class HOTEL
#All Debug prints will be removed once GUI has been created
class Hotel:
    def __init__(self, name: str, room_count: int, amenities: list, staff_count: int, staff_names: list):
        assert room_count >= 0
        assert staff_count >= 0
        self.name = name
        self.room_count = room_count
        self.amenitieis = amenities
        self.staff_count = staff_count
        self.staff_names = staff_names
    
    def get_info(self):
        #####DEBUG PRINT#####
        print("""
Hotel Name: {self.name}
Hotel Room Count: {self.room_count}
Hotel Available Amenities: {self.amenitites}
Hotel Staff Count: {self.staff_count}         
            """)
    
    def get_employee_info(self):
        employee_names_format = self.staff_names.join(",")
        ######DEBUG PRINT#######
        print("""
Hotel Staff Count: {self.staff_count}
Hotel Staff Names: {employee_names_format}
              """)

#class hotel room, contains information about each hotel room
class Hotel_room:
    all = []
    
    def __init__(self, name: str, bed_count: int, amenitieis: list, price: float, availability: bool):
        assert bed_count >= 0
        assert price >= 0
        self.name = name
        self.bed_count = bed_count
        self.amenitieis = amenitieis
        self.price = price
        self.availability = availability
        #Appends to list of the class attribute all (for looping logic)
        Hotel_room.all.append(self)
    
    def get_info(self):
        ########DEBUG PRINT#######
        print("""
Name: {self.name}
Bed count: {self.bed_count}
Amenities: {self.amenitieis}
Price: {self.price}/night
Available: {self.availability}
              """)
    def discount_room(self, discount: float):
        self.price = self.price - (self.price * discount)
        #####DEBUG PRINT#######
        print(f"Room has been discounted to {self.price}")

class Amenitieis:
    all = []

    def __init__(self, name: str, included: bool, staff: list):
        self.name = name
        self.included= included
        self.staff = staff
        #Appends to list of the class attribute all (for looping logic)
        Amenitieis.all.append(self)

class Staff:
    all = []

    def __init__(self, name: str, position: str, tenure: float, salary: float):
        assert tenure > 0
        assert salary >= 0
        self.name = name
        self.position = position
        self.tenure = tenure
        self.payrate = salary

        Staff.all.append(self)
