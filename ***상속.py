import math

 

class Animal:

    def __init__(self, age, height, color, xpos, ypos):

        self.age = age

        self.height = height

        self.color = color

        self.xposition = xpos

        self.yposition = ypos

        self.velocity = 0

 

    def sound(self):

        pass

 

class Horse(Animal):

    def __init__(self, age, height, color, xpos, ypos):

        Animal.__init__(self, age, height, color, xpos, ypos)

 

    def sound(self):

        print('Neigh')

 

    def run(self, xdistance, ydistance, time):

        self.xposition += xdistance

        self.yposition += ydistance

        total_distance = math.sqrt((xdistance + xdistance) * (ydistance + ydistance))

        self.velocity = total_distance/time

 

class Dog(Animal):

    def __init__(self, age, height, color, xpos, ypos):

        Animal.__init__(self, age, height, color, xpos, ypos)

 

    def sound(self):

        print('Bow-Wow')

 

if __name__ == '__main__':

    danbi = Horse(5, 160, 'brown', 0, 0)

    choco = Dog(10, 100, 'black', 50, 30)

    danbi.sound()

    choco.sound()
