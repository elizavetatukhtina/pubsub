class Bus():
    def __init__(self):
        "setting empty dict to store rooms"
        self.rooms = {}

    def subscribe(self, room, who):
        "add new subscriber to a certain room"
        if not self.rooms.get(room):  # if the room doesn't exist - add it
            self.rooms[room] = []
        self.rooms[room].append(who)

    def publish(self, room, data):
        "sending data to all subscribers of a certain room"
        if self.rooms.get(room):  # checking if the room exists
            for instance in self.rooms[room]:
                instance(data)


class Subscriber():
    def __init__(self, name):
        "setting string to name field"
        self.name = name

    def __call__(self, data):
        "making instance callable"
        print('{} got message "{}"'.format(self.name, data))
