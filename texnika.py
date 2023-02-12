class Texnika:
    def __init__(self, brand, model, typer):
        self.brand = brand
        self.model = model
        self.typer = typer
    def info(self):
        print(f"Brand: {self.brand} Model: {self.model} Type: {self.typer}" )
        
class Notebooks(Texnika):
    
    def __init__(self,brand,model,typer, video_card, ram, display):
        super().__init__(brand, model,typer)
        self.video_card = video_card
        self.ram = ram
        self.display = display
    def more_info(self):
        print(f"Brand: {self.brand} Model: {self.model} Type: {self.typer}:: Video Crad: {self.video_card}, Ram: {self.ram}, Display: {self.display} " )

class Televisions(Texnika):
    
    def __init__(self,brand,model,typer,size, display):
        super().__init__(brand, model,typer)
        self.size = size
        self.display = display
    def more_info(self):
        print(f"Brand: {self.brand} Model: {self.model} Type: {self.typer} ::  Size: {self.size}, Display: {self.display} " )

class Smartphones(Texnika):
    
    def __init__(self,brand,model,typer,size, sim_count):
        super().__init__(brand, model,typer)
        self.size = size
        self.sim_count = sim_count
    def more_info(self):
        print(f"Brand: {self.brand} Model: {self.model} Type: {self.typer} ::  Size: {self.size}, Sim Count: {self.sim_count} " )



# tex = Texnika(brand="Telephone", model="A6", typer="Samsung")
# tex.info()
# note = Notebooks("Samsung", "A6","Telephone","nvdia",16,"iris")
# note.more_info()
# tel = Televisions("Samsung", "M3","Polski", 16,"Full")
# tel.more_info()

tel = Smartphones("Apple", "Iphone 14", "Phone",32,2)
tel.more_info()