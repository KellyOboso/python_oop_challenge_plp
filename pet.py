class Pet:
    def _init_(self, name):
        self.name = name
        self.hunger = 0  
        self.energy = 10  
        self.happiness = 5  
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness += 1
        print(f"{self.name} is eating...")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
            print(f"{self.name} is playing...")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"{self.name}'s current status: "
              f"Hunger: {self.hunger}, "
              f"Energy: {self.energy}, "
              f"Happiness: {self.happiness}, "
              f"Tricks: {self.tricks}")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}")

    def show_tricks(self):
        print(f"{self.name} knows the following tricks: {', '.join(self.tricks) if self.tricks else 'None'}")
 
