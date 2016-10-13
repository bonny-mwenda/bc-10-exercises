class Car(object):
    """Boiler plate for creating cars"""

    def __init__(self, name=None, model=None, type_=None):
        """Initialize car instance

        Attributes:
        name = car name
        model = make of car
        type_ = type of car, eg saloon or trailer
        """
        super(Car, self).__init__()
        self.name = name
        self.model = model
        self.type_ = type_
        self.num_of_doors = 4
        self.num_of_wheels = 4
        self.speed = 0

        if not self.name:
            self.name = "General"
        if not self.model:
            self.model = "GM"

        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.num_of_doors = 2

        if self.type_ == "trailer":
            self.num_of_wheels = 8

    def is_saloon(self):
        if self.type_ != "trailer":
            self.type_ = "saloon"
        else:
            self.type_ = "trailer"
        return self.type_

    def drive(self, speed):
        if self.type_ == "trailer":
            moving_speed = speed * 11
        else:
            moving_speed = 10 ** speed
        self.speed = moving_speed
        return self
