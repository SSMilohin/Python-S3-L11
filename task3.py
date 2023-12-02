import csv
import matplotlib.pyplot as plt


with open('passengers.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [row for row in reader]

dates = [row[0] for row in data]
passengers = [int(row[1]) for row in data]

plt.figure(figsize=(10, 5))
plt.plot(range(1, len(passengers) + 1), passengers, color='black', label='Пассажиропоток', marker='.', markerfacecolor='yellow', markersize=6)
plt.xlabel('Месяц')
plt.ylabel('Количество пассажиров')
plt.title('График пассажиропотока (1949 - 1960 гг.)')
plt.grid(True)
plt.xticks(range(0, len(data)+12, 12))
plt.legend()
plt.show()


years = [1951, 1952, 1953, 1954, 1955]
months = list(range(1, 13))
annual_data = []
for year in years:
    annual_data.append([passengers[i] for i in range(len(dates)) if dates[i].startswith(str(year))])

fig, ax = plt.subplots(figsize=(10, 5))
for i in range(len(years)):
    item_width = 1 / len(years)
    ax.bar([x + i*item_width for x in months], annual_data[i], width=item_width, align='edge', label=str(years[i]))

plt.xlabel('Месяц')
plt.ylabel('Количество пассажиров')
plt.title('Распределение пассажиров по месяцам в 1951 - 1955 гг.')
plt.xticks(months)
plt.grid(True, axis='x')
ax.legend()
plt.show()
