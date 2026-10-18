class Event:
    def __init__(self, name, category, date, location, capacity, registered):
        if type(name) is not str:
            raise TypeError("Event name must be a string.")

        if type(category) is not str:
            raise TypeError("Event category must be a string.")

        if type(date) is not str:
            raise TypeError("Event date must be a string.")

        if type(location) is not str:
            raise TypeError("Event location must be a string.")

        if type(capacity) is not int:
            raise TypeError("Capacity must be an integer.")

        if type(registered) is not int:
            raise TypeError("Registered count must be an integer.")
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")

        if registered < 0 or registered > capacity:
            raise ValueError("Registered count must be between 0 and capacity.")
        if not name.strip():
            raise ValueError("Event name cannot be empty.")

        if not category.strip():
            raise ValueError("Event category cannot be empty.")

        if not date.strip():
            raise ValueError("Event date cannot be empty.")

        if not location.strip():
            raise ValueError("Event location cannot be empty.")

        self.name = name
        self.category = category
        self.date = date
        self.location = location
        self.capacity = capacity
        self.registered = registered

    def display(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Date: {self.date}")
        print(f"Location: {self.location}")
        print(f"Capacity: {self.capacity}")
        print(f"Registered: {self.registered}")

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "date": self.date,
            "location": self.location,
            "capacity": self.capacity,
            "registered": self.registered
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["category"],
            data["date"],
            data["location"],
            data["capacity"],
            data["registered"]
        )
    def register(self):
        if not self.is_full():
            self.registered += 1
            return True
        return False
    def cancel_registration(self):
        if self.registered > 0:
            self.registered -= 1
            return True

        return False

    def is_full(self):
        return self.registered >= self.capacity