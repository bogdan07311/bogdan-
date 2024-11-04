class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 100  # рівень щастя
        self.energy = 100     # рівень енергії

    def feed(self):
        if self.energy < 100:
            self.energy += 10
            print(f"{self.name} поїв і відновив енергію! Тепер енергія: {self.energy}")
        else:
            print(f"{self.name} не голодний.")

    def play(self):
        if self.energy >= 20:
            self.happiness += 20
            self.energy -= 20
            print(f"{self.name} грає і стає щасливішим! Тепер щастя: {self.happiness}, енергія: {self.energy}")
        else:
            print(f"{self.name} втомлений і не може грати.")

    def sleep(self):
        self.energy = 100
        print(f"{self.name} спить і відновлює енергію. Тепер енергія: {self.energy}")

    def status(self):
        print(f"Ім'я: {self.name}, Вид: {self.species}, Щастя: {self.happiness}, Енергія: {self.energy}")

# Приклад використання
my_pet = Pet("Мурчик", "Котик")

my_pet.status()
my_pet.play()
my_pet.feed()
my_pet.sleep()
my_pet.status()