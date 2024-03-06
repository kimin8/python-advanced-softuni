from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        result = room.take_room(people)
        if not result:
            self.guests += people

    def free_room(self, room_number: int):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        people_in_room = room.guests
        result = room.free_room()
        if not result:
            self.guests -= people_in_room

    def status(self) -> str:
        free_rooms = list(filter(lambda r: not r.is_taken, self.rooms))
        taken_rooms = list(filter(lambda r: r.is_taken, self.rooms))

        free_nums = []
        for room in free_rooms:
            free_nums.append(f"{room.number}")

        taken_nums = []
        for room in taken_rooms:
            taken_nums.append(f"{room.number}")

        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_nums)}\n" \
               f"Taken rooms: {', '.join(taken_nums)}"
