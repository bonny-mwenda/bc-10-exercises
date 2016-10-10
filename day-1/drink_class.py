class Beverage(object):
    """Beverage class

    Methods:
    drink - decrement volume of the beverage
    price - set price of the beverage
    """

    def __init__(self, name, volume):
        """Initialize Beverage class

        Properties:
        name - name of the beverage
        volume - volume of the beverage
        """

        self.name = name
        self.volume = volume

    def drink(self, amount):
        """Decrement volume after drinking"""

        if amount > self.volume:
            return "Sorry, we can't serve you that amount of {0}".format(self.name)
        else:
            self.volume -= amount
            return "Cheers!" + " You have {0} units of {1} left".format(self.volume, self.name)

    def price(self):
        """set the price of the beverage"""

        self.__price = self.volume * 10
        return self.__price


class Alcohol(Beverage):
    """Alcohol class that inherits from Beverage

    Methods:
    drink - uses drink method inherited from beverage class
    price - sets the price of alcoholic drink
    """

    def __init__(self, name, type_, volume, age=None):
        """Initialize Drink class

        Properties:
        name - name of alcoholic drink
        volume - volume of drink
        type - example beer, wine, whisky
        age - number of years the grain has been aged
        """

        self.name = name
        self.volume = volume
        self.type_ = type_
        self.age = age

        # Set default age of the drink if not specified
        if not age:
            if self.type_ == "wine":
                self.age = 10
            elif self.type_ == "beer":
                self.age = 1.5
            elif self.type_ == "vodka":
                self.age = 2
            elif self.type_ == "whisky":
                self.age = 20
            else:
                self.age = 1
        else:
            self.age = age

    def price(self):
        """Set price of the drink"""

        self.__price = self.age * self.volume * 10
        return self.__price


