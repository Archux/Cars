class Car:
    def __init__(self, make, model, transmission, price, fuel, fuel_consumption):
        self.make = make
        self.model = model
        self.transmission = transmission
        self.price = price
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.engine_running = False
        self.engine_shut = True
        self.doors_open = False
        self.doors_closed = True
        self.moving = False
        self.stopped = True

    def __repr__(self):
        return(f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Transmission: {self.transmission}\n"
              f"Price: {self.price}\n"
              f"Fuel: {self.fuel}\n"
              f"Fuel Consumption: {self.fuel_consumption}\n")

    def start_engine(self):
        if self.engine_running:
            print(f"{self.make} {self.model} is already running.")
        else:
            print("Kle..kle..kle.. Wroomm!!!")
            self.engine_running = True
            self.engine_shut = False

    def stop_engine(self):
        if self.engine_running:
            print("Brum..pum..pu.. ... .. .")
            self.engine_running = False
            self.engine_shut = True
        else:
            print(f"{self.make} {self.model} engine is already off.")

    def open_doors(self):
        if self.moving:
            print("Please stop the car before opening doors!")
        elif self.doors_open:
            print("Doors are already open.")
        else:
            print("Opening doors.")
            self.doors_open = True
            self.doors_closed = False

    def close_doors(self):
        if self.doors_open:
            print("Closing doors..")
            self.doors_open = False
            self.doors_closed = True
        else:
            print("Doors are already closed")

    def car_drive(self, speed):
        if not self.engine_running:
            print("Turn on the engine first.")
        elif self.doors_open:
            print("Close the car doors before moving.")
        else:
            print(f"Car driving {speed}")
            self.moving = True
            self.stopped = False

    def stop_car(self):
        if self.stopped:
            print("Car already stopped")
        else:
            print("Stopping the car..")
            self.moving = False
            self.stopped = True

    def save_(self):
        with open ("cars.txt", "w") as f:
            f.write(f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Transmission: {self.transmission}\n"
              f"Price: {self.price}\n"
              f"Fuel: {self.fuel}\n"
              f"Fuel Consumption: {self.fuel_consumption}\n")


class UsedCar(Car):

    def __init__(self, make, model, year, transmission, price, fuel, fuel_consumption, milage):
        super().__init__(make, model, transmission, price, fuel, fuel_consumption)
        self.year = year
        self.milage = milage

    def __repr__(self):
        return (f"Make: {self.make}\n"
                f"Model: {self.model}\n"
                f"Year: {self.year}\n"
                f"Transmission: {self.transmission}\n"
                f"Price: {self.price}\n"
                f"Fuel: {self.fuel}\n"
                f"Fuel Consumption: {self.fuel_consumption}\n"
                f"Milage: {self.milage}\n")


C1 = Car("Audi", "A4", "Manual", 25000, 'Diesel', "6L/100km")
print(C1)

U1 = UsedCar("BMW", "320", "2004", "Automatic", 2000, "Petrol", "10L/100km", 150000)
print(U1)


U1.open_doors()
U1.close_doors()
U1.car_drive("fast")
U1.start_engine()
U1.car_drive("fast")
U1.stop_engine()
U1.car_drive("fast")
U1.stop_car()
U1.open_doors()
U1.stop_engine()
U1.open_doors()
U1.close_doors()
