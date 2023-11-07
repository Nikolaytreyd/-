import numpy as np
from prettytable import PrettyTable


class Grid:

    def __init__(self):
        # Размеры куба
        self.size_x = 5000
        self.size_y = 5000
        self.z_min = 1800
        self.z_max = 1810

        # Шаг сетки
        self.step_x = 1000
        self.step_y = 1000
        self.step_z = 10

    # Атрибуты сетки
    @property
    def model(self):
        return np.meshgrid(
            np.linspace(0, self.size_x, self.step_x),
            np.linspace(0, self.size_y, self.step_y),
            np.linspace(self.z_min, self.z_max, self.step_z)
        )

    @property
    def geometric_volume(self):
        return self.size_x * self.size_y * (self.z_max - self.z_min)

    # Количество ячеек
    @property
    def size_params(self):
        return {'cells_x': self.size_x // self.step_x,
                'cells_y': self.size_y // self.step_y,
                'cells_z': (self.z_max - self.z_min) // self.step_z}

    # Куб пористости
    @property
    def porosity(self):
        return np.random.uniform(low=0.05, high=0.12, size=(self.size_params['cells_x'],
                                                            self.size_params['cells_y'],
                                                            self.size_params['cells_z']))
    # Обновление куба пористости
    @porosity.setter
    def porosity(self, low, high):
        return np.random.uniform(low=low, high=high, size=(self.size_params['cells_x'],
                                                           self.size_params['cells_y'],
                                                           self.size_params['cells_z']))

    # Куб нефтенасыщенности
    @property
    def soil(self):
        return np.random.uniform(low=0.43, high=0.52, size=(self.size_params['cells_x'],
                                                            self.size_params['cells_y'],
                                                            self.size_params['cells_z']))

    # Куб нефтенасыщенности
    @soil.setter
    def soil(self, low, high):
        return np.random.uniform(low=low, high=high, size=(self.size_params['cells_x'],
                                                           self.size_params['cells_y'],
                                                           self.size_params['cells_z']))
    @property
    def coverage_rate(self):
        return np.random.uniform(low=0.573, high=0.685, size=(self.size_params['cells_x'],
                                                              self.size_params['cells_y'],
                                                              self.size_params['cells_z']))
    @coverage_rate.setter
    def coverage_rate(self, low, high):
        return np.random.uniform(low=low, high=high, size=(self.size_params['cells_x'],
                                                           self.size_params['cells_y'],
                                                           self.size_params['cells_z']))

    @property
    def displacement_rate(self):
        return np.random.uniform(low=0.472, high=0.843, size=(self.size_params['cells_x'],
                                                              self.size_params['cells_y'],
                                                              self.size_params['cells_z']))
    @displacement_rate.setter
    def displacement_rate(self, low, high):
        return np.random.uniform(low=low, high=high, size=(self.size_params['cells_x'],
                                                           self.size_params['cells_y'],
                                                           self.size_params['cells_z']))

    def __str__(self):
        table = PrettyTable()
        table.field_names = ['ПАРАМЕТР', 'РЕЗУЛЬТАТ']
        table.add_row(['Геологические запасы, млн.куб.м.', str(np.sum(self.porosity *
                                                                      self.soil *
                                                                      self.geometric_volume) / 1_000_000)])
        table.add_row(['Извлекаемые запасы, млн.куб.м.', str(np.sum(self.porosity *
                                                                    self.soil *
                                                                    self.geometric_volume *
                                                                    self.coverage_rate *
                                                                    self.displacement_rate) / 1_000_000)])
        return table


if __name__ == '__main__':
    grid = Grid()
    print(grid.__str__())