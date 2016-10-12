# Andela BootCamp 10 Exercises

This repo contains the expected outputs of Andela Bootcamp 10. The outputs have been sorted in folders corresponding to their respective days. Unittests of each file can be found in a sub-folder named 'tests' for each day.

All exercises have been done using `python 3.4`. In case you need to clone this repo to your local drive, copy this code to your terminal.

`$ git clone git@github.com:bonny-mwenda/bc-10-exercises.git`

Below is a description of what each of the folders contain.

## Clinic
This contains exercises for Andela Bootcamp 10 self learning clinic.

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
A simple application that gives Nairobi's five day weather forecast for every three hours using a Public API. The API used is the OpenWeatherMap, and the response is in JSON format. Python's `requests` library is used to send the GET request.

## Day 3
This folder contains a simple web page where boot campers can rate their experience at Andela. The rating considers Andela facilities and the help/assistance provided by the facilitators. See a screenshot of the interface below:

![Feedback Form Screenshot](https://cloud.githubusercontent.com/assets/19901453/19316849/b16266e8-90ab-11e6-9632-b1d58c548748.png)
