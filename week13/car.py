class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

    def set_year(self, new_year):
        if(new_year < 1900): 
            print("Invalid year")
            return
        self.year = new_year
