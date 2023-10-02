def badge_maker(name):
    return
    ("Hello, my name is " + name + ".")

def batch_badge_creator(names):
    return 
    badge_messages = []
    for name in names:
        badge_messages.append("Hello, my name is " + name + ".")
    return badge_messages

def assign_rooms(names):
    return 
    room_assignments = []
    for index, names in enumerate(names, start=1):
        room_assignment = (f"Hello, {name}! You'll be assigned to room {index}!")
        room_assignments.append(room_assignment)
    return room_assignments

def printer(names):
    return 
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for message in badge_messages:
        print(message)

    for assignment in room_assignments:
        print(assignment)
