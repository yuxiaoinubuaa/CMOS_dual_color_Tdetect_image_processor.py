# @Time    : 2020/8/27 15:41
# @Author  : Xiao YU

from scipy.interpolate import interp1d
from skimage import io
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import re

#root folder of data
DATADIR = os.getcwd()

#Reading out all the file names into one array.
strings = os.listdir(os.getcwd())

#Adding "," between names and put all the subfolder names into one string.
BIG_string =','
for item in strings:
    BIG_string = BIG_string + item + ','

#Extracting numbers which are the files containing data in the string
Num_strings = re.findall(r"[-+]?\d*\.\d+|\d+", BIG_string)

currents = np.asfarray(Num_strings, float)
currents.sort()

#Making an array of strings for the names of the data folders.
currents_string = []
for item in currents:
    item = '%.2f'%item
    currents_string.append(item)

#currents_string should be ["6.00", "6.50", "7.00", "7.50", "8.00", "8.50", "9.00", "9.50", "10.00", "10.50", "11.00", "11.50", "12.00", "12.50", "13.00", "13.50", "14.00", "14.50"]

T_reference = [500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140, 2150, 2160, 2170, 2180, 2190, 2200, 2210, 2220, 2230, 2240, 2250, 2260, 2270, 2280, 2290, 2300, 2310, 2320, 2330, 2340, 2350, 2360, 2370, 2380, 2390, 2400, 2410, 2420, 2430, 2440, 2450, 2460, 2470, 2480, 2490, 2500, 2510, 2520, 2530, 2540, 2550, 2560, 2570, 2580, 2590, 2600, 2610, 2620, 2630, 2640, 2650, 2660, 2670, 2680, 2690, 2700, 2710, 2720, 2730, 2740, 2750, 2760, 2770, 2780, 2790, 2800, 2810, 2820, 2830, 2840, 2850, 2860, 2870, 2880, 2890, 2900, 2910, 2920, 2930, 2940, 2950, 2960, 2970, 2980, 2990, 3000, 3010, 3020, 3030, 3040, 3050, 3060, 3070, 3080, 3090, 3100, 3110, 3120, 3130, 3140, 3150, 3160, 3170, 3180, 3190, 3200, 3210, 3220, 3230, 3240, 3250, 3260, 3270, 3280, 3290, 3300, 3310, 3320, 3330, 3340, 3350, 3360, 3370, 3380, 3390, 3400, 3410, 3420, 3430, 3440, 3450, 3460, 3470, 3480, 3490, 3500, 3510, 3520, 3530, 3540, 3550, 3560, 3570, 3580, 3590, 3600, 3610, 3620, 3630, 3640, 3650, 3660, 3670, 3680, 3690, 3700, 3710, 3720, 3730, 3740, 3750, 3760, 3770, 3780, 3790, 3800, 3810, 3820, 3830, 3840, 3850, 3860, 3870, 3880, 3890, 3900, 3910, 3920, 3930, 3940, 3950, 3960, 3970, 3980, 3990, 4000]
ratio_reference = [5.43018689360223E-05, 6.71027251392767E-05, 0.000082260195703524, 0.000100082459707905, 0.000120899643531073, 0.000145063469127727, 0.000172946753769571, 0.000204942770713111, 0.000241464481456737, 0.000282943651148525, 0.000329829859325168, 0.000382589418526084, 0.000441704213462045, 0.000507670473352523, 0.000580997489808414, 0.000662206292254061, 0.000751828292380639, 0.000850403908526141, 0.000958481180207746, 0.00107661438231042, 0.001205362647679, 0.00134528860608548, 0.0014969570467625, 0.00166093361091926, 0.00183778351989721, 0.00202807034388763, 0.00223235481542765, 0.00245119369122076, 0.00268513866519513, 0.00293473533512158, 0.00320052222456329, 0.00348302986142264, 0.00378277991388715, 0.00410028438415456, 0.00443604485993736, 0.00479055182340643, 0.00516428401693182, 0.00555770786471253, 0.00597127694915585, 0.00640543154066756, 0.0068605981793446, 0.00733718930692038, 0.00783560294719643, 0.00835622243310161, 0.00889941617844844, 0.00946553749240388, 0.0100549244346574, 0.0106678997092496, 0.0113047705950197, 0.0119658289106365, 0.0126513510121962, 0.0133615978213962, 0.0140968148823303, 0.0148572324449917, 0.0156430655736193, 0.0164545142780744, 0.0172917636664926, 0.0181549841175144, 0.0190443314704614, 0.019959947231888, 0.0209019587970055, 0.021870479684538, 0.0228656097836398, 0.0238874356115666, 0.0249360305808599, 0.0260114552748684, 0.0271137577304931, 0.0282429737271056, 0.0293991270806494, 0.0305822299419944, 0.0317922830986693, 0.0330292762791556, 0.0342931884589783, 0.0355839881678806, 0.0369016337974189, 0.0382460739083638, 0.0396172475373362, 0.0410150845021523, 0.0424395057053929, 0.0438904234357508, 0.04536774166675, 0.0468713563524628, 0.0484011557198872, 0.0499570205576792, 0.0515388245009616, 0.0531464343119642, 0.0547797101562723, 0.0564385058744894, 0.0581226692491418, 0.0598320422666749, 0.0615664613744135, 0.0633257577323759, 0.0651097574598505, 0.0669182818766622, 0.0687511477390677, 0.0706081674702386, 0.0724891493852997, 0.0743938979109066, 0.0763222137993558, 0.0782738943372323, 0.080248733548609, 0.0822465223928217, 0.0842670489568514, 0.0863100986423542, 0.0883754543473834, 0.0904628966428587, 0.092572203943838, 0.0947031526756582, 0.0968555174350097, 0.0990290711460195, 0.101223585211415, 0.103438829658854, 0.105674573282488, 0.107930583779863, 0.110206627884227, 0.112502471492336, 0.114817879787854, 0.117152617360431, 0.119506448320544, 0.121879136410212, 0.124270445109656, 0.126680137740006, 0.129107977562148, 0.131553727871803, 0.134017152090925, 0.136498013855512, 0.138996077099922, 0.141511106137787, 0.144042865739604, 0.1465911212071, 0.149155638444459, 0.151736184026486, 0.154332525263814, 0.156944430265209, 0.159571667997085, 0.162214008340288, 0.164871222144245, 0.16754308127854, 0.170229358682009, 0.172929828409425, 0.17564426567584, 0.178372446898668, 0.181114149737573, 0.18386915313223, 0.186637237338034, 0.18941818395982, 0.192211775983658, 0.195017797806787, 0.197836035265752, 0.200666275662805, 0.203508307790623, 0.20636192195541, 0.209226909998433, 0.212103065316046, 0.21499018287826, 0.217888059245912, 0.220796492586469, 0.223715282688542, 0.22664423097513, 0.229583140515664, 0.232531816036878, 0.235490063932567, 0.238457692272259, 0.241434510808853, 0.244420330985264, 0.247414965940106, 0.250418230512458, 0.253429941245742, 0.256449916390768, 0.259477975907947, 0.262513941468741, 0.26555763645636, 0.268608885965744, 0.271667516802865, 0.274733357483368, 0.277806238230589, 0.280885990972979, 0.283972449340948, 0.28706544866317, 0.290164825962363, 0.293270419950576, 0.296382071024002, 0.299499621257338, 0.302622914397721, 0.305751795858257, 0.308886112711154, 0.312025713680505, 0.315170449134703, 0.318320171078542, 0.321474733145001, 0.324633990586728, 0.327797800267256, 0.330966020651945, 0.334138511798688, 0.337315135348375, 0.340495754515148, 0.343680234076443, 0.346868440362846, 0.35006024124777, 0.353255506136966, 0.356454105957878, 0.359655913148853, 0.362860801648226, 0.366068646883276, 0.36927932575907, 0.372492716647215, 0.375708699374503, 0.378927155211483, 0.38214796686095, 0.385371018446376, 0.388596195500269, 0.391823384952497, 0.395052475118548, 0.398283355687767, 0.401515917711561, 0.404750053591567, 0.40798565706782, 0.411222623206891, 0.414460848390028, 0.417700230301294, 0.420940667915705, 0.424182061487377, 0.427424312537687, 0.430667323843452, 0.433910999425124, 0.437155244535018, 0.44039996564556, 0.443645070437578, 0.446890467788618, 0.450136067761308, 0.453381781591762, 0.456627521678025, 0.459873201568575, 0.463118735950865, 0.466364040639927, 0.469609032567029, 0.472853629768388, 0.476097751373943, 0.479341317596195, 0.482584249719102, 0.485826470087048, 0.489067902093874, 0.492308470171981, 0.495548099781496, 0.498786717399522, 0.502024250509445, 0.505260627590331, 0.508495778106382, 0.511729632496483, 0.514962122163811, 0.518193179465533, 0.521422737702577, 0.524650731109481, 0.527877094844325, 0.531101764978741, 0.534324678488003, 0.537545773241201, 0.54076498799149, 0.543982262366428, 0.54719753685839, 0.550410752815072, 0.553621852430065, 0.556830778733523, 0.560037475582906, 0.563241887653813, 0.566443960430888, 0.569643640198814, 0.572840874033393, 0.576035609792698, 0.579227796108318, 0.58241738237668, 0.58560431875045, 0.588788556130021, 0.591970046155079, 0.595148741196251, 0.598324594346834, 0.601497559414607, 0.604667590913713, 0.607834644056638, 0.610998674746249, 0.614159639567928, 0.617317495781778, 0.620472201314901, 0.623623714753767, 0.626771995336649, 0.629917002946137, 0.633058698101733, 0.636197041952518, 0.639331996269892, 0.642463523440396, 0.6455915864586, 0.648716148920071, 0.651837175014408, 0.654954629518359, 0.658068477789, 0.66117868575699, 0.664285219919898, 0.667388047335598, 0.670487135615738, 0.673582452919269, 0.676673967946056, 0.679761649930544, 0.682845468635501, 0.685925394345822, 0.689001397862404, 0.692073450496079, 0.695141524061625, 0.698205590871829, 0.701265623731619, 0.704321595932261, 0.707373481245617, 0.710421253918463, 0.713464888666873, 0.716504360670662, 0.719539645567888, 0.722570719449415, 0.725597558853538, 0.728620140760661, 0.731638442588038, 0.734652442184567, 0.73766211782565, 0.740667448208096, 0.743668412445089, 0.746664990061213, 0.749657160987524, 0.752644905556679, 0.755628204498122, 0.758607038933323, 0.76158139037106, 0.764551240702766, 0.76751657219792, 0.770477367499489, 0.773433609619422, 0.776385281934195, 0.779332368180399, 0.782274852450391, 0.78521271918797, 0.788145953184128, 0.791074539572824, 0.793998463826822, 0.796917711753564, 0.799832269491096, 0.802742123504035, 0.805647260579584, 0.808547667823586, 0.811443332656627, 0.814334242810182, 0.817220386322798, 0.820101751536329, 0.8229783270922, 0.825850101927729]

resul_max =[]          #The maximum value of the ratio in each temperature
resul_min =[]          #The miniimum value of the ratio in each temperature
resul_stdarr =[]       #Standard error of the ratio in each temperature
resul_ratio = []       #Array containing the calculated ratios in each temperature

#loop to open every subfolder
for category in currents_string:
    path = os.path.join(DATADIR, category)

    #Arrays for calculated data in a certain lamp current
    ratio = []
    wavelen_resul = []
    wavelen_min = []
    wavelen_max = []
    wavelen_stdarr = []

    #loop to open each tiff file in a subfoler
    for img in os.listdir(path):
        #Read tiff file into an array
        img_array = io.imread(os.path.join(path, img))
        #Selecting regions for two color channels and background
        sub_array_red = img_array[920:940, 700:720]
        sub_array_blue = img_array[920:940, 1380:1400]
        backgrd = img_array[50:70, 50:70]
        #Taking mean value in the selected regions and calculated signal intensity
        intensity_red = np.mean(sub_array_red) - np.mean(backgrd)
        intensity_blue = np.mean(sub_array_blue) - np.mean(backgrd)
        #Calculating the ratio of signal intensity
        intensity_ratio = intensity_blue/intensity_red
        #Adding the calculated ratio to an array
        ratio.append(intensity_ratio)

    #Calculating the mean value of the ratio in a certain temperature
    wavelen_resul = np.mean(ratio)

    #getting the starndard error, maximum and minimum value of the ratio in a certain temperature
    wavelen_max = np.max(ratio)
    wavelen_min = np.min(ratio)
    wavelen_stdarr = np.std(ratio)

    #printing the calculated ratios and the array length, only for debugging use
    print(ratio)
    print(len(ratio))

    #adding the calculated mean value, max and min values of the ratio into a final result array
    resul_ratio.append(wavelen_resul)
    resul_max.append(wavelen_max)
    resul_min.append(wavelen_min)
    resul_stdarr.append(wavelen_stdarr)


#Printing the final ratios in different temperature
print('Ratios')
print(resul_ratio)
print('Standard errors')
print(resul_stdarr)
print('Minimum value of the ratio in each lamp current')
print(resul_min)
print('Maximum value of the ratio in each lamp current')
print(resul_max)

#Calculating tempreature and related parameters with the calculated ratio
f1 = interp1d(ratio_reference, T_reference, kind='cubic')
T_resul = f1(resul_ratio)
T_resul_max = f1(resul_max)
T_resul_min = f1(resul_min)
T_delta = T_resul_max - T_resul_min
T_ratio = T_delta/T_resul

print('Maximum values of the Temperature in each lamp current')
print(T_resul_max)
print('Minimum values of the Temperature in each lamp current')
print(T_resul_min)
print('Difference between maximum and minimum values in each lamp current')
print(T_delta)
print('Delta_T/T')
print(T_ratio)
print('strings')
print(strings)
print('currents_string')
print(currents_string)
print('currents')
print(currents)

#Printing the length of result and error arrays, only for debugging use
# print(len(resul))
# print(len(resul_min))
# print(len(resul_max))

#Ratio results with max and min vaules
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(currents, resul_ratio, '-o')
ax.fill_between(currents, resul_min, resul_max, alpha=0.2)
ax.set_xlabel('Lamp current (A)', fontsize = 14)
ax.set_ylabel('Ratio of blue versus red band', fontsize = 14)
ax.set_title('Ratio of two band radiances',fontsize=16)
ax.grid(True, linestyle='-')
ax.set_xlim(currents[0]-0.5, currents[-1]+0.5)
ax.set_xticks(np.arange(math.floor(currents[0]+0.4), math.ceil(currents[-1]+0.4), 1))
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
# plt.show()

#Ratio results with standard errors
fig, ax = plt.subplots(figsize=(10, 5))
ax.errorbar(currents, resul_ratio, yerr=resul_stdarr, fmt='-o', ms=5)
ax.set_xlabel('Lamp current (A)', fontsize = 14)
ax.set_ylabel('Ratio of blue versus red band', fontsize = 14)
ax.set_title('Ratio of two band radiances',fontsize=16)
ax.grid(True, linestyle='-')
ax.set_xlim(currents[0]-0.5, currents[-1]+0.5)
ax.set_xticks(np.arange(math.floor(currents[0]+0.4), math.ceil(currents[-1]+0.4), 1))
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

#Dtedted temprature plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(currents, T_resul,'-o')
ax.fill_between(currents, T_resul_min, T_resul_max, alpha=0.2)
ax.set_xlabel('Lamp current (A)', fontsize = 14)
ax.set_ylabel('Detected temperature (K)', fontsize = 14)
ax.set_title('Measured temperature by dual-color method',fontsize=16)
ax.grid(True, linestyle='-')
ax.set_xlim(currents[0]-0.5, currents[-1]+0.5)
ax.set_xticks(np.arange(math.floor(currents[0]+0.4), math.ceil(currents[-1]+0.4), 1))
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

#ΔT versus T plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(currents, T_ratio,'-o')
ax.set_yscale('log')
ax.set_xlabel('Lamp current (A)', fontsize = 14)
ax.set_ylabel('ΔT/T', fontsize = 14)
ax.set_title('Ratio of ΔT/T',fontsize=16)
ax.grid(True, linestyle='-')
ax.set_xlim(currents[0]-0.5, currents[-1]+0.5)
ax.set_xticks(np.arange(math.floor(currents[0]+0.4), math.ceil(currents[-1]+0.4), 1))
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
plt.show()