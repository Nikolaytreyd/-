'''
import lasio
import os
from matplotlib import pyplot as plt

name = []
output = "D:\ласы 227 скв Норвгеии\карбонаты"
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

'''
'''
from random import gauss, uniform, randint
from math import sqrt
from matplotlib import pyplot as plt

def capillary(PERM, PORO, r):
    PC = []
    SW = []
    b = randint(3, 5)
    a = 21.351*pow(PERM, -0.267)
    for sw in range(100, 1100, 80):
        while True:
            if sw >= 1000:
                sw = 1000
            swi = round(gauss(sw, 10) / 1000, 4)
            if swi >= 1:
                swi = 1
            break
        Pc = round(
            ((1 - swi) * r / (sqrt(abs(PERM-1000) / PORO) * 3.1415))
             * (a * uniform(0.950, 1.050) + b)
             * pow((1000 - sw) / 1000, a + uniform(-0.500, 0.500)), 4)
        if Pc > 15 or Pc < 0.001:
            continue
        else:
            PC.append(abs(Pc))
            SW.append(swi)
    return PC, SW


while True:
    ''''''
    Perm = 150
    PC_1, SW_1 = capillary(Perm/40, 0.1, 76)
    PC_2, SW_2 = capillary(Perm/10, 0.15, 76)
    PC_3, SW_3 = capillary(Perm/2, 0.25, 76)
    PC_4, SW_4 = capillary(Perm*1.5, 0.3, 76)
    PC_5, SW_5 = capillary(Perm*5, 0.4, 76)

    plt.plot(SW_1, PC_1)
    plt.plot(SW_2, PC_2)
    plt.plot(SW_3, PC_3)
    plt.plot(SW_4, PC_4)
    plt.plot(SW_5, PC_5)

    plt.ylim(0, 5)
    plt.legend(
        [
            str(int(Perm / 40)),
            str(int(Perm / 10)),
            str(int(Perm / 2)),
            str(int(Perm * 1.5)),
            str(int(Perm * 5))
        ]
    )

    # 


    plt.show()
    break
'''
'''
import lasio
from matplotlib import pyplot as plt

well_name = ['Well_1', 'Well_2', 'Well_3']

proect_name = 'Result'
input_file = 'C:\\test\\'

def sort_litho_e(output, id):
    step = 0
    exit = []
    while True:
        try:
            if output[step] == id:
                exit.append(output[step])
            else:
                exit.append(0)
            step += 1
        except IndexError:
            break
    return exit

well = 0
while True:
    try:
        plt.ion()
        plt.clf()
        las = lasio.read(input_file + '//' + proect_name + '//6.LAS_file//' + well_name[well] + '.las')
        # --------------------------------------------------------------------------------------
        Keys = las.keys()
        DEPT = las['DEPT']
        LITHO = las['LITHO']
        LITHOE = las['LITHO_E']
        PERM = las['PERM']
        PORO = las['PORO']
        NTG = las['NTG']
        SW = las['SW']
        SO = las['SO']
        SG = las['SG']
        SWL = las['SWL']

        LITHOE_1 = sort_litho_e(LITHOE, 1)
        LITHOE_2 = sort_litho_e(LITHOE, 2)
        LITHOE_3 = sort_litho_e(LITHOE, 3)
        LITHOE_4 = sort_litho_e(LITHOE, 4)
        LITHOE_5 = sort_litho_e(LITHOE, 5)
        LITHOE_6 = sort_litho_e(LITHOE, 6)
        LITHOE_7 = sort_litho_e(LITHOE, 7)
        LITHOE_8 = sort_litho_e(LITHOE, 8)
        # --------------------------------------------------------------------------------------
        fig, axs = plt.subplots(figsize=(14, 25), ncols=9, nrows=1, sharey=True)
        # -------------------------------------------------------------------------------------
        while True:
            axs[0].barh(DEPT, LITHO, color='gold')
            axs[0].patch.set_facecolor('dimgray')
            axs[0].set_xlim(0, 0.99)
            axs[0].set_ylim(DEPT[0], DEPT[-1])
            axs[0].get_xaxis().set_visible(False)
            axs[0].set_xlabel('litho', color='black')
            axs[0].invert_yaxis()
            axs[0].set_title(well_name[well] + ' - ' + 'Litho')
            break
        # -------------------------------------------------------------------------------------
        while True:
            axs[1].barh(DEPT, LITHOE_1, color='darkblue')
            axs[1].barh(DEPT, LITHOE_2, color='slateblue')
            axs[1].barh(DEPT, LITHOE_3, color='royalblue')
            axs[1].barh(DEPT, LITHOE_4, color='deepskyblue')
            axs[1].barh(DEPT, LITHOE_5, color='orange')
            axs[1].barh(DEPT, LITHOE_6, color='darkorange')
            axs[1].barh(DEPT, LITHOE_7, color='y')
            axs[1].barh(DEPT, LITHOE_8, color='olive')

            axs[1].patch.set_facecolor('dimgray')
            axs[1].set_xlim(0, 0.99)
            axs[1].set_ylim(DEPT[0], DEPT[-1])
            axs[1].get_xaxis().set_visible(False)
            axs[1].set_xlabel('LITHOE', color='black')
            axs[1].invert_yaxis()
            axs[1].set_title(well_name[well] + ' - ' + 'Litho Ex')
            break
        # --------------------------------------------------------------------------------------
        while True:
            color = 'indigo'
            axs[2].plot(PERM, DEPT, color=color)
            axs[2].set_ylim(DEPT[0], DEPT[-1])
            axs[2].set_xlabel('Perm, mD', color=color)
            axs[2].locator_params(axis='x', nbins=5)
            axs[2].locator_params(axis='y', nbins=20)
            axs[2].tick_params(color=color, labelcolor=color)
            axs[2].grid()
            axs[2].invert_yaxis()
            axs[2].set_title(well_name[well] + ' - ' + 'Perm')
            break
        # --------------------------------------------------------------------------------------
        while True:
            color = 'maroon'
            axs[3].plot(PORO, DEPT, color=color)
            axs[3].set_ylim(DEPT[0], DEPT[-1])
            axs[3].set_xlabel('Poro, share', color=color)
            axs[3].locator_params(axis='x', nbins=5)
            axs[3].locator_params(axis='y', nbins=20)
            axs[3].tick_params(color=color, labelcolor=color)
            axs[3].grid()
            axs[3].invert_yaxis()
            axs[3].set_title(well_name[well] + ' - ' + 'Poro')
            break
        # --------------------------------------------------------------------------------------
        while True:
            color = 'olive'
            axs[4].plot(NTG, DEPT, color=color)
            axs[4].set_ylim(DEPT[0], DEPT[-1])
            axs[4].set_xlabel('NTG, share', color=color)
            axs[4].locator_params(axis='x', nbins=5)
            axs[4].locator_params(axis='y', nbins=20)
            axs[4].tick_params(color=color, labelcolor=color)
            axs[4].grid()
            axs[4].invert_yaxis()
            axs[4].set_title(well_name[well] + ' - ' + 'NTG')
            break
        # --------------------------------------------------------------------------------------
        while True:
            color = 'navy'
            axs[5].plot(SW, DEPT, color=color)
            axs[5].set_ylim(DEPT[0], DEPT[-1])
            axs[5].set_xlabel('SW, share', color=color)
            axs[5].locator_params(axis='x', nbins=5)
            axs[5].locator_params(axis='y', nbins=20)
            axs[5].tick_params(color=color, labelcolor=color)
            axs[5].grid()
            axs[5].invert_yaxis()
            axs[5].set_title(well_name[well] + ' - ' + 'SW')
            break
        # --------------------------------------------------------------------------------------
        while True:
            color = 'peru'
            axs[6].plot(SO, DEPT, color=color)
            axs[6].set_ylim(DEPT[0], DEPT[-1])
            axs[6].set_xlabel('SO, share', color=color)
            axs[6].locator_params(axis='x', nbins=5)
            axs[6].locator_params(axis='y', nbins=20)
            axs[6].tick_params(color=color, labelcolor=color)
            axs[6].grid()
            axs[6].invert_yaxis()
            axs[6].set_title(well_name[well] + ' - ' + 'SO')
            break
        # --------------------------------------------------------------------------------------
        while True:
            color = 'darkcyan'
            axs[7].plot(SG, DEPT, color=color)
            axs[7].set_ylim(DEPT[0], DEPT[-1])
            axs[7].set_xlabel('SG, share', color=color)
            axs[7].locator_params(axis='x', nbins=5)
            axs[7].locator_params(axis='y', nbins=20)
            axs[7].tick_params(color=color, labelcolor=color)
            axs[7].grid()
            axs[7].invert_yaxis()
            axs[7].set_title(well_name[well] + ' - ' + 'SG')
            break
        # --------------------------------------------------------------------------------------
        while True:
            color = 'orchid'
            axs[8].plot(SWL, DEPT, color=color)
            axs[8].set_ylim(DEPT[0], DEPT[-1])
            axs[8].set_xlabel('SWL, share', color=color)
            axs[8].locator_params(axis='x', nbins=5)
            axs[8].locator_params(axis='y', nbins=20)
            axs[8].tick_params(color=color, labelcolor=color)
            axs[8].grid()
            axs[8].invert_yaxis()
            axs[8].set_title(well_name[well] + ' - ' + 'SWL')
            break
        # --------------------------------------------------------------------------------------
        fig.tight_layout()
        fig.savefig(input_file + '//' + proect_name + '//7.LAS_snapshot//' + '//Logs_' + well_name[well] + '.png',
                    orientation='landscape')
        plt.close(fig)
        print('     #5.3.' + str(well + 1), 'Планшет РИГИС по скважине', well_name[well], 'успешно создана и сохранена')
        well += 1
    except IndexError:
        break
'''
import porespy as ps
import matplotlib.pyplot as plt

im = ps.generators.blobs(shape=[500, 500], porosity=0.6, blobiness=2)
plt.imshow(im)




