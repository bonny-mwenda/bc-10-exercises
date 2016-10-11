# Andela BootCamp 10 Exercises

## Self Learning Clinic
### Prime Numbers
This is an implementation of a function that returns a list of the first n prime numbers, where n is any integer value.
Example: Given `n = 5`
>Result: `[2, 3, 5, 7, 11]`

### Fibonacci Numbers
This is a function that returns a list of the first n fibonacci numbers
Example: Given `n = 10`
>Result: `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`

## Day 1

Contains exercises illustrating OOP concepts. Two classes have been used as examples: Beverage and Alcohol

### Beverage Class
This is the base class. Takes two properties: name and volume of the beverage instance.
Methods:
* drink - decrements volume of the beverage by the quantity passed
* price - sets the price of the beverage based on volume

### Alcohol class
Inherits from Beverage class. Has the properties, name, volume, type and age.
Methods:
* drink - uses the inherited method from beverage class to decrement volume when the beverage is drank
* price - sets the price based on age of the drink

## Day 2
A simple application that gives a weather forecast using a Public API. The API used is the OpenWeatherMap, and the respomse is a JSON. Python's `requests` library is used to send the GET request.

