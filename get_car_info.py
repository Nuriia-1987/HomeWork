# get_car_info —> def get_car_info(car): —> car_info

from .create_cars import Car

class Get(Car):

    def car_info(self):
        print(f"""
            Title: {self.title}
            Model: {self.model}
            Color: {self.color}
            Engine: {self.engine}
            """)
