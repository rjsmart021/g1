class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    def update_owner(self, new_owner):
        self.owner = new_owner
class Event:
    def __init__(self, name, date):
        self.list_of_participants = []
        self.name = name
        self.date = date
    def add_participant(self, name, age):
       self.list_of_participants.append((name,age))
    def get_participant_count(self):
        return f"Number of participants{len(self.list_of_participants)}"
#Test 1
v1 = Vehicle( 44545, "Ferrari", "Gorla")
v1.update_owner("Margarette")
print(v1.owner)
#Test 2
event1 = Event("Event test", "2024-10-10")
event1.add_participant("daniel", 24)
print(event1.get_participant_count())
