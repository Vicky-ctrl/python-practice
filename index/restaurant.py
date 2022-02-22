class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name, "is restaurant_name")
        print(self.cuisine_type, "is cuisine_type")

    def open_restaurant(self):
        print("is open")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num
