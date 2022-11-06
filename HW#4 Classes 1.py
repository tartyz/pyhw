# 1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed, break_speed, mileage_info
# 2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод seating_capacity
# 3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)
# 4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus
# 5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами school_address, main_subject
# 6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color
# 7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри: від Ведмідь і від Вовк,
# створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.
# Магічні методи:
# Додатково: 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу, лише коли population > 1500,
# інакше повертається повідомлення: "Your city is too small". Підказка: використовуєте для цього завдання магічні методи
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def increase_speed(self):
        print (f'Increase speed up tu speed limit = {self.max_speed}kn/h')
    def break_speed(self):
        print(f'Brake in cse speed is over = {self.max_speed}kn/h')
    def mileage_info(self):
        print(f'mileage info = {self.mileage}km')
print('#1. Ford is class Vechicle:')
ford = Vehicle(250, 51000)
ford.increase_speed()
ford.mileage_info()
ford.break_speed()
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seats_qty):
        super().__init__(max_speed, mileage)
        self.seats_qty = seats_qty
    def seating_capacity(self):
        print(f'Seating capacity is: {self.seats_qty}')
print ("Bus1  info:")
bus1  = Bus(120, 15000, 18)
bus1.increase_speed()
bus1.mileage_info()
bus1.break_speed()
bus1.seating_capacity()

print(" #3 Is 'Bus' subclass of 'Vehicle'?:", issubclass(Bus, Vehicle))

school_bus = Bus(90, 80000, 45)
school_bus.increase_speed()
school_bus.mileage_info()
school_bus.seating_capacity()
school_bus.break_speed()
print('#4.1. Is school_bus the object of Vehicle:', isinstance(school_bus, Vehicle))
print('#4.2. Is school_bus the object of Bus:', isinstance(school_bus, Bus))

print ('#5 ')
class School:
    def __init__(self,get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students
    def school_address(self):
        print (f'Find school address by students q-ty ={self.number_of_students}')
    def main_subject(self):
        print (f'Find main subject by school ID is: {self.get_school_id}')
school1 = School(32654, 350)
school1.school_address()
school1.main_subject()
print ('#6')
class SchoolBus(Bus, School):
    def __init__(self, max_speed, mileage, seats_qty, get_school_id, number_of_students):
        """

        :rtype: object
        """
        super(). __init__(max_speed, mileage, seats_qty)
        School. __init__(self, get_school_id, number_of_students)
    def school_address(self):
        print(f'Find school address by students q-ty ={self.number_of_students}')

    def main_subject(self):
        print(f'Find main subject by school ID is: {self.get_school_id}')
    def bus_school_color(self):
        print (f'Bus color by School id {self.get_school_id} is white')

sbc = SchoolBus(110, 88000, 52, 32597, 550)
sbc.school_address()
sbc.main_subject()
sbc.bus_school_color()
print  ('#7')
class Bear:
    def __init__(self, name, eat):
        self.name = name
        self.eat = eat
    def info(self):
        print (f'I amd Bear {self.name}.I eat {self.eat}.')
    def MakeSound(self):
        print('Ro-aaa-rrr!!!')

class Wolf:
    def __init__(self, name, eat):
        self.name = name
        self.eat = eat
    def info(self):
        print (f'I amd Wolf {self.name}.I eat {self.eat}.')
    def MakeSound(self):
        print('Auuuu!!!')

bear1 = Bear("Winney", "Honey")
woolf1 = Wolf("Jack", "Chicken")

for animal in (bear1, woolf1):
        animal.info()
        animal.MakeSound()
print ('#8')

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def __gt__(self, populationA=1500):
        if self.population > populationA:
            return f'City {self.name} with {self.population} poplation'
        else:
            return 'Your city is too small'
city_a = City("Kaakziabra", 500)
print ('infor regarding city_a:', city_a. __gt__())
city_b = City('infor regarding city_b:'"Kyiv", 3000000)
print (city_b. __gt__())
