

class Car:

    def __init__(self, title, model, color, engine):
        self.title = title
        self.model = model
        self.color = color
        self.engine = engine

    def start_engine(self):
        print(f"On {self.title} {self.model} engine starting!")

    def stop_engine(self):
        print(f"Off {self.title} {self.model} engine stopping!")

    def get_info(self):
        print(f'title: {self.title},'
              f'model: {self.model},'
              f'color: {self.color},'
              f'engine: {self.engine}')

