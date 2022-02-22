# 5-9
# accounts = ['xiaoming', "xiaoli", "xiaowang", "admin"]
# if accounts:
#     for account in accounts:
#         if account == "admin":
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print("Hello" + "account, thank you for logging in again")
# else:
#     print("We need to find some users!")

# 5-10
# current_users = ['xiaoming', "xiaoli", "xiaowang", "Admin", "tom", "xiaosu"]
# new_users = ['xiaoming', "Xiaoli", "Alice", "admin", "Tom"]
# for index_1, user_1 in enumerate(current_users):
#     current_users[index_1] = current_users[index_1].lower()
# for index_2, user_2 in enumerate(new_users):
#     new_users[index_2] = new_users[index_2].lower()
# for user_1 in new_users:
#     if user_1 in current_users:
#         print("Sorry, " + user_1 + " had already been used!")
#     else:
#         print("Create " + user_1 + " succeed!")

# 5-11
# numbers = range(1, 10)
# for number in numbers:
#     if number == 1:
#         print('1st')
#     elif number == 2:
#         print('2nd')
#     elif number == 3:
#         print('3rd')
#     elif number > 3:
#         print(str(number) + 'th')
# print("done")

# 6-1
# person = {
#     'first_name': 'Vicky',
#     'last_name': 'Hou',
#     'age': '26',
# }
# print(person['last_name'], "is person's name")

# 6-4
# friends = {
#     'Tim': 1,
#     'Tom': 2,
#     'Vicky': 7,
# }
# for friend in friends.keys():
#     words = friend + "'s favorite number is " + str(friends[friend])
#     print(words, "is words")

# 9-13引入库，重写
# from collections import OrderedDict
# friends = OrderedDict()
# friends['Tim'] = 1
# friends['Tom'] = 2
# friends['Vicky'] = 7
# for friend in friends.keys():
#     words = friend + "'s favorite number is " + str(friends[friend])
#     print(words, "is words")
# print("success main")

# 6-6
# favorite_languages = {
#     'jen': 'java',
#     'tim': 'C',
#     'tom': 'python',
#     'vicky': 'javascript'
# }
# confirmed_accounts = ['tim', 'tom']
# for name in favorite_languages.keys():
#     if name in confirmed_accounts:
#         print('Thanks ' + name.title() + '.')
#     else:
#         print('Sorry ' + name.title() + '.')

# 6-7
# person = {
#     'first_name': 'Vicky',
#     'last_name': 'Hou',
#     'age': '26',
# }
# people = [
#     {
#         'first_name': 'Vicky',
#         'last_name': 'Hou',
#         'age': '26',
#     },
#     {
#         'first_name': 'Tom',
#         'last_name': 'Su',
#         'age': '27',
#     },
#     {
#         'first_name': 'Alex',
#         'last_name': 'Liu',
#         'age': '28',
#     },
# ]
# for person in people:
#     for key in person.keys():
#         print(key + ' : ' + person[key])

# 6-11
# cities = {
#     'Shanghai': {
#         'country': 'China',
#         'population': 111111,
#         'fact': '金融中心',
#     },
#     'Landon': {
#         'country': 'England',
#         'population': 22222,
#         'fact': 'gentle',
#     },
#     'Paris': {
#         'country': 'France',
#         'population': 22222,
#         'fact': 'fashion',
#     },
# }
# for name, city in cities.items():
#     for key, item in city.items():
#         print(name + "'s " + key + " is " + str(item))

# 7
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message, "is me")
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name?"
# name = input(prompt)
# print("\nHello, " + name + "!")

# 7-1
# prompt = "Let me see if I can find you a: "
# print(input(prompt))

# 7-2
# prompt = "How many people: "
# number = input(prompt)
# if int(number) > 8:
#     print("Sorry")
# else:
#     print("OK")

# 7-3
# prompt = "Input a number: "
# number = input(prompt)
# if int(number) % 10 == 0:
#     print("是 10 的整数倍")
# else:
#     print("不是 10 的整数倍")

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# active = True
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#         break
#     else:
#         print(message)

# 7-4
# prompt = "\nTell me something, and We will add it to the pizza:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# active = True
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#         break
#     else:
#         print("We will add it to the pizza:" + message)

# 7-5
# prompt = "\nEnter 'quit' to end the program."
# prompt += "\nTell me your age:"
# message = ""
# active = True
# if active:
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#         break
#     elif int(message) < 3:
#         print("The price: Free")
#     elif (int(message) >= 3) and (int(message) < 12):
#         print("The price: 10")
#     else:
#         print("The price: 15")


# 7-7
# message = 1
# while message <= 5:
# # 下面这行注释掉就是无限循环
#     message += 1
#     print(message)

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     confirmed_users.append(current_user.title())
#     print(confirmed_users, unconfirmed_users, "is confirmed_users")

# 7-8
# 7-9
# sandwich_orders = ['cheese', "pastrami", "egg", "beef", "pastrami", "pastrami"]
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     if sandwich != "pastrami":
#         finished_sandwiches.append(sandwich)
#         print("I made your " + sandwich + "sandwich")
# print(sandwich_orders, finished_sandwiches, "is finish")

# 8-6
# def city_country(city, country):
#     """国家和城市"""
#     result = city + ',' + country
#     return result
#
#
# print(city_country('Pairs', 'France'))

# 8-7
# def make_album(singer, album, num="7"):
#     result = {
#         'singer': singer,
#         'album': album,
#         'num': num,
#     }
#     return result
#
#
# re_1 = make_album('JJ', 'name', "99")
# re_2 = make_album('JZ', 'nananak')
# print(re_1, re_2, "is rereee")


# 8-8
# def get_album():
#     print("随时按 'q' 退出")
#     while True:
#         singer = input('请输入歌手名称')
#         if singer == 'q':
#             break
#         else:
#             album = input('请输入专辑名称')
#             if album == 'q':
#                 break
#             else:
#                 return make_album(singer, album)
#
#
# re = get_album()
# print(re)


# 8-9
# def show_magicians(items):
#     """打印所有魔术师的名字"""
#     for item in items:
#         print(item)


# 8-10 8-11
# def make_great(name):
#     """美国魔术师名字都加上 the Great, 并且传递副本，存到另一个列表，打印前后两个列表"""
#     result_name = "the Great " + name
#     return result_name
#
#
# magicians = ['Tim', 'Tom', 'Alex']
# magicians_copy = []
# show_magicians(magicians)
# for magician in magicians:
#     magicians_copy.append(make_great(magician))
# show_magicians(magicians_copy)
# print(magicians, magicians_copy, "is pre next")


# 8-12
# def ordered_sandwiches(*foods):
#     """收集提供的所有食材，调用三次，打印一条信息，所点菜单的概述"""
#     message = ""
#     for food in foods:
#         message = message + food + ' '
#     result = "You ordered: " + message
#     print(result)
#
#
# ordered_sandwiches('beef', 'tomato', 'egg')


# 8-13
# def build_profile(first, last, **user_info):
#     """简介，指定参数和三个键值对"""
#     profile = dict()
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
#
# print(build_profile('Vicky', 'Hou', location="auto", age="26"))


# 8-14
# def make_car(brand, model, **more_info):
#     print(1)
#     car_info = dict()
#     car_info['brand'] = brand
#     car_info['model'] = model
#     for key, value in more_info.items():
#         car_info[key] = value
#     return car_info


# 9-1 9-4
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name, "is restaurant_name")
#         print(self.cuisine_type, "is cuisine_type")
#
#     def open_restaurant(self):
#         print("is open")
#
#     def set_number_served(self, num):
#         self.number_served = num
#
#     def increment_number_served(self, num):
#         self.number_served += num


# re = Restaurant("yoyo", "Chinese Food")
# print(re.number_served, "is pre num")
# re.number_served = 77
# print(re.number_served, "is num")
# re.set_number_served(99)
# print(re.number_served, "is after")
# re.increment_number_served(101)
# print(re.number_served, "is inc")


# 9-3 9-5
# class User():
#     def __init__(self, first_name, last_name, **other_info):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#         # if other_info:
#         #     for key, info in other_info.items():
#         #         self[key] = info
#         #         print("user's " + key + "is " + info)
#
#     def describe_user(self):
#         print("info is", self.first_name, self.last_name)
#
#     def greet_user(self):
#         print("Hello, ", self.first_name + " " + self.last_name)
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# user = User("Vicky", "Hou", age="8", location="Beijing")
# user.increment_login_attempts()
# user.increment_login_attempts()
# print(user.login_attempts, "is login1")
# user.reset_login_attempts()
# print(user.login_attempts, "is login2")


# 9-6
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name, "is restaurant_name")
#         print(self.cuisine_type, "is cuisine_type")
#
#     def open_restaurant(self):
#         print("is open")
#
#     def set_number_served(self, num):
#         self.number_served = num
#
#     def increment_number_served(self, num):
#         self.number_served += num


# 这里要传参，父类的名字
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ["mango", "apple", "strawberry"]
#
#     def ice_cream_flavors(self):
#         result = ''
#         for flavor in self.flavors:
#             result += flavor + ' '
#             print("flavors: " + result)
#
#
# ice_cream = IceCreamStand("Vicky's", "dessert")
# ice_cream.ice_cream_flavors()


# 9-7 9-8
# class Privileges():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.privileges = ["can add post", "can delete post", "can ban user"]
#     def show_privileges(self):
#         for privilege in self.privileges:
#             print(self.first_name + " " + self.last_name + " " + privilege)
#
#
# class User():
#     def __init__(self, first_name, last_name, **other_info):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print("info is", self.first_name, self.last_name)
#
#     def greet_user(self):
#         print("Hello, ", self.first_name + " " + self.last_name)
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name, **other_info):
#         super().__init__(first_name, last_name, **other_info)
#         self.privileges = Privileges(self.first_name, self.last_name)


# 9-9
# class Car():
#     """一次模拟汽车的简单尝试"""
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.model + ' ' + self.make
#         return long_name.title()
#
#     def read_odometer(self):
#         print('This car has ' + str(self.odometer_reading) + ' miles on it')
#
#     def update_odometer(self, mile):
#         if mile >= self.odometer_reading:
#             self.odometer_reading = mile
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#     def fill_gas_tank(self):
#         print("car fill")
#
#
# class Battery():
#     def __init__(self, battery_size=70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print("电瓶的尺寸是 " + str(self.battery_size))
#
#     def get_range(self):
#         if self.battery_size == 70:
#             battery_range = 240
#         if self.battery_size == 80:
#             battery_range = 270
#         if self.battery_size == 85:
#             battery_range = 285
#         message = "This car can go approximately " + str(battery_range)
#         message += " miles on a full charge"
#         print(message)
#
#     def update_battery(self):
#         if self.battery_size != 85:
#             self.battery_size = 85
#
#
# class ElectricCar(Car):
#     """电动车"""
#     def __init__(self, make, model, year, battery):
#         super().__init__(make, model, year)
#         self.battery = Battery(battery)
#
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-kwh battery")
#
#     def fill_gas_tank(self):
#         print("This car doesn't need a gas tank")
#
#
# my_tesla = ElectricCar('tesla', 'models', "2021", 80)
# print(my_tesla.get_descriptive_name())
# print(my_tesla.describe_battery())
# print(my_tesla.fill_gas_tank())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.update_battery()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


# 9-10

# 9-14
# from random import randint
#
#
# class Die:
#     def __init__(self, sides="6"):
#         self.sides = int(sides)
#
#     def roll_die(self):
#         times = 0
#         while times < 10:
#             num = randint(1, self.sides)
#             print(num)
#             times += 1
#
#
# print("success main")
#
#
# my_num = Die(10)
# my_num.roll_die()

