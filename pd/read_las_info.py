import lasio
import os
from pandas import DataFrame as df


class Data:
    def __init__(self, output=r"D:\6. Учеба\1 курс\1 курс\5. Программирование\pd\las_file"):
        # Ссылка на директорию. При скачивании las файлов, необходимо скорректировать
        self.output = output

    # Чтение файлов, получение ссылок на файлы
    def __name(self):
        name = []
        for root, dirs, files in os.walk(self.output):
            for filename in files:
                name.append(filename)
        return name

    # Создаем DF по скважинам
    def __creat_df(self):
        global_direct = {}
        for well in self.__name():
            well_las = lasio.read(self.output + '\\' + well)
            keys = well_las.keys()
            direct = {}
            for key in keys:
                direct[key] = well_las[key]

            global_direct[well] = df(direct)
        return global_direct

    def __call__(self, *args, **kwargs):
        return self.__info()

    def __info(self):
        general = self.__creat_df()
        for well in self.__name():
            print(general[well].info())


run = Data()
run()



