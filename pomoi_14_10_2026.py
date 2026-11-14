class Animal:

    def make_meat(self):
        return self.mass

    def make_milke(self):
        return round(self.mass * 0.02) , "литров"

    def how_to_run(self):
        return round(self.speed * 2)

class Cow(Animal):

    counter = 0

    def __init__(self, mass: int):
        Cow.counter += 1
        self.id = Cow.counter
        self.mass = mass



    def __str__(self):
        return (f'у вашей коровки {self.id}, масса столькото {self.mass}, а молочка с нее надоили {self.make_milke()}\n'
                f'мяса с коровы  {self.id} - {self.make_meat()}')

class Horses(Animal):

    counter = 0

    def __init__(self, mass: int, speed):
        Horses.counter += 1
        self.id = Horses.counter
        self.mass = mass
        self.speed = speed

    def make_milke(self): return f"прекрасное существо с ногми и вымем еще и молоко дает {self.make_milke()}"

    def __str__(self):
        return f"все норм{self.id, self.mass, self.how_to_run()}"

if __name__ == '__main__':
    cow1 = Cow(654)
    cow2 = Cow(546)
    print(f"{cow1}\n{cow2}")
    hors1 = Horses(200, 60)
    hors2 = Horses(201,80)
    print(hors1)
    print(hors2)

