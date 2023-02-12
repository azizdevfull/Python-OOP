class Transport:
    def __init__(self, brand, model, typer):
        self.brand = brand
        self.model = model
        self.typer = typer
    def info(self):
        print(f"Brand: {self.brand} Model: {self.model} Type: {self.typer}" )

class ElectroCars(Transport):
    
    def __init__(self,brand,model,typer, battery_life, chargin_time):
        super().__init__(brand, model,typer)
        self.battery_life = battery_life
        self.chargin_time = chargin_time
    def more_info(self):
        print(f"Brand: {self.brand} Model: {self.model} Type: {self.typer}:: Battery Life: {self.battery_life}, Chargin Time: {self.chargin_time}" )

class SportCars(Transport):
    
    def __init__(self,brand,model,typer,motor, color):
        super().__init__(brand, model,typer)
        self.motor = motor
        self.color = color
    def more_info(self):
        print(f"Brand: {self.brand} Model: {self.model} Type: {self.typer} ::  Motor: {self.motor}, Color: {self.color} " )

class Truck(Transport):
    
    def __init__(self,brand,model,typer,motor, height, longer, wieght):
        super().__init__(brand, model,typer)
        self.motor = motor
        self.height = height
        self.longer = longer
        self.wieght = wieght
    def more_info(self):
        print(f"Brand: {self.brand} Model: {self.model} Type: {self.typer} ::  Height: {self.height}, Long: {self.longer}, Weight: {self.wieght} " )


# tran = Transport(brand="Shevrolet", model="Nexia", typer="Transport")
# tran.info()

# elec = ElectroCars("Tesla", "Tesla x3","Transport",20,245)
# elec.more_info()

# sport = SportCars("Formula", "Formula 1","Transport","XRT-35","Red")
# sport.more_info()

truck = Truck(brand="Shevrolet", model="Nexia", typer="Transport",motor="XRT-35",height=172,longer=150,wieght=172)
truck.more_info()
