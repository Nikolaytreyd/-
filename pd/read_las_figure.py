
import lasio
import os
from matplotlib import pyplot as plt

name = []
output = "D:\ласы 227 скв Норвгеии\карбонаты" #нужно указать другой путь на директорию las-файлов
for root, dirs, files in os.walk(output):
    for filename in files:
        name.append(filename)

for well in range(len(name)):
    print('-------')
    print(name[well])
    well_las = lasio.read(output + '\\' + name[well])
    Keys = well_las.keys()
    print(Keys)
    print(well_las[Keys[0]][0])
    fig, axs = plt.subplots(figsize=(14, 22), ncols=len(Keys), nrows=1, sharey=True)
    # -------------------------------------------------------------------------------------
    for i in range(1, len(Keys)):
        axs[i-1].plot(well_las[Keys[i]], well_las[Keys[0]])
        axs[i-1].set_ylim(well_las[Keys[0]][0], well_las[Keys[0]][-1])
        axs[i-1].set_xlabel(str(Keys[i]))
        axs[i-1].locator_params(axis='x', nbins=5)
        axs[i-1].locator_params(axis='y', nbins=20)
        axs[i-1].grid()
        axs[i-1].invert_yaxis()
        axs[i-1].set_title(str(Keys[i]))
        fig.tight_layout()
    fig.savefig('D:\\ласы 227 скв Норвгеии\\планшеты\\' + name[well] + '.png',
                orientation='landscape')
    plt.clf()





