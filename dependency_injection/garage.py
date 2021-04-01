class Garage:

    def __init__(self, vehicle):
        self.vehicle = vehicle

    def use_vehicle(self):
        try:
            self.vehicle.start()
            self.vehicle.drive()
            self.vehicle.stop()
        except:
            print('Looks like this isnt a vehicle!')
