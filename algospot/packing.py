import sys


class Thing():
    def __init__(self, name="", volume=0, value=0):
        self.name = name
        self.volume = volume
        self.value = value

max_value = 0
max_things = []
things = []

def pack(limit, index, added_list):
    global max_value
    global max_things
    if index >= len(things):
        temp_value = 0
        for thing in added_list:
            temp_value += thing.value
        if temp_value > max_value:
            max_value = temp_value
            max_things = added_list
        return

    added_list = [w for w in added_list]
    thing = things[index]
    pack(limit, index + 1, added_list)
    added_list.append(thing)
    pack(limit - thing.volume, index + 1, added_list)

test_case = input()
case = 0
while case < test_case:
    # init global variable
    max_value = 0
    max_things = []
    # input
    temp_input = sys.stdin.readline().strip().split()
    num_things = int(temp_input[0])
    volume_limit = int(temp_input[1])

    # insert object to list
    things = []
    for i in range(num_things):
        temp_input = sys.stdin.readline().strip().split()
        things.append(Thing(temp_input[0], int(temp_input[1]), int(temp_input[2])))

    pack(volume_limit, 0, [])
    print(max_value, len(max_things))
    for thing in max_things:
        print(thing.name)
    case += 1