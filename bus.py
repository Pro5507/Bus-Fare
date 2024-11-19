class bus():
    def __init__(self, name, seats, from_to):
        self.name= name
        self.seats= seats
        self.from_to= from_to
    def run(self):
        print(self.name, self.seats, self.from_to)
obj= bus("Tata", 20, "Delhi to Agra")
obj.run()