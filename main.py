class Car:
    speed = 100
    weight = 250
    value = 1000
    skid = 90
    manufacturability = 100
class Tesla(Car):
    super().speed += 20
    super().weight += 120
    super().skid += 20
    super().manufacturability += 20
class TeslaX(Tesla):
    carbon = 10
    super().speed += 20

class Mazda(Car):
    super().speed += 50
    super().weight -= 10
    super().skid -= 15
    super().manufacturability += 5

class Nissan(Car):
    super().speed += 5
    super().weight += 50
    super().skid += 30
    super().manufacturability -= 20

class Honda(Car):
    super().speed -= 10
    super().weight += 120
    super().skid -= 50
    super().manufacturability += 5