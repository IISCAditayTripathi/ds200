import json
import math
import statistics
import matplotlib
import numpy as np
from collections import defaultdict
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

file = json.load(open('water_charges_surat.json'))


date = []
water_charges = []
for data in file['data']:
    try:
        water_charges.append(float(str(data[2])))
        date.append(data[1])
    except:
        pass

per_month = defaultdict(list)
per_month_water_avg = []

for day, charges in zip(date, water_charges):
    day = day.split('/')
    month = day[1]+'/'+day[2][2:]
    per_month[month].append(charges)

avg_charges = []
max_charges = []
min_charges = []
all_points = []
for key, items in per_month.items():
    all_points.append(items)
    avg_charges.append([key, statistics.mean(items), max(items), min(items)])


x = [a for a in range(len(avg_charges))]
y = [a[1] for a in avg_charges]
f = plt.figure()
fig, ax = plt.subplots()
ax.bar(x,y)
ax.set_title('Avg. Water Meter Charges collection by Surat Municipal Corporation per month starting Feb 2017', fontsize=10, pad=20)
ax.set_ylabel('Avg. water charges per month')
ax.set_xlabel('Month number starting from Feb. 2017')
fig.set_size_inches(8.5, 8.5)
plt.savefig('bar_plot_water_charges_surat.png')


fig, ax = plt.subplots()
ax.scatter(x,y)
ax.set_title('Avg. Water Meter Charges collection by Surat Municipal Corporation per month starting Feb 2017', fontsize=10, pad=20)
ax.set_ylabel('Avg. water charges per month')
ax.set_xlabel('Month number starting from Feb. 2017')
fig.set_size_inches(8.5, 8.5)
plt.savefig('scatter_plot_water_charges_surat.png')

fig, ax = plt.subplots()
ax.boxplot(all_points, labels=x, patch_artist=True, meanline=True, showfliers=False)
ax.set_title('Water Meter Charges collection by Surat Municipal Corporation per month starting Feb 2017', fontsize=20, pad=20)
ax.set_ylabel('Water charges per month')
ax.set_xlabel('Month number starting from Feb. 2017')
fig.set_size_inches(16.5, 8.5)
plt.savefig('box_plot_water_charges_surat.png')

