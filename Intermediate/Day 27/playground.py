def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(1,2,3,4,5,6,7,8))


def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


calculate(add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.year = kw.get("year")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model, my_car.year)

