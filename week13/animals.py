class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    def speak(self):
        return "..."

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}"

    def speak(self):
        return "Woof!"
