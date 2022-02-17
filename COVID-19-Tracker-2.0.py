import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime


###Set class and variables for different regions of Aomori.###

separator = ", "

hirosaki_area = ['Fujisaki', 'Hirakawa', 'Hirosaki', 'Inakadate', 'Itayanagi', 'Kuroishi', 'Nishimeya', 'Owani']
goshogawara_area = ['Ajigasawa', 'Fukaura', 'Goshogawara', 'Nakadomari', 'Tsugaru', 'Tsuruta']
mutsu_area = ['Higashidori', 'Kazamaura', 'Mutsu', 'Oma', 'Sai']
kamitosan_area = ['Misawa', 'Noheji', 'Rokkasho', 'Rokunohe', 'Shichinohe', 'Tohoku', 'Towada', 'Yokohama']
sannohe_area = ['Gonohe', 'Hashikami', 'Nanbu', 'Oirase', 'Sannohe', 'Shingo', 'Takko']
eastern_area = ['Hiranai', 'Imabetsu', 'Sotogahama', 'Yomogita']

class Region:

    def __init__(self, name, message, municipalities_message, municipalities, fourteen_day):
        self.name = name
        self.message = message
        self.municipalities_message = municipalities_message
        self.municipalities = municipalities
        self.cases = []
        self.fourteen_day = fourteen_day

aomori = Region('Aomori', 'in Aomori City', '', '', 0)
hachinohe = Region('Hachinohe', 'in Hachinohe City', '', '', 0)
hirosaki = Region('Hirosaki', 'in the Hirosaki Area', 'This area consists of the following municipalities: ', separator.join(hirosaki_area), 0)
goshogawara = Region('Goshogawara', 'in the Goshogawara Area', 'This area consists of the following municipalities: ', separator.join(goshogawara_area), 0)
mutsu = Region('Mutsu', 'in the Mutsu Area', 'This area consists of the following municipalities: ', separator.join(mutsu_area), 0)
kamitosan = Region('Kamitosan', 'in in the Kamitosan Area', 'This area consists of the following municipalities: ', separator.join(kamitosan_area), 0)
sannohe = Region('Sannohe', 'in the Sannohe Area', 'This area consists of the following municipalities: ', separator.join(sannohe_area), 0)
eastern = Region('Eastern', 'in the Eastern Area', 'This area consists of the following municipalities: ', separator.join(eastern_area), 0)
outside_aomori = Region('Outside Aomori', 'from outside Aomori Prefecture', '', '', 0)
aomori_prefecture = Region('Aomori', 'in Aomori Prefecture', '', '', 0)

###Create data for charts.###

filename = 'aomoricovid.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []

    for row in reader:

        date_list = datetime.strptime(row[0], '%m/%d/%Y')
        dates.append(date_list)
        aomori.cases.append(int(row[1]))
        hachinohe.cases.append(int(row[2]))
        hirosaki.cases.append(int(row[3]))
        goshogawara.cases.append(int(row[4]))
        mutsu.cases.append(int(row[5]))
        kamitosan.cases.append(int(row[6]))
        sannohe.cases.append(int(row[7]))
        eastern.cases.append(int(row[8]))
        outside_aomori.cases.append(int(row[9]))
        aomori_prefecture.cases.append(aomori.cases[-1] + hachinohe.cases[-1] + hirosaki.cases[-1] + goshogawara.cases[-1] + mutsu.cases[-1] + kamitosan.cases[-1] + sannohe.cases[-1] + eastern.cases[-1] + outside_aomori.cases[-1])
aomori.fourteen_day = round(sum(aomori.cases[-14:])/14, 1)
hachinohe.fourteen_day = round(sum(hachinohe.cases[-14:])/14, 1)
hirosaki.fourteen_day = round(sum(hirosaki.cases[-14:])/14, 1)
goshogawara.fourteen_day = round(sum(goshogawara.cases[-14:])/14, 1)
mutsu.fourteen_day = round(sum(mutsu.cases[-14:])/14, 1)
kamitosan.fourteen_day = round(sum(kamitosan.cases[-14:])/14, 1)
sannohe.fourteen_day = round(sum(sannohe.cases[-14:])/14, 1)
eastern.fourteen_day = round(sum(eastern.cases[-14:])/14, 1)
outside_aomori.fourteen_day = round(sum(outside_aomori.cases[-14:])/14, 1)
aomori_prefecture.fourteen_day = round(sum(aomori_prefecture.cases[-14:])/14, 1)

current_date = dates[-1].strftime('%b. %d, %Y')

regions = [aomori, hachinohe, hirosaki, goshogawara, mutsu, kamitosan, sannohe, eastern, outside_aomori]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates[-14:], aomori_prefecture.cases[-14:], c='red', marker='o')

ax.set_title('Cases in Aomori Prefecture (Last 14 Days)', fontsize=16)
ax.set_xlabel('Date', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Cases', fontsize=10)
ax.set_ylim(ymin=0)

ax.tick_params(axis='both', which='major')

plt.style.use('seaborn')
fig, ax = plt.subplots()
for region in regions:
    bar_1 = ax.barh(region.name, region.cases[-1], color='crimson', height=0.35, align='edge')
    bar_2 = ax.barh(region.name, region.fourteen_day, color='gold', height=-0.35, align='edge')

ax.set_title("Today's Cases by Region", fontsize=16)
ax.legend((bar_1[0], bar_2[0]), ('Today', '14-Day Average'))
ax.set_xlabel('Cases', fontsize=10)
ax.set_ylabel('Region', fontsize=10)

ax.tick_params(axis='both', which='major')

###Opening Message###

print("Welcome to the Aomori Prefecture COVID-19 Tracker.\n")
print(f"{current_date}: There were {aomori_prefecture.cases[-1]} reported COVID-19 cases {aomori_prefecture.message}. The 14-day average for the prefecture is {aomori_prefecture.fourteen_day} cases per day.")
print("\nToday's cases by region:\n")

for region in regions:
    print(f"{region.name}: {region.cases[-1]}")

print("\nTo find more information about a particular region, please enter the region's name.")
print("\nTo see a visual representation of data, please enter 'charts'.")
print("\nCase numbers are updated daily at approximately 4:30 p.m. All data is cited from the Aomori Prefectural Government."
      "\nPlease visit https://www.pref.aomori.lg.jp/ for more information.")
print("\nTo exit the program, please enter 'exit'.\n")

###Take user input.###

user_input = False
while user_input == False:
    message_1 = input()
    for region in regions:
        if message_1 == region.name or message_1 == region.name.lower():
            user_input = True
            print(f"\nToday there were {region.cases[-1]} reported COVID-19 cases {region.message}. The 14-day average for the area is {region.fourteen_day} cases per day."
                  f"\n{region.municipalities_message}{region.municipalities}")
        if message_1 == 'charts':
            user_input = True
            plt.show()
            break
        if message_1 == 'exit':
            print("Thank you for using the Aomori Prefecture COVID-19 Tracker.")
            exit()
    if user_input == False:
        print("\nPlease input a valid response.")
    user_input = False