class Texnika: 
    def __init__(self, brand):
        self.brand = brand

class Notebooks(Texnika):
    def __init__(self,brand,video_card):
        super().__init__(brand)
        self.video_card = video_card
    def more_info(self):
        print(self.brand)
note = Notebooks('Samsung', 'nvdia')
note.more_info()