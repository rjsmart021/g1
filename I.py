 class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def update_owner(self, new_owner):
            self.owner = new_owner

       @classmethod
        def isinstance_Vehehicle():
            x = isinstance(Vehehicle, class)
            print(x)



class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
    list_of_participants = []
    @classmethod
    def Add_Participant(name, age):
       return list_of_participants.append()
       print(list_of_participants)
    @classmethod
    def get_participant_count(cls):
        return f"Number of participants: 
        {len(cls.list_of_participants)}"


#Test 1
v1 = Vehicle_1
v1.reg_num = 44545
v1.type = "Ferrari"
v1.owner ="Gorla"
print(Vehicle)
#Test 2
E1 = Event_1
E1.name = "Foko"
E1.date = 8/9/2023
Add_Participant("John", 36)
get_participant_count(cls)
