
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f'Starting the {self.year} {self.make} {self.model}')

    def drive(self):
        print(f'Driving the {self.year} {self.make} {self.model}')

    def stop(self):
        print(f'Stopping the {self.year} {self.make} {self.model}')
