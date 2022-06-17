#HW:
# Создать пакет - (cars)
# создать модули такие как (create_car, get_car_info)
# create_cars —> Создать Абстрактный класс (Car)
# Создать методы для Car - (start_engine, stop_engine)
# get_car_info —> def get_car_info(car): —> car_info
# создать main.py файл и там использовать ваш пакет (cars)

from cars.create_cars import Car

bmw = Car('BMW', 'e34', 'black', 8)
bmw.get_info()
bmw.start_engine()
bmw.stop_engine()


