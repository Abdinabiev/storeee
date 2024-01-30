
# student = {}

# student["name"] = input("атын:  ")
# student["age"] = input("жашын: ")
# student["univer"] = input("универ:  ")

# print(student)


# customer = {"name": "Marsel", 'age': "18", "city" : "Bishkek"}
# print(customer["city"])


# people=["Анна","Олег","Мария","Анна","Мария","Мария", "Мария","Мария"]

# persons = {}

# persons["Анна"]= people.count("Анна")
# persons["Олег"]= people.count("Олег")
# persons["Мария"]= people.count("Мария")
# print(persons)


# # products = {"apple": 50, "banana": 20, "cherry": 10}

# # user = input("Soz jaz: ")

# # if user in products:
# #     print(f"{user}: {products[user]} som")
# # else:
# #     print("Error")


# ; people=["Анна","Олег","Мария","Анна","Мария","Мария"]
# ; a= people.count("Анна")
# ; b=people.count("Олег")
# ; v=people.count("Мария")

# ; persons = {}
# ; persons["Анна"]= a
# ; persons["Олег"]=b
# ; persons["Мария"]=v
# ; print(persons)


# ; i = 10
# ; print('Старт')
# ; while i != 0:
# ;     print(i)
# ;     i -=1
# ; else:
# ;     print("Конец")


# ; nums = []
# ; for i in range(1, 10):
# ;     nums.append(i)

# ; print('Старт')
# ; for j in nums[::-1]:
# ;     print(j)


# ; passwords = ['admin', 'qwert', 3434, 'qwer23', 'asdf']
# ; for i in (passwords):
# ;     print(i)



# ; passwords = 'admin'

# ; while True:
# ;     word = input(" :")
# ;     if word == passwords:
# ;         print("Tuura")
# ;         break
# ;     else:
# ;         continue



# ; password = "admin"
# ; for i in range(10):
# ;     name = input("Поиск кода:  ")
# ;     if name in password:
# ;         print('Код заверщён! ')
# ;         break
# ;     else:
# ;         print("Код еще не заверщён! ")
# ;         continue





# ; password = "#"
# ; while True:
# ;     name = input('Бир белгини танданыз: ')
# ;     if name in password:
# ;         break
# ;     if name in ('+', '-', '*', '/' ):
# ;         a = int(input("Биринчи санды жазыңыз: "))
# ;         b = int(input("Экинчи санды жазыңыз: "))
# ;         if name == "+":
# ;             print(a + b)
# ;         elif name == "-":
# ;             print(a - b)
# ;         elif name == "*":
# ;             print(a * b)
# ;         elif name == "/":
# ;             if b != 0:
# ;                 print(a / b)
# ;             else:
# ;                 print("Деление на ноль! ")
# ;     else:
# ;         print("Туура эмес белги!!! ")









# ; num = 0
# ; while True:
# ;     user = int(input("Напишите целое число: "))
# ;     num += user
# ;     if user == 0:
# ;         print(num)






# ; num = int(input("number: "))
# ; for i in range(1, 11):
# ;     print(f'{i} * {num} = {i * num}')




# ; num = 0
# ; while True:
# ;     san = int(input("Напишите целое число: "))
    
# ;     if san %2 == 0:
# ;         num  += san 
# ;     if san == 0:
# ;         print(num)
# ;         break





# ; import random

# ; num = int(input("min san jaz: "))
# ; num2 = int(input("max san jaz: "))

# ; san = random.randint(num , num2)
# ; attemts = 0

# ; while True:
# ;     i = int(input(f"Угадай число до {num2}:  "))
# ;     attemts += 1
# ;     if i == san:
# ;         print(f"Вы нашли число {san}! За столько попыток: {attemts}")
# ;         break
# ;     elif i < san:
# ;         print("Попробуйте число больше")
# ;     else:
# ;         print("Попробуйте число меньше")





# ; def check_wort(a):
# ;     if a == a[::-1]:
# ;         print('Polindrom')
# ;     else:
# ;         print("Polindrom emes")

# ; check_wort("appa")

# def sum_numbers(*args):
#     summ_nums = 0
#     for i in args:
#         if i %2 != 0:
#             summ_nums += i
#     print(summ_nums)
# sum_numbers(5,3,4,5,4,4,3)


# def sum_numbers(a,b,c):
#     return a + b + c

# print(sum_numbers(5,3,4))


# sum_numbers = lambda a,b :f"{a} {b}"

# print(sum_numbers('Hello', 'World'))



# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# def sum_numbers(e):
#     for i in e:
#         if i <= 5:

#             print(i)

# sum_numbers(a)




class Vehicle:
    def init(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage

    def vehicle_speed(self):
        return self.speed, self.mileage

class Car(Vehicle):
    def init(self, speed, mileage, fuel):
        super().init(speed, mileage)
        self.fuel = fuel

    def cars(self):
       return self.speed, self.mileage, self.fuel

class Bike(Vehicle):
    def init(self, speed, milleage, type):
        super().init(speed, milleage)
        self.type = type

    def bike1(self):
        return self.speed, self.mileage, self.type

vehicle1 = Vehicle(420, "mp/h")
car1 = Car(350, "km/h", 2.2)
bike = Bike(20, "km/p", "sport")


print(vehicle1.vehicle_speed())
print(bike.bike1())
print(car1.cars())